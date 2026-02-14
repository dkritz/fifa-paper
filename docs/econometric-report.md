# Econometric Report and Data Plan

This document summarizes the current Python replication results, diagnostics, improvement ideas, and a plan to obtain updated data. It also includes a task list for obtaining the paper’s published econometric tables.

## Summary of Current Results (Python)

Note: the end-to-end runner and actual-data notebook scale GDP per capita (thousands) and population (millions) for interpretability. Coefficients from those runs are rescaled relative to `scripts/replicate_stata.py`, which uses raw units.

### Equation (1): Baseline FE
- GDP per capita and population have positive linear terms and negative squared terms (inverted-U), with strong statistical significance.
- Interpretation: wealth and population increase FIFA points up to a point; marginal returns decline.

### Equation (2): FE + macro/resource controls
- The inverted-U patterns for GDP and population remain robust.
- Trade openness and life expectancy are positive and significant.
- Inflation and oil rents are not significant in the full sample.
- Sample size shrinks due to missing macro data, which may affect comparability.

### Equation (3): FE IV with club strength
- The IV estimates are imprecise; the CLUB coefficient is not significant.
- First-stage diagnostics indicate extremely weak instruments:
  - Partial F-statistic ≈ 0.42
  - Partial R-squared ≈ 0.0003
- Interpretation: the UrbPOP instruments do not explain CLUB once fixed effects are applied, so Eq(3) is weakly identified in this dataset.

## Ideas to Improve Model Results

1. Strengthen identification for CLUB
   - Replace rank-based CLUB with a points-based or continuous metric.
   - Use alternative instruments (e.g., historical club success, stadium capacity, attendance, media revenue, league infrastructure proxies).
   - Use lagged instruments (e.g., urbpop lagged 5–10 years) to reduce simultaneity.

2. Address missing data and sample selection
   - Run Eq(2) and Eq(3) on a consistent sample to improve comparability.
   - Consider multiple imputation for macro variables with moderate missingness.

3. Specification robustness
   - Test log specifications for GDP per capita and population.
   - Consider interactions (e.g., GDP × population, trade × confed).
   - Add time fixed effects as a robustness check where feasible.

4. Confederation-specific estimation
   - Re-run Eq(3) focused on UEFA where club data quality is strongest.
   - Compare regional first-stage strength and IV stability.

## Plan for Newer / Updated / More-Complete Data

1. FIFA performance
   - Extend FIFA points beyond 2010 using FIFA archives or public datasets.
   - Verify methodological consistency over time (rank points vs ranking method changes).

2. Club strength
   - Use UEFA coefficients for Europe and confederation coefficients for other regions.
   - Explore public club rating sources (e.g., FiveThirtyEight, World Football Elo).
   - Consider constructing a club success index from continental competition results.

3. Macro controls (WDI)
   - Refresh WDI series through the current year.
   - Validate units (percent vs fraction) and apply consistent scaling.

4. Instrument set
   - Gather urbanization data from earlier decades for lagged instruments.
   - Add city-level proxies for club infrastructure (stadium capacity, attendance).

5. Reproducible pipeline updates
   - Add scripted downloads and checksums for new sources.
   - Document new sources and transformations in `docs/data-pipeline.md`.

## Task List for Paper Results (Human-Provided)

Please supply any of the following to enable coefficient-by-coefficient comparison:

1. Published tables (Table 2, Table 3, Table 4) with coefficients and standard errors.
2. Original paper PDF or Docx that includes the numeric tables.
3. Stata output files from `xtreg` / `xtivreg2` runs.
4. Any appendix tables or robustness tables with exact estimates.

Once provided, a side-by-side comparison can be produced against the Python results.
