# Replication Status Notebook Spec

This document defines the required structure and content for the GitHub-viewable
notebook at `notebooks/replication_status.ipynb`.

## Goals
- Provide a lightweight, reproducible overview of current replication status.
- Demonstrate the model pipeline on synthetic data that matches the expected
  panel schema.
- Offer clear placeholders for future work (real data, Stata comparison).

## Notebook structure (cell outline)
1) Title + project goal (markdown)
   - One-paragraph summary of the paper replication objective.
   - Link to `README.md` and `replication-plan.md`.

2) Environment + imports (code)
   - Python version print.
   - Imports: pandas, numpy, linearmodels, statsmodels (if needed), pathlib.

3) Synthetic data generation (code)
   - Create a panel with `country`, `year`, `confed`.
   - Generate variables: `fifa_points`, `gdp_pc`, `gdp_pc_sq`, `pop`, `pop_sq`,
     `trade`, `infl`, `oil`, `leb`, `club`, `urbpop`, `urbpop_sq`.
   - Include a deterministic seed.
   - Ensure columns match `data/analysis/panel.csv` schema.

4) Synthetic data snapshot (markdown + code)
   - Show `df.head()` and basic shape.
   - Brief note that this is illustrative only.

5) Load model runner helpers (code)
   - Option A: import from `scripts/replicate_stata.py` (preferred).
   - Option B: local minimal copies of `fit_fe_ols` and `fit_fe_iv` if import
     fails in notebook context.

6) Run Equation (1) (code)
   - FE OLS on base covariates.
   - Show `res.summary`.

7) Run Equation (2) (code)
   - FE OLS on base + macro.
   - Show `res.summary`.

8) Run Equation (3) (code)
   - FE IV/2SLS with `club` instrumented by `urbpop`, `urbpop_sq`.
   - Show `res.summary`.

9) Write outputs (code)
   - Save CSV summaries to `results/` in the notebook runtime.
   - Note: synthetic-only output.

10) Replication status (markdown)
   - Checklist: synthetic run, real data ingest, Stata comparison, output format,
     validation.

11) Next steps (markdown)
   - Link to `docs/data-dictionary.md` and `replication-plan.md`.
   - Call out open questions (Stata version, data provenance).

## Notebook constraints
- Keep it short and easy to run.
- No non-deterministic outputs (always set a seed).
- Avoid heavy formatting or large plots unless needed.
