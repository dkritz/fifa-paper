# FIFA Paper Replication

This repo contains the published paper, a LaTeX reproduction, and a Python
replication script for the econometric analysis.

## Project goal
Replicate the paper's econometric results in Python with Stata 8/9-compatible
defaults (fixed-effects OLS for equations (1)-(2), fixed-effects IV/2SLS for
equation (3)), and write comparable result tables to `results/`.

## Notebook (new feature)
Create a repository-visible Python notebook that documents the current
replication status and runs on synthetic data. The notebook should live at
`notebooks/replication_status.ipynb` so it renders on GitHub.

Notebook contents (initial scope):
1) Project goal and replication status summary.
2) Synthetic panel data generator (schema matches `data/analysis/panel.csv`).
3) Run equations (1)-(3) on synthetic data using the same code paths as
   `scripts/replicate_stata.py`.
4) Write outputs to a local `results/` subfolder in the notebook runtime.
5) Include placeholders/sections for future: real data ingest, Stata comparison,
   table export formatting, and validation checks.

## Quick start
1) Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Prepare a panel dataset (CSV) with these columns:
- `country`, `year`, `confed`
- `fifa_points`
- `gdp_pc`, `gdp_pc_sq`
- `pop`, `pop_sq`
- `trade`, `infl`, `oil`, `leb`
- `club`
- `urbpop`, `urbpop_sq`

3) Run the replication script:

```bash
python3 scripts/replicate_stata.py --data data/analysis/panel.csv
```

Results will be written to the `results/` folder as CSV summaries.

## Data inputs
Provide a panel dataset at `data/analysis/panel.csv` with these columns:
- `country`, `year`, `confed`
- `fifa_points`
- `gdp_pc`, `gdp_pc_sq`
- `pop`, `pop_sq`
- `trade`, `infl`, `oil`, `leb`
- `club`
- `urbpop`, `urbpop_sq`

### Data dictionary (required)
This repo assumes you already have the panel dataset. Please document the
following in `docs/data-dictionary.md` (template included):
- Source and coverage for each variable (years, countries, updates).
- Units and transformations (levels, logs, shares, deflators).
- Construction details for derived variables (e.g., `*_sq`, `club`).
- Any filters or exclusions applied before creating the panel.

## Expected outputs
The replication script writes CSV summaries to `results/` with the following
baseline files:
- `eq1_full.csv`: Equation (1), FE OLS, clustered SEs.
- `eq2_full.csv`: Equation (2), FE OLS with macro/resource controls, clustered SEs.
- `eq3_full.csv`: Equation (3), FE IV/2SLS with `club` instrumented by `urbpop` and `urbpop_sq`.

If `confed` is present, the script also writes confederation splits as
`eq1_{CONFED}.csv` and `eq2_{CONFED}.csv`. For IV, it additionally writes
`eq3_UEFA.csv` when UEFA is present.

## Notes
- Python 3.8+ is required for the replication script.
- The original Stata do files are missing, so the replication relies on the
  specification in the paper and Stata 8/9 defaults.
- Equation (3) uses a fixed-effects IV approach with urban population as the
  instrument for `club`.

## Dev checklist
1) Build the initial notebook at `notebooks/replication_status.ipynb` per the
   Notebook section above.
2) Complete `docs/data-dictionary.md` with variable sources, units, and construction rules.
3) Confirm the exact Stata version (8 vs 9) used in the original analysis.
4) Run the replication script and verify outputs appear in `results/`.

## Docs
- `docs/data-dictionary.md`
- `docs/notebook-spec.md`
- `docs/research-questions.md`
