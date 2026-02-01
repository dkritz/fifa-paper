# Stata to Python Replication Plan

## Goal
Recreate Stata results in Python as faithfully as possible before any refactoring.

## Plan
1) Collect and catalog inputs
- Identify all Stata do files, ado dependencies, raw data files, and intermediate outputs.
- Note exact Stata version used in the paper (affects defaults and numeric behavior).
- Confirm OS and file encodings (some Stata workflows assume Windows-style paths).

2) Build a dependency map
- Parse each do file’s flow: data import, cleaning, merges, derived variables, regressions, tables/figures.
- Record dataset lineage and intermediates.
- Identify Stata-specific behaviors needing explicit Python handling (for example, missing values, weights, robust SE defaults, factor variables, xtset/panel commands).

3) Create a deterministic Python environment
- Pin Python version and key libraries (pandas, numpy, statsmodels, linearmodels, scipy).
- Create a reproducible runner (scripts, not notebooks) mirroring Stata’s step order.

4) Translate Stata data steps
- Map use, merge, append, collapse, egen, reshape, bysort, tsset/xtset.
- Encode Stata missing values and categorical handling exactly.
- Preserve variable labels and value labels as metadata (optional but helpful).

5) Translate estimation blocks
- Map each model to statsmodels/linearmodels equivalents.
- Match Stata defaults: constant inclusion, degrees-of-freedom adjustments, cluster/robust variance, weights, and fixed effects.
- Ensure exact sample restrictions and if/in logic.

6) Recreate tables and figures
- Replicate esttab/estout or outreg outputs with Python (statsmodels summary2, stargazer, pandas formatting).
- For figures, match axis scales, bins, and normalization rules.

7) Validation checkpointing
- After each step, compare row counts, summary stats, and key variables to Stata outputs.
- For each regression, compare coefficients, SEs, and p-values against Stata to acceptable tolerances and document any drift.

8) Final verification
- Reproduce the exact paper tables and figures.
- Provide a differences log listing any unavoidable deviations and their causes.

## Inputs needed to tailor the conversion
1) Paths to the Stata files and data
2) Stata version used in the paper (or on those do files)
3) Any custom ado files and their locations
4) Rough dataset sizes (row counts or file sizes)
5) Preference on table and figure formatting: exact match or numeric equality only
