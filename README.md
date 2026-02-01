# FIFA Paper Replication

This repo contains the published paper, a LaTeX reproduction, and a Python
replication script for the econometric analysis.

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
python scripts/replicate_stata.py --data data/analysis/panel.csv
```

Results will be written to the `results/` folder as CSV summaries.

## Notes
- The original Stata do files are missing, so the replication relies on the
  specification in the paper and Stata 8/9 defaults.
- Equation (3) uses a fixed-effects IV approach with urban population as the
  instrument for `club`.
