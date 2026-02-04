# FIFA Paper Replication

This repo contains the published paper, a LaTeX reproduction, and a Python
replication script for the econometric analysis.

## Project goal
Replicate the paper's econometric results in Python with Stata 8/9-compatible
defaults (fixed-effects OLS for equations (1)-(2), fixed-effects IV/2SLS for
equation (3)), and write comparable result tables to `results/`.

## Notebooks

Two notebooks are provided for replication:

### 1. `notebooks/replication_status.ipynb` (Synthetic Data)
Documents the replication status using **synthetic data** to demonstrate the model
pipeline without requiring the full dataset. Useful for testing and development.

**Contents**:
- Project goal and replication status summary
- Synthetic panel data generator (schema matches `data/analysis/panel.csv`)
- Equations (1)-(3) on synthetic data using the same code paths as `scripts/replicate_stata.py`
- Outputs saved to local `results/` subfolder

### 2. `notebooks/replication_actual_data.ipynb` (Actual Data)
Runs the full replication using the **actual** panel dataset built from FIFA
rankings, club rankings, and World Development Indicators (1993-2010).

**Contents**:
- Load and validate the actual panel dataset
- Run Equations (1)-(3) on real data
- Confederation-level analysis
- Export results to CSV
- Summary statistics and data quality checks

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

The panel dataset is built from three raw sources. You can either:

**Option A: Build from raw sources**
```bash
python3 scripts/build_panel.py
```
This creates `data/analysis/panel.csv` by merging:
- FIFA World Rankings (1993-2010)
- FIFA Club Rankings (2000-2010)
- World Bank WDI data (1993-2010)

See [docs/data-pipeline.md](docs/data-pipeline.md) for complete documentation.

**Option B: Provide your own panel**
Create `data/analysis/panel.csv` with these columns:
- `country`, `year`, `confed`
- `fifa_points`
- `gdp_pc`, `gdp_pc_sq`
- `pop`, `pop_sq`
- `trade`, `infl`, `oil`, `leb`
- `club`
- `urbpop`, `urbpop_sq`

### Data documentation
- [docs/data-dictionary.md](docs/data-dictionary.md): Variable definitions, sources, and transformations
- [docs/data-pipeline.md](docs/data-pipeline.md): Complete ETL pipeline documentation
- Country name mappings, WDI series codes, and construction rules are fully documented

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
- [x] Build synthetic data notebook at `notebooks/replication_status.ipynb`
- [x] Build actual data notebook at `notebooks/replication_actual_data.ipynb`
- [x] Complete `docs/data-dictionary.md` with variable sources, units, and construction rules
- [x] Create `docs/data-pipeline.md` documenting the ETL workflow
- [ ] Confirm the exact Stata version (8 vs 9) used in the original analysis
- [ ] Run validation comparing Python results to original paper/Stata output
- [ ] Add coefficient comparison tables
- [ ] Document any discrepancies and their causes

## Docs
- `docs/data-dictionary.md` - Variable definitions and sources
- `docs/data-pipeline.md` - ETL pipeline documentation
- `docs/notebook-spec.md` - Notebook structure specification
- `docs/research-questions.md` - Original and post-publication research questions
- `docs/architecture-review.md` - Project architecture assessment
