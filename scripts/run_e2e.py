"""Run end-to-end replication and write a short interpretation report.

Builds the panel (if missing), estimates equations (1)-(3) using the
actual-data specification in the notebook, saves CSV summaries, and
emits a concise interpretation to stdout and results/interpretation.md.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

import pandas as pd
from linearmodels.iv import IV2SLS
from linearmodels.panel import PanelOLS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        default="data/analysis/panel.csv",
        help="Path to the prepared panel dataset.",
    )
    parser.add_argument(
        "--output",
        default="results",
        help="Output directory for CSV summaries and interpretation.",
    )
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="Write results/interpretation.md.",
    )
    return parser.parse_args()


def build_panel_if_missing(data_path: Path) -> None:
    if data_path.exists():
        return
    repo_root = Path(__file__).resolve().parent.parent
    subprocess.run(["python3", "scripts/build_panel.py"], cwd=repo_root, check=True)


def fit_fe_ols(panel: pd.DataFrame, dep: str, exog: list[str]):
    y = panel[dep]
    x = panel[exog]
    model = PanelOLS(
        y,
        x,
        entity_effects=True,
        time_effects=False,
        check_rank=False,
        drop_absorbed=True,
    )
    return model.fit(cov_type="clustered", cluster_entity=True, debiased=True)


def demean_by_entity(df: pd.DataFrame, cols: list[str], entity: str) -> pd.DataFrame:
    out = df.copy()
    for col in cols:
        ent_mean = out.groupby(entity)[col].transform("mean")
        out[col] = out[col] - ent_mean
    return out


def fit_fe_iv(
    df: pd.DataFrame,
    dep: str,
    exog: list[str],
    endog: str,
    instr: list[str],
    entity: str,
    time: str,
):
    cols = [dep] + exog + [endog] + instr + [entity, time]
    work = pd.DataFrame(df[cols].dropna().copy())
    work = demean_by_entity(work, [dep] + exog + [endog] + instr, entity)
    y = work[dep]
    x = work[exog]
    endog_v = work[endog]
    z = work[instr]
    model = IV2SLS(y, x, endog_v, z)
    return model.fit(cov_type="clustered", clusters=work[entity], debiased=True)


def save_summary(res, out_path: Path) -> None:
    table = res.summary.tables[1].as_csv()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(table)


def _coef_line(res, label_map: dict[str, str]) -> list[str]:
    lines = []
    for key, label in label_map.items():
        if key not in res.params.index:
            continue
        val = res.params[key]
        pval = res.pvalues[key]
        sign = "positive" if val > 0 else "negative" if val < 0 else "zero"
        sig = "significant" if pval < 0.05 else "not significant"
        lines.append(f"- {label}: {sign} ({sig}, p={pval:.3f})")
    return lines


def interpret_model(name: str, res, label_map: dict[str, str]) -> list[str]:
    entities = None
    if hasattr(res, "entity_info"):
        try:
            entities = int(res.entity_info["total"])
        except Exception:
            entities = None
    if entities is not None:
        lines = [f"**{name}**", f"- N={res.nobs}, entities={entities}"]
    else:
        lines = [f"**{name}**", f"- N={res.nobs}"]
    if hasattr(res, "rsquared") and res.rsquared is not None:
        r2 = res.rsquared
        r2_note = "negative" if r2 < 0 else "positive"
        lines.append(f"- R-squared: {r2:.4f} ({r2_note})")
    lines.extend(_coef_line(res, label_map))
    return lines


def _iv_diagnostics(res) -> list[str]:
    lines: list[str] = []
    first_stage = getattr(res, "first_stage", None)
    if first_stage is None:
        return lines
    summary = first_stage.summary
    if summary is None:
        return lines
    table = summary.tables[0].data
    pfs = None
    pfs_p = None
    for row in table:
        if len(row) < 2:
            continue
        key = str(row[0]).strip().lower()
        if key.startswith("partial f-statistic"):
            pfs = row[1]
        if key.startswith("p-value") and "partial f" in key:
            pfs_p = row[1]
    if pfs is not None:
        if pfs_p is not None:
            lines.append(f"- First-stage partial F: {pfs} (p={pfs_p})")
        else:
            lines.append(f"- First-stage partial F: {pfs}")
    pr2 = None
    for row in table:
        if len(row) < 2:
            continue
        key = str(row[0]).strip().lower()
        if key.startswith("partial r-squared"):
            pr2 = row[1]
    if pr2 is not None:
        lines.append(f"- First-stage partial R-squared: {pr2}")
    return lines


def main() -> None:
    args = parse_args()
    data_path = Path(args.data)
    build_panel_if_missing(data_path)

    if not data_path.exists():
        raise FileNotFoundError(f"Panel data not found at {data_path}")

    df = pd.read_csv(data_path)
    df["gdp_pc_k"] = df["gdp_pc"] / 1000.0
    df["gdp_pc_k_sq"] = df["gdp_pc_k"] ** 2
    df["pop_m"] = df["pop"] / 1_000_000.0
    df["pop_m_sq"] = df["pop_m"] ** 2

    dep = "fifa_points"
    base = ["gdp_pc_k", "gdp_pc_k_sq", "pop_m", "pop_m_sq"]
    macro = ["trade", "infl", "oil", "leb"]
    club = "club"
    instr = ["urbpop", "urbpop_sq"]

    df = df.sort_values(["country", "year"])
    panel = df.set_index(["country", "year"])

    results_dir = Path(args.output)

    res1 = fit_fe_ols(panel, dep, base)
    save_summary(res1, results_dir / "eq1_full.csv")

    res2 = fit_fe_ols(panel, dep, base + macro)
    save_summary(res2, results_dir / "eq2_full.csv")

    res3 = None
    try:
        res3 = fit_fe_iv(df, dep, base + macro, club, instr, "country", "year")
        save_summary(res3, results_dir / "eq3_full.csv")
    except Exception as exc:
        print(f"Equation (3) failed: {exc}")

    report = []
    report.append("## End-to-End Replication Summary")
    report.append("")

    report.extend(
        interpret_model(
            "Equation (1)",
            res1,
            {
                "gdp_pc_k": "GDP per capita (thousands)",
                "gdp_pc_k_sq": "GDP per capita squared",
                "pop_m": "Population (millions)",
                "pop_m_sq": "Population squared",
            },
        )
    )
    report.append("")

    report.extend(
        interpret_model(
            "Equation (2)",
            res2,
            {
                "gdp_pc_k": "GDP per capita (thousands)",
                "gdp_pc_k_sq": "GDP per capita squared",
                "pop_m": "Population (millions)",
                "pop_m_sq": "Population squared",
                "trade": "Trade (% GDP)",
                "infl": "Inflation",
                "oil": "Oil rents (% GDP)",
                "leb": "Life expectancy",
            },
        )
    )
    report.append("")

    if res3 is not None:
        report.extend(
            interpret_model(
                "Equation (3)",
                res3,
                {
                    "gdp_pc_k": "GDP per capita (thousands)",
                    "gdp_pc_k_sq": "GDP per capita squared",
                    "pop_m": "Population (millions)",
                    "pop_m_sq": "Population squared",
                    "trade": "Trade (% GDP)",
                    "infl": "Inflation",
                    "oil": "Oil rents (% GDP)",
                    "leb": "Life expectancy",
                    "club": "Club strength (endogenous)",
                },
            )
        )
        report.extend(_iv_diagnostics(res3))
    else:
        report.append("**Equation (3)**")
        report.append("- Failed to estimate; see stdout for error.")

    print("\n".join(report))
    if args.write_report:
        results_dir.mkdir(parents=True, exist_ok=True)
        (results_dir / "interpretation.md").write_text("\n".join(report))


if __name__ == "__main__":
    main()
