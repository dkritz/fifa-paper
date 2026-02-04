# Data Dictionary

This file documents the construction of `data/analysis/panel.csv` used by the replication script.

## Dataset overview
- **Source file**: `data/analysis/panel.csv` (built from multiple raw sources)
- **Panel index**: `country`, `year`
- **Frequency**: annual
- **Coverage**: 1993–2010 (18 years)
- **Countries**: 150+ nations with FIFA rankings
- **Confederations**: UEFA, CAF, CONMEBOL, CONCACAF, AFC, OFC
- **Notes**: Filtered to countries with FIFA points data; Faroe Islands excluded due to missing WDI data

## Data Sources

### 1. FIFA Points Data
- **File**: `data/fifa_points/fifa_excel_long_93_10_sheet1.csv`
- **Source**: FIFA World Rankings (converted from Excel)
- **Coverage**: 1993–2010, all FIFA member nations
- **Key variables**: `fps` (FIFA points), `country`, `year`
- **Transformations**:
  - Year converted: original format (1-18) → calendar year (1993-2010)
  - Column renamed: `fps` → `fifa_points`
  - Country names remapped to match WDI naming conventions (see Country Mapping section)

### 2. Club Rankings Data
- **File**: `data/club_rankings/fifa_club_merge_2000_plus.csv`
- **Source**: FIFA club ranking data 2000–2013
- **Coverage**: 2000–2010 for replication (years 2000-2010)
- **Key variables**: `TEAM`, `CODE`, `CONF-Code`, `CLUB2000`–`CLUB2013`
- **Transformations**:
  - Reshaped from wide to long format
  - Confederation codes mapped: 1=UEFA, 2=CONMEBOL, 3=CONCACAF, 4=AFC, 5=CAF, 6=OFC
  - Club strength aggregated at national level

### 3. World Development Indicators (WDI)
- **Files**: 
  - `data/wdi_and_gdf_csv/wdi_gdf_data.csv` (main data)
  - `data/wdi_and_gdf_csv/wdi_gdf_country.csv` (country code mappings)
- **Source**: World Bank World Development Indicators and Global Development Finance
- **Coverage**: 1993–2010, 200+ countries
- **WDI Series Used**:

| WDI Code | Variable Name | Description |
|----------|---------------|-------------|
| NY.GDP.PCAP.CD | gdp_pc | GDP per capita (current US$) |
| SP.POP.TOTL | pop | Population, total |
| NE.TRD.GNFS.ZS | trade | Trade (% of GDP) |
| FP.CPI.TOTL.ZG | infl | Inflation, consumer prices (annual %) |
| NY.GDP.PETR.RT.ZS | oil | Oil rents (% of GDP) |
| SP.DYN.LE00.IN | leb | Life expectancy at birth, total (years) |
| SP.URB.TOTL.IN.ZS | urbpop | Urban population (% of total) |

### 4. FIFA Points Supplementary Data
The FIFA points file also contains supplementary economic data used as fallback:
- `gdppercapitacurrentus` → fills missing `gdp_pc`
- `tradeofgdp` → fills missing `trade`
- `inflation` → fills missing `infl`
- `lifeexpect` → fills missing `leb`

## Variable Definitions

| Variable | Description | Unit/Scale | Source | Transformations/Construction | Notes |
|----------|-------------|------------|--------|------------------------------|-------|
| country | Country name (standardized) | text | FIFA points file | Mapped to WDI naming conventions | 150+ countries |
| year | Calendar year | year | Derived | Original year codes (1-18) + 1992 | 1993–2010 |
| confed | Football confederation | code | Club rankings | 1=UEFA, 2=CONMEBOL, 3=CONCACAF, 4=AFC, 5=CAF, 6=OFC | Based on FIFA codes |
| fifa_points | FIFA ranking points | points | FIFA points file | As recorded by FIFA | See assumptions on aggregation frequency |
| gdp_pc | GDP per capita | current US$ | WDI (NY.GDP.PCAP.CD) | Fallback: FIFA file gdppercapitacurrentus | Nominal (current US$), not PPP |
| gdp_pc_sq | GDP per capita squared | US$^2 | Derived | gdp_pc^2 | Computed after merge |
| pop | Population | people | WDI (SP.POP.TOTL) | Mid-year estimate | |
| pop_sq | Population squared | people^2 | Derived | pop^2 | Computed after merge |
| trade | Trade openness | % of GDP | WDI (NE.TRD.GNFS.ZS) | Fallback: FIFA file tradeofgdp | Imports + exports |
| infl | Inflation | annual % | WDI (FP.CPI.TOTL.ZG) | Fallback: FIFA file inflation | Consumer price index |
| oil | Oil rents | % of GDP | WDI (NY.GDP.PETR.RT.ZS) | No fallback | Resource measure |
| leb | Life expectancy | years | WDI (SP.DYN.LE00.IN) | Fallback: FIFA file lifeexpect | At birth, both sexes |
| club | Domestic club strength | index | Club rankings file | Sum/average of club rankings by country | Missing pre-2000 (no zero fill) |
| urbpop | Urban population share | % | WDI (SP.URB.TOTL.IN.ZS) | Instrument for club | % of total population |
| urbpop_sq | Urban population share squared | %^2 | Derived | urbpop^2 | Computed after merge; instrument |

## Country Name Mappings (COUNTRY_REMAP)

The following country name mappings were applied to align FIFA names with WDI conventions:

| FIFA Name | WDI Name | Notes |
|-----------|----------|-------|
| Bahamas | Bahamas, The | Standardized naming |
| Bosnia-Herzegovina | Bosnia and Herzegovina | Hyphen handling |
| Cape Verde Islands | Cape Verde | Shortened form |
| China PR | China | People's Republic dropped |
| Congo | Congo, Rep. | Republic specified |
| Congo DR | Congo, Dem. Rep. | Democratic Republic specified |
| Egypt | Egypt, Arab Rep. | Official WDI name |
| FYR Macedonia | Macedonia, FYR | Order reversed |
| Gambia | Gambia, The | Standardized naming |
| Hong Kong | Hong Kong SAR, China | SAR specified |
| Iran | Iran, Islamic Rep. | Official WDI name |
| Korea DPR | Korea, Dem. Rep. | North Korea |
| Korea Republic | Korea, Rep. | South Korea |
| Kyrgyzstan | Kyrgyz Republic | Official WDI name |
| Laos | Lao PDR | Official WDI name |
| Macau | Macao SAR, China | SAR specified |
| Russia | Russian Federation | Official WDI name |
| Slovakia | Slovak Republic | Official WDI name |
| Syria | Syrian Arab Republic | Official WDI name |
| USA | United States | Full name |
| Venezuela | Venezuela, RB | Bolivarian Republic |
| Yemen | Yemen, Rep. | Republic specified |
| Faroe Islands | **EXCLUDED** | No WDI data available |

## Construction Notes

### Data Pipeline Steps (`scripts/build_panel.py`)

1. **Load FIFA points**: Read and transform year format, rename columns
2. **Load WDI data**: Extract relevant series, reshape from wide to long
3. **Load club rankings**: Reshape from wide to long, extract confederation codes
4. **Country code mapping**: Map FIFA country names to WDI country codes
5. **Merge datasets**: 
   - Left join WDI data to FIFA data on country code + year
   - Left join club data on FIFA country code + year
   - Left join confederation data on country code
6. **Apply fallbacks**: Fill missing WDI values with FIFA file supplementary data
7. **Compute derived variables**: Create squared terms (gdp_pc_sq, pop_sq, urbpop_sq)
8. **Filter and export**: Select columns, sort, save to CSV

### Missing Data Handling

- **Faroe Islands**: Excluded entirely (no WDI data)
- **Other countries**: Missing WDI values filled from FIFA supplementary data where available
- **Club data**: Missing values remain null (no zero fill in pre-2000 years)
- **Listwise deletion**: Applied in regression models (complete case analysis)

### Sample Restrictions

- **Years**: 1993–2010 only (FIFA points data availability)
- **Countries**: Must have FIFA points data
- **Club data**: Available from 2000 onwards only (earlier years are null)

## Data Quality Notes

1. **GDP per capita**: Mix of WDI and FIFA source data; some countries may have gaps
2. **Club strength**: Missing values in 1993-1999 indicate no data, not zero ranking
3. **Confederations**: OFC (Oceania) may have limited observations
4. **Panel balance**: Unbalanced panel due to country entry/exit from FIFA rankings
5. **Oil rents**: May be zero for non-oil-producing countries

## Assumptions and open points

- **FIFA points aggregation**: The source file provides a single annual points value per country-year. The exact aggregation method (monthly average vs year-end snapshot) is not documented in the raw file. We treat it as the annual FIFA ranking points for the given year.

## Usage in Regression Models

### Equation (1): Baseline
- **Dependent**: `fifa_points`
- **Independent**: `gdp_pc`, `gdp_pc_sq`, `pop`, `pop_sq`
- **Effects**: Country + time fixed effects
- **SEs**: Clustered by country

### Equation (2): With Controls
- **Dependent**: `fifa_points`
- **Independent**: Equation (1) + `trade`, `infl`, `oil`, `leb`
- **Effects**: Country + time fixed effects
- **SEs**: Clustered by country

### Equation (3): IV/2SLS
- **Dependent**: `fifa_points`
- **Independent**: Equation (2) + `club`
- **Instruments**: `urbpop`, `urbpop_sq` (for `club`)
- **Effects**: Country + time fixed effects (via demeaning)
- **SEs**: Clustered by country
