# Data Dictionary

This file documents the construction of `data/analysis/panel.csv` used by the
replication script. Fill in each field before running the final replication.

## Dataset overview
- Source file: `data/analysis/panel.csv`
- Panel index: `country`, `year`
- Frequency: annual
- Coverage: <years>, <countries>
- Confederations: <list of confed codes/names>
- Notes: <filters, exclusions, or sample restrictions>

## Variable definitions
Use the table below to document each variable's source, units, and any
transformations. Add rows as needed.

| Variable | Description | Unit/Scale | Source | Transformations/Construction | Notes |
| --- | --- | --- | --- | --- | --- |
| country | Country identifier | <text or code> | <source> | <none> | <ISO code or name> |
| year | Calendar year | year | <source> | <none> | <range> |
| confed | Confederation | <text or code> | <source> | <none> | <mapping> |
| fifa_points | FIFA ranking points | <points> | <source> | <none> | <as of date> |
| gdp_pc | GDP per capita | <currency> | <source> | <deflator, base year> | <PPP or nominal> |
| gdp_pc_sq | GDP per capita squared | <currency^2> | <derived> | gdp_pc^2 | <calc details> |
| pop | Population | <people> | <source> | <none> | <mid-year?> |
| pop_sq | Population squared | <people^2> | <derived> | pop^2 | <calc details> |
| trade | Trade openness | <share or percent> | <source> | <definition> | <imports+exports?> |
| infl | Inflation | <percent> | <source> | <definition> | <CPI?> |
| oil | Oil exporter/resource measure | <unit> | <source> | <definition> | <binary?> |
| leb | Life expectancy at birth | <years> | <source> | <none> | <sex?> |
| club | Domestic club strength | <index> | <source> | <construction> | <definition> |
| urbpop | Urban population share | <share or percent> | <source> | <definition> | <measurement> |
| urbpop_sq | Urban population share squared | <share^2> | <derived> | urbpop^2 | <calc details> |

## Construction notes
- Record any imputations, interpolations, or forward/backward fills.
- Document any country re-codings or merges.
- Note missing data handling rules used before producing the panel.
