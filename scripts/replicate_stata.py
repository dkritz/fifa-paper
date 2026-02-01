"""Replicate Stata 8/9 panel regressions in Python.

Assumptions:
- Data are already transformed and merged into a single panel file.
- Quadratic terms (GDP2, POP2, UrbPOP2) are precomputed.
- Country and year identifiers are present.

Outputs are printed to stdout and optionally saved to CSV.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS


def parse_args() -> argparse.Namespace:
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


def two_way_demean(df: pd.DataFrame, cols: list[str], entity: str, time: str) -> pd.DataFrame:
    """Two-way demean columns by entity and time (within estimator)."""
    out = df.copy()
    for col in cols:
        overall = out[col].mean()
        ent_mean = out.groupby(entity)[col].transform("mean")
        time_mean = out.groupby(time)[col].transform("mean")
        out[col] = out[col] - ent_mean - time_mean + overall
    return out


def fit_fe_ols(panel: pd.DataFrame, dep: str, exog: list[str]) -> PanelOLS:
    y = panel[dep]
    X = panel[exog]
    model = PanelOLS(y, X, entity_effects=True, time_effects=True)
    res = model.fit(cov_type="clustered", cluster_entity=True, debiased=True)
    return res


def fit_fe_iv(
    df: pd.DataFrame,
    dep: str,
    exog: list[str],
    endog: str,
    instr: list[str],
    entity: str,
    time: str,
) -> IV2SLS:
    cols = [dep] + exog + [endog] + instr + [entity, time]
    work = df[cols].dropna().copy()
    work = two_way_demean(work, [dep] + exog + [endog] + instr, entity, time)

    y = work[dep]
    X = work[exog]
    endog_v = work[endog]
    Z = work[instr]

    model = IV2SLS(y, X, endog_v, Z)
    res = model.fit(cov_type="clustered", clusters=work[entity], debiased=True)
    return res


def save_summary(res, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    table = res.summary.tables[1].as_csv()
    out_path.write_text(table)


def main() -> None:
    args = parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    df = pd.read_csv(data_path)

    dep = "fifa_points"
    base = ["gdp_pc", "gdp_pc_sq", "pop", "pop_sq"]
    macro = ["trade", "infl", "oil", "leb"]
    club = "club"
    instr = ["urbpop", "urbpop_sq"]

    required = [args.entity, args.time, dep] + base + macro + [club] + instr
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.sort_values([args.entity, args.time])
    panel = df.set_index([args.entity, args.time])

    output_dir = Path(args.output)

    # Equation (1)
    res1 = fit_fe_ols(panel, dep, base)
    print("\nEquation (1) - Full sample")
    print(res1.summary)
    save_summary(res1, output_dir / "eq1_full.csv")

    # Equation (2)
    res2 = fit_fe_ols(panel, dep, base + macro)
    print("\nEquation (2) - Full sample")
    print(res2.summary)
    save_summary(res2, output_dir / "eq2_full.csv")

    # Equation (3) - IV with fixed effects
    res3 = fit_fe_iv(df, dep, base + macro, club, instr, args.entity, args.time)
    print("\nEquation (3) - Full sample")
    print(res3.summary)
    save_summary(res3, output_dir / "eq3_full.csv")

    # By confederation
    if args.confed in df.columns:
        for confed in sorted(df[args.confed].dropna().unique()):
            subset = df[df[args.confed] == confed]
            if subset.empty:
                continue
            panel_sub = subset.set_index([args.entity, args.time])

            try:
                res1c = fit_fe_ols(panel_sub, dep, base)
                save_summary(res1c, output_dir / f"eq1_{confed}.csv")
            except Exception:
                pass

            try:
                res2c = fit_fe_ols(panel_sub, dep, base + macro)
                save_summary(res2c, output_dir / f"eq2_{confed}.csv")
            except Exception:
                pass

            # IV is typically reported for full sample and UEFA
            if confed.upper() == "UEFA":
                try:
                    res3c = fit_fe_iv(subset, dep, base + macro, club, instr, args.entity, args.time)
                    save_summary(res3c, output_dir / f"eq3_{confed}.csv")
                except Exception:
                    pass


if __name__ == "__main__":
    main()
