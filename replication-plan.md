# Stata to Python Replication Plan

## Goal
Recreate Stata results in Python as faithfully as possible before any refactoring.

## Econometric specification (from paper)
- Panel fixed-effects (country and time), annual data 1993–2010.
- Dependent variable: FIFA points.
- Equation (1): baseline wealth and population with quadratic terms.
  - FIFA = f(GDP, GDP^2, POP, POP^2)
- Equation (2): adds macro/resource controls.
  - FIFA = f(GDP, GDP^2, POP, POP^2, TRADE, INFL, OIL, LEB)
- Equation (3): adds domestic club strength (CLUB), treated as endogenous.
  - FIFA = f(GDP, GDP^2, POP, POP^2, TRADE, INFL, OIL, LEB, CLUB)
  - First stage: CLUB = g(GDP, GDP^2, POP, POP^2, TRADE, INFL, OIL, LEB, UrbPOP, UrbPOP^2)
  - Instrument: urban population share (UrbPOP) and squared term.
- Estimation: FE OLS with cluster-robust SE for (1) and (2); IV/2SLS with HAC/cluster-robust SE for (3), using xtivreg2.

## Constraints and assumptions
- Original Stata do files are not available; we must infer workflow from the paper and data files.
- Regressions were run in Stata 8 or 9 using xtivreg and xtivreg2 (panel IV estimators).
- Replication should prioritize matching Stata 8/9 defaults (e.g., FE handling, variance estimators, and small-sample adjustments).

## Scope clarification (no do files)
Because the original do files are missing, the plan below focuses on
reconstructing the workflow from the paper, available data, and Stata 8/9
defaults rather than translating an existing script.

## Plan
1) Collect and catalog inputs
- Identify raw data files, intermediate outputs (if any), and any custom ado dependencies used in related work.
- Note exact Stata version used in the paper (affects defaults and numeric behavior).
- Confirm OS and file encodings (some Stata workflows assume Windows-style paths).
- Fill out `docs/data-dictionary.md` with sources, units, and construction rules for each variable.

2) Stand up the replication status notebook
- Create `notebooks/replication_status.ipynb` and ensure it renders on GitHub.
- Add synthetic panel data generation matching the required schema.
- Run equations (1)-(3) against synthetic data using the same code paths as
  `scripts/replicate_stata.py`.
- Add placeholders for real data ingest, Stata comparison, and validation.

3) Build a dependency map
- Reconstruct the data flow: import, cleaning, merges, derived variables, regressions, tables/figures.
- Record dataset lineage and intermediates.
- Identify Stata-specific behaviors needing explicit Python handling (for example, missing values, weights, robust SE defaults, factor variables, xtset/panel commands).

4) Create a deterministic Python environment
- Pin Python version and key libraries (pandas, numpy, statsmodels, linearmodels, scipy).
- Create a reproducible runner (scripts, not notebooks) mirroring Stata’s step order.

5) Translate Stata data steps
- Map use, merge, append, collapse, egen, reshape, bysort, tsset/xtset.
- Encode Stata missing values and categorical handling exactly.
- Preserve variable labels and value labels as metadata (optional but helpful).

6) Translate estimation blocks
- Map each model to statsmodels/linearmodels equivalents.
- Match Stata defaults: constant inclusion, degrees-of-freedom adjustments, cluster/robust variance, weights, and fixed effects.
- Ensure exact sample restrictions and if/in logic.

7) Recreate tables and figures
- Replicate esttab/estout or outreg outputs with Python (statsmodels summary2, stargazer, pandas formatting).
- For figures, match axis scales, bins, and normalization rules.

8) Validation checkpointing
- After each step, compare row counts, summary stats, and key variables to Stata outputs.
- For each regression, compare coefficients, SEs, and p-values against Stata to acceptable tolerances and document any drift.

9) Final verification
- Reproduce the exact paper tables and figures.
- Provide a differences log listing any unavoidable deviations and their causes.

## Inputs needed to tailor the conversion
1) Paths to the Stata files and data
2) Stata version used in the paper (or on those do files)
3) Any custom ado files and their locations
4) Rough dataset sizes (row counts or file sizes)
5) Preference on table and figure formatting: exact match or numeric equality only

## Immediate next steps for devs (priority order)
1) Build the initial notebook at `notebooks/replication_status.ipynb` and ensure it runs end-to-end on synthetic data.
2) Complete `docs/data-dictionary.md` so variable definitions are unambiguous.
3) Confirm the exact Stata version (8 vs 9) used in the paper or related runs.
4) Run the replication script on the prepared panel and verify output files in `results/`.
