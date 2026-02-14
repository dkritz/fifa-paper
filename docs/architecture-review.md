# Architecture Review

This document summarizes the current state and recommendations for project
architecture docs based on the repository's structure and contents.

## Docs reviewed
- README.md (project goal, quick start, data inputs, expected outputs, dev checklist)
- replication-plan.md (methodical plan, assumptions, step-by-step tasks, priority order)
- docs/data-dictionary.md ✅ (completed with actual sources and transformations)
- docs/data-pipeline.md ✅ (created with full ETL documentation)
- docs/notebook-spec.md (notebook cell outline, constraints)
- docs/research-questions.md (original paper questions + post-publication prediction questions)
- scripts/build_panel.py (data pipeline: ETL from raw sources to panel.csv)
- notebooks/replication_status.ipynb (synthetic data)
- notebooks/replication_actual_data.ipynb ✅ (created for actual data)
- .gitignore (ignore rules)

## What works well ✅
- Clear project goal and entry point (README + quick start, exact CLI command).
- Expected outputs are explicitly listed with filenames, matching the script's actual behavior.
- Replication plan is thorough, methodical, and shows awareness of Stata defaults.
- Priority order for devs is explicit in both README and replication-plan.
- Notebook spec is actionable (cell-by-cell outline) and aligned to repo code.
- **Two functional notebooks**: synthetic data (`replication_status.ipynb`) and actual data (`replication_actual_data.ipynb`).
- Research questions connect original work to modern predictive questions.
- **Complete data documentation**: data dictionary filled with actual sources, transformations, and WDI series codes.
- **Full data pipeline documentation**: ETL workflow documented with source details, merge logic, and quality controls.
- Data pipeline (`scripts/build_panel.py`) implements complete ETL: country name remapping (25 mappings), WDI code translation, multi-source merging with fallback logic.
- Notebook-script integration is implemented: notebook imports from `scripts/replicate_stata.py` with minimal fallback copies.
- README updated to reference both notebooks and all documentation.

## Gaps / improvements

### Remaining
- Environment reproducibility
  - requirements.txt exists but is unpinned; no lockfile or pyproject.toml.
  - The plan mentions pinning but doesn't present a concrete mechanism.
  - Minimum Python version only in README script header and plan, not in a file.
- Output validation criteria
  - No description of acceptable coefficient/SE drift tolerances for "faithful" replication.
- Stata comparison
  - No coefficient-by-coefficient comparison to original paper results.
  - No documentation of numerical differences (Stata 8/9 vs Python linearmodels).
  - Econometric report and data update plan documented in docs/econometric-report.md

### Completed ✅
- ~~Data dictionary completion~~ - Filled with actual sources, WDI series codes, transformations
- ~~Data provenance documentation~~ - Documented in data-pipeline.md (country mappings, quality decisions, fallback logic)
- ~~Second notebook~~ - Created replication_actual_data.ipynb for actual data
- ~~Notebook-script contract~~ - Already implemented and documented
- ~~Repository hygiene~~ - .gitignore is comprehensive

## Recommendations (architectural)

### 1. Add a reproducibility checklist
- Python version pin, requirements lock, environment verification command.
- Document how to rebuild the venv from scratch.

### 2. Define replication tolerances
- In replication-plan.md, add a section on coefficient/SE precision and handling of minor numerical drift when comparing to Stata.

### 3. Create coefficient comparison framework
- Build comparison tables between Python results and original paper.
- Document acceptable tolerances for coefficient drift.
- Add validation tests for key regression outputs.

### 4. Add CI/CD foundation
- Even if not implemented, note in replication-plan.md that a future CI step could run the notebook/script on synthetic data on PRs.
- Consider GitHub Actions workflow for running notebooks.

## Completed work ✅
- ~~Complete data dictionary~~ - Filled with actual sources, WDI series codes, transformations, and variable definitions
- ~~Document data pipeline provenance~~ - Created data-pipeline.md with complete ETL documentation including country mappings and quality decisions
- ~~Create actual data notebook~~ - Built replication_actual_data.ipynb for running on real panel data
- ~~Verify notebook–script contract~~ - Confirmed and documented in README
- ~~Update README~~ - Added references to both notebooks and all documentation

## Next steps
1. **Reproducibility**: Draft reproducibility checklist (Python version, lockfile)
2. **Validation**: Add coefficient tolerances section to replication-plan.md
3. **Stata comparison**: Create comparison tables between Python and original paper results
4. **Testing**: Add validation tests for regression outputs
5. **CI/CD**: Add CI stub note in replication-plan.md
