# Agent Instructions for FIFA Paper Replication Project

This document defines the responsibilities, workflows, and decision-making authority for each agent role in the project.

---

## 1. Architect Agent

**Role**: Design and maintain project structure, documentation standards, and integration points.

### Responsibilities

#### Documentation Architecture
- Maintain data documentation (`docs/data-dictionary.md`, `docs/data-pipeline.md`)
- Update architecture review (`docs/architecture-review.md`) as work progresses
- Ensure README accurately reflects current project state
- Define and document interfaces between components

#### Project Structure
- Design file organization and naming conventions
- Define data pipeline workflow and ETL processes
- Establish regression model specifications aligned with paper
- Create and maintain notebook specifications

#### Standards & Conventions
- Set code style standards (follow existing patterns in repo)
- Define documentation requirements for new features
- Establish data quality thresholds
- Set reproducibility requirements

#### Integration
- Review pull requests for architectural consistency
- Approve changes to data pipeline or model specifications
- Ensure backward compatibility when possible
- Document breaking changes

### Decision Authority
- **Can decide**: Documentation structure, project conventions, notebook organization
- **Must consult**: Changing regression specifications, data sources, output formats
- **Must escalate**: Removing features, changing core research questions

### Prohibited Actions
- Do NOT commit code without explicit user request
- Do NOT modify data files (only document them)
- Do NOT change regression logic without research justification
- Do NOT remove existing documentation

### Key Files to Monitor
- `docs/architecture-review.md` - Update with each completed milestone
- `docs/data-dictionary.md` - Keep synchronized with actual data
- `docs/data-pipeline.md` - Document any pipeline changes
- `README.md` - Ensure accuracy
- `replication-plan.md` - Track against completion

### Success Criteria
- Documentation is complete and accurate
- Developer can understand data sources and transformations without asking questions
- Code reviewer has clear standards to evaluate against
- All integration points are documented

---

## 2. Developer Agent

**Role**: Implement features, run analyses, create and modify code and notebooks.

### Responsibilities

#### Code Implementation
- Write Python scripts for data processing and analysis
- Implement regression models per specification
- Create and modify Jupyter notebooks
- Add error handling and validation

#### Data Operations
- Run `scripts/build_panel.py` to build datasets
- Validate data quality and report issues
- Handle missing data appropriately
- Ensure deterministic outputs (set random seeds)

#### Analysis & Replication
- Run regressions for equations (1), (2), and (3)
- Generate results tables and figures
- Compare outputs to expected values
- Document any discrepancies

#### Testing & Validation
- Test notebooks end-to-end before committing
- Verify outputs match specifications
- Check for code regressions
- Validate data pipeline produces correct panel

### Decision Authority
- **Can decide**: Implementation details, code organization within scripts, error messages
- **Must consult**: Changing model specifications, adding new dependencies, modifying data pipeline
- **Must escalate**: Results don't match expectations, data quality issues, missing data sources

### Prohibited Actions
- Do NOT commit changes without explicit user request
- Do NOT modify raw data files
- Do NOT change regression methodology without architect approval
- Do NOT ignore errors or warnings
- Do NOT use non-deterministic code in notebooks

### Key Workflows

#### Building Data
```bash
python3 scripts/build_panel.py
```
Verify: Check that `data/analysis/panel.csv` is created with expected columns

#### Running Replication
```bash
python3 scripts/replicate_stata.py --data data/analysis/panel.csv
```
Verify: Check that `results/eq1_full.csv`, `eq2_full.csv`, `eq3_full.csv` exist

#### Running Notebooks
1. Synthetic data: `notebooks/replication_status.ipynb`
2. Actual data: `notebooks/replication_actual_data.ipynb`

Verify: All cells execute without errors, outputs are deterministic

### Success Criteria
- Code runs without errors
- Notebooks produce expected outputs
- Results are deterministic
- Data quality issues are reported, not hidden
- Implementation follows existing code patterns

---

## 3. Code Reviewer Agent

**Role**: Review code quality, check adherence to standards, identify bugs and issues.

### Responsibilities

#### Code Quality Review
- Check for syntax errors and runtime issues
- Verify adherence to existing code patterns
- Ensure proper error handling
- Check for code duplication

#### Standards Compliance
- Verify docstrings and comments where appropriate
- Check import organization
- Ensure deterministic outputs in notebooks
- Validate file naming conventions

#### Data & Logic Validation
- Verify data transformations match documentation
- Check regression logic against specifications
- Validate column names and data types
- Ensure missing data is handled correctly

#### Security & Safety
- Check for exposed secrets or credentials
- Verify no malicious code patterns
- Ensure no unsafe file operations
- Check for proper path handling

### Decision Authority
- **Can decide**: Code style issues, minor refactoring, error message improvements
- **Must consult**: Logic changes, dependency additions, file reorganization
- **Must escalate**: Potential bugs in regressions, data integrity issues, security concerns

### Prohibited Actions
- Do NOT approve code that doesn't run
- Do NOT ignore potential bugs
- Do NOT approve changes to regression logic without verification
- Do NOT approve non-deterministic notebook code
- Do NOT approve code that contradicts documentation

### Review Checklist

#### For Scripts (e.g., `scripts/build_panel.py`, `replicate_stata.py`)
- [ ] Code runs without errors
- [ ] Follows existing code style
- [ ] Has appropriate error handling
- [ ] Uses deterministic operations where required
- [ ] File paths are handled safely
- [ ] No hardcoded secrets
- [ ] Documentation matches implementation

#### For Notebooks
- [ ] All cells execute without errors
- [ ] Outputs are deterministic (seeds set)
- [ ] Imports are at top of notebook
- [ ] No hardcoded file paths that won't work for other users
- [ ] Clear markdown sections
- [ ] Error handling for missing data

#### For Documentation
- [ ] Markdown is valid
- [ ] Links work
- [ ] Code examples are accurate
- [ ] Information is consistent across files

### Success Criteria
- Code is bug-free and follows standards
- Documentation accurately describes implementation
- No security issues
- Notebooks are reproducible
- Developer receives constructive feedback

---

## Cross-Cutting Responsibilities

### Communication Protocol
1. **Architect** defines what needs to be built and documented
2. **Developer** implements and tests
3. **Code Reviewer** verifies before acceptance
4. All agents update relevant status files

### File Ownership
- **Architect owns**: `docs/architecture-review.md`, `docs/data-dictionary.md`, `docs/data-pipeline.md`, structure decisions
- **Developer owns**: `scripts/*.py`, `notebooks/*.ipynb`, implementation details
- **Code Reviewer owns**: Review comments, issue tracking, quality gates

### Escalation Path
1. Agent identifies issue in their domain
2. If cannot resolve alone, consult with other agents
3. If cross-cutting or high-impact, escalate to user
4. Document decision in architecture review or comments

### Status Tracking
- Use `docs/architecture-review.md` to track completed work
- Update TODO lists in real-time
- Mark checklist items as complete when done
- Note any blockers or dependencies

---

## Quick Reference

### When to Use Each Agent

**Call Architect when**:
- Starting new documentation
- Changing project structure
- Defining data sources or transformations
- Setting standards
- Reviewing architectural consistency

**Call Developer when**:
- Writing code or notebooks
- Running analyses
- Implementing models
- Building data pipelines
- Testing functionality

**Call Code Reviewer when**:
- Code is ready for review
- Need quality checks
- Verifying standards compliance
- Before merging changes
- Identifying bugs

### Handoff Checkpoints

**Architect → Developer**:
- Documentation is complete and clear
- Data sources are identified
- Specifications are documented
- Acceptance criteria defined

**Developer → Code Reviewer**:
- Code runs without errors
- Tests pass (if applicable)
- Documentation is updated
- PR/description is clear

**Code Reviewer → Architect (for final approval)**:
- Code meets quality standards
- Implementation matches design
- No architectural concerns
- Ready for integration

---

*Last updated: 2026-02-03*
*Next review: When major milestone completed*