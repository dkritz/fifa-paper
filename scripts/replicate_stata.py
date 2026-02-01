"""Replicate Stata 8/9 panel regressions in Python.

Assumptions:
- Data are already transformed and merged into a single panel file.
- Quadratic terms (GDP2, POP2, UrbPOP2) are precomputed.
- Country and year identifiers are present.

Outputs are printed to stdout and optionally saved to CSV.
"""

import argparse
import os
import sys


if sys.version_info < (3, 8):
    sys.stderr.write("Python 3.8+ is required. Run: python3 scripts/replicate_stata.py\n")
    sys.exit(1)

import pandas as pd
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        default="data/analysis/panel.csv",
        help="Path to the prepared panel dataset.",
    )
    parser.add_argument(
        "--entity",
        default="country",
        help="Entity (country) column name.",
    )
    parser.add_argument(
        "--time",
        default="year",
        help="Time (year) column name.",
    )
    parser.add_argument(
        "--confed",
        default="confed",
        help="Confederation column name.",
    )
    parser.add_argument(
        "--output",
        default="results",
        help="Output directory for CSV summaries.",
    )
    return parser.parse_args()


def two_way_demean(df, cols, entity, time):
    """Two-way demean columns by entity and time (within estimator)."""
    out = df.copy()
    for col in cols:
        overall = out[col].mean()
        ent_mean = out.groupby(entity)[col].transform("mean")
        time_mean = out.groupby(time)[col].transform("mean")
        out[col] = out[col] - ent_mean - time_mean + overall
    return out


def _drop_absorbed(panel, exog):
    names = list(panel.index.names)
    if len(names) < 2 or names[0] is None or names[1] is None:
        return exog, []

    entity, time = names[0], names[1]
    work = panel.reset_index()
    demeaned = two_way_demean(work, exog, entity, time)
    dropped = []
    keep = []
    for col in exog:
        if demeaned[col].var() <= 1e-12:
            dropped.append(col)
        else:
            keep.append(col)
    return keep, dropped


def fit_fe_ols(panel, dep, exog):
    keep, dropped = _drop_absorbed(panel, exog)
    if dropped:
        print("Dropped absorbed variables: {0}".format(", ".join(dropped)))
    if not keep:
        raise ValueError("All regressors absorbed by fixed effects.")

    y = panel[dep]
    X = panel[keep]
    model = PanelOLS(y, X, entity_effects=True, time_effects=True)
    res = model.fit(
        cov_type="clustered",
        cluster_entity=True,
        debiased=True,
    )
    return res


def fit_fe_iv(df, dep, exog, endog, instr, entity, time):
    cols = [dep] + exog + [endog] + instr + [entity, time]
    work = df[cols].dropna().copy()
    work = two_way_demean(work, [dep] + exog + [endog] + instr, entity, time)

    y = work[dep]
    keep_exog = [c for c in exog if work[c].var() > 1e-12]
    if not keep_exog:
        raise ValueError("All exogenous regressors absorbed by fixed effects.")

    endog_v = work[endog]
    if endog_v.var() <= 1e-12:
        raise ValueError("Endogenous regressor absorbed by fixed effects.")

    keep_instr = [c for c in instr if work[c].var() > 1e-12]
    if not keep_instr:
        raise ValueError("All instruments absorbed by fixed effects.")

    X = work[keep_exog]
    Z = work[keep_instr]

    model = IV2SLS(y, X, endog_v, Z)
    res = model.fit(cov_type="clustered", clusters=work[entity], debiased=True)
    return res


def save_summary(res, out_path):
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)
    table = res.summary.tables[1].as_csv()
    with open(out_path, "w") as handle:
        handle.write(table)


def main():
    args = parse_args()

    data_path = args.data
    if not os.path.exists(data_path):
        raise FileNotFoundError("Data file not found: {0}".format(data_path))

    df = pd.read_csv(data_path)

    dep = "fifa_points"
    base = ["gdp_pc", "gdp_pc_sq", "pop", "pop_sq"]
    macro = ["trade", "infl", "oil", "leb"]
    club = "club"
    instr = ["urbpop", "urbpop_sq"]

    required = [args.entity, args.time, dep] + base + macro + [club] + instr
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError("Missing required columns: {0}".format(missing))

    df = df.sort_values([args.entity, args.time])
    panel = df.set_index([args.entity, args.time])

    output_dir = args.output

    # Equation (1)
    res1 = fit_fe_ols(panel, dep, base)
    print("\nEquation (1) - Full sample")
    print(res1.summary)
    save_summary(res1, os.path.join(output_dir, "eq1_full.csv"))

    # Equation (2)
    res2 = fit_fe_ols(panel, dep, base + macro)
    print("\nEquation (2) - Full sample")
    print(res2.summary)
    save_summary(res2, os.path.join(output_dir, "eq2_full.csv"))

    # Equation (3) - IV with fixed effects
    res3 = fit_fe_iv(df, dep, base + macro, club, instr, args.entity, args.time)
    print("\nEquation (3) - Full sample")
    print(res3.summary)
    save_summary(res3, os.path.join(output_dir, "eq3_full.csv"))

    # By confederation
    if args.confed in df.columns:
        for confed in sorted(df[args.confed].dropna().unique()):
            subset = df[df[args.confed] == confed]
            if subset.empty:
                continue
            panel_sub = subset.set_index([args.entity, args.time])

            try:
                res1c = fit_fe_ols(panel_sub, dep, base)
                save_summary(res1c, os.path.join(output_dir, "eq1_{0}.csv".format(confed)))
            except Exception:
                pass

            try:
                res2c = fit_fe_ols(panel_sub, dep, base + macro)
                save_summary(res2c, os.path.join(output_dir, "eq2_{0}.csv".format(confed)))
            except Exception:
                pass

            # IV is typically reported for full sample and UEFA
            if confed.upper() == "UEFA":
                try:
                    res3c = fit_fe_iv(subset, dep, base + macro, club, instr, args.entity, args.time)
                    save_summary(res3c, os.path.join(output_dir, "eq3_{0}.csv".format(confed)))
                except Exception:
                    pass


if __name__ == "__main__":
    main()
