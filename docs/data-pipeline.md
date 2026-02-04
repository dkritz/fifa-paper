# Data Pipeline Documentation

This document describes the complete data pipeline for the FIFA Paper Replication project, from raw data sources to the final analysis-ready panel dataset.

## Overview

The data pipeline transforms three raw data sources into a unified panel dataset suitable for econometric analysis. The pipeline is implemented in `scripts/build_panel.py`.

```
Raw Data Sources:
├── FIFA Points (1993-2010)
├── Club Rankings (2000-2013)  
└── World Development Indicators (WDI)

↓ ETL Pipeline (build_panel.py)

Analysis Dataset:
└── data/analysis/panel.csv
    ├── 15 variables
    ├── 1993-2010 panel
    └── 150+ countries
```

## Data Sources Detail

### 1. FIFA World Rankings Points
**File**: `data/fifa_points/fifa_excel_long_93_10_sheet1.csv`

**Original Source**: FIFA World Rankings system tracking national team performance from 1993-2010.

**Schema**:
```
cid,year,country,fps,gdpgrowthannual,gdppercapitacurrentus,
strdum,tradeofgdp,inflation,healthexpenditurepercapitacurren,lifeexpect
```

**Key Variables**:
- `fps`: FIFA ranking points (converted to `fifa_points`)
- `country`: Country name in FIFA convention
- `year`: Year index (1-18, converted to 1993-2010)
- Supplementary economic data used as fallback

### 2. FIFA Club Rankings
**File**: `data/club_rankings/fifa_club_merge_2000_plus.csv`

**Original Source**: FIFA club coefficient rankings measuring domestic league strength.

**Schema** (wide format):
```
TEAM,CODE,CONF-Code,FIFAid,FIFA2000,FIFA2001,...,FIFA2013,
Nat,CLUB2000,CLUB2001,...,CLUB2013,Conf_Code
```

**Key Variables**:
- `TEAM`: National team name
- `CODE`: 3-letter country code
- `CONF-Code`: Confederation code (1-6)
- `CLUB2000`-`CLUB2013`: Annual club ranking points

**Confederation Mapping**:
| Code | Confederation | Region |
|------|---------------|--------|
| 1 | UEFA | Europe |
| 2 | CONMEBOL | South America |
| 3 | CONCACAF | North/Central America & Caribbean |
| 4 | AFC | Asia |
| 5 | CAF | Africa |
| 6 | OFC | Oceania |

### 3. World Development Indicators (WDI)
**Files**: 
- `data/wdi_and_gdf_csv/wdi_gdf_data.csv`
- `data/wdi_and_gdf_csv/wdi_gdf_country.csv`

**Original Source**: World Bank's comprehensive development database.

**Series Extracted**:
| Variable | WDI Code | Description |
|----------|----------|-------------|
| gdp_pc | NY.GDP.PCAP.CD | GDP per capita (current US$) |
| pop | SP.POP.TOTL | Total population |
| trade | NE.TRD.GNFS.ZS | Trade (% of GDP) |
| infl | FP.CPI.TOTL.ZG | Consumer price inflation (%) |
| oil | NY.GDP.PETR.RT.ZS | Oil rents (% of GDP) |
| leb | SP.DYN.LE00.IN | Life expectancy at birth |
| urbpop | SP.URB.TOTL.IN.ZS | Urban population (% of total) |

## Pipeline Steps

### Step 1: Load and Transform FIFA Points
```python
def load_fifa():
    # Read CSV
    # Rename fps → fifa_points
    # Convert year: 1-18 → 1993-2010
    # Apply country name mappings
    # Filter years 1993-2010
```

**Transformations**:
- Year conversion: `year = year_index + 1992`
- Country name standardization (25 mappings applied)
- Faroe Islands excluded

### Step 2: Load Country Code Mappings
```python
def load_country_map():
    # Read wdi_gdf_country.csv
    # Build name → code mapping from Table Name and Short Name columns
```

**Purpose**: Bridge FIFA country names to WDI country codes.

### Step 3: Load and Reshape WDI Data
```python
def load_wdi():
    # Read wdi_gdf_data.csv
    # Extract 7 series of interest
    # Reshape: wide (years as columns) → long (year as rows)
    # Rename series codes to variable names
```

**Transformations**:
- Wide-to-long reshape
- Series code mapping (e.g., NY.GDP.PCAP.CD → gdp_pc)
- Filter to 1993-2010

### Step 4: Load and Reshape Club Data
```python
def load_club():
    # Read fifa_club_merge_2000_plus.csv
    # Reshape CLUB2000-CLUB2013 from wide to long
    # Extract confederation mappings
    # Map confederation codes to names
```

**Transformations**:
- Wide-to-long reshape for club rankings
- Confederation code mapping (1-6 → UEFA, CAF, etc.)
- Filter to 2000-2010 (club data availability)

### Step 5: Merge Datasets
```python
# Main merge sequence:
1. fifa + country_codes
2. fifa + wdi (on country_code + year)
3. fifa + club (on fifa_code + year)
4. fifa + confederation (on fifa_code)
```

**Merge Logic**:
- Left joins preserve all FIFA points observations
- Unmatched WDI/club data becomes null

### Step 6: Apply Fallbacks
```python
# Where WDI is missing, fill from FIFA supplementary data:
- gdp_pc ← gdppercapitacurrentus
- trade ← tradeofgdp
- infl ← inflation
- leb ← lifeexpect
```

### Step 7: Compute Derived Variables
```python
# Squared terms for quadratic specifications:
- gdp_pc_sq = gdp_pc ** 2
- pop_sq = pop ** 2
- urbpop_sq = urbpop ** 2
```

### Step 8: Export
```python
# Select final column order
# Sort by country, year
# Export to data/analysis/panel.csv
```

**Runtime summary**:
- Prints row/column counts and year range
- Reports missing values by column (non-zero only)

## Data Quality Controls

### Country Name Harmonization
25 country name mappings applied to align FIFA and WDI conventions:

**Examples**:
- "USA" → "United States"
- "Korea Republic" → "Korea, Rep."
- "Russia" → "Russian Federation"

**Exclusions**:
- Faroe Islands: No WDI data available

### Missing Data Strategy

| Variable | Missing Strategy |
|----------|------------------|
| gdp_pc, trade, infl, leb | Fallback to FIFA supplementary data |
| club | Null for 1993-1999 (before data collection) |
| oil, urbpop | No fallback; use WDI only |

### Validation Checks

1. **Country code coverage**: Report unmapped countries
2. **Year range**: Enforce 1993-2010
3. **Duplicates**: Check for (country, year) duplicates
4. **Missingness**: Summary statistics on missing values

## Usage

### Building the Panel
```bash
cd /Users/dkritz/git/fifa-paper
python3 scripts/build_panel.py
```

**Output**: `data/analysis/panel.csv`

### Loading the Panel
```python
import pandas as pd
panel = pd.read_csv("data/analysis/panel.csv")
panel = panel.set_index(["country", "year"])
```

### Running Regressions
```bash
python3 scripts/replicate_stata.py --data data/analysis/panel.csv
```

**Output**: CSV files in `results/` directory

## Pipeline Dependencies

**Input Files Required**:
- `data/fifa_points/fifa_excel_long_93_10_sheet1.csv`
- `data/club_rankings/fifa_club_merge_2000_plus.csv`
- `data/wdi_and_gdf_csv/wdi_gdf_data.csv`
- `data/wdi_and_gdf_csv/wdi_gdf_country.csv`

**Output File**:
- `data/analysis/panel.csv`

**Python Dependencies**:
- pandas (data manipulation)
- numpy (numerical operations)

## Known Limitations

1. **Club data availability**: Only 2000-2010, earlier years set to 0/null
2. **Country coverage**: Limited to countries with both FIFA and WDI data
3. **Temporal alignment**: WDI annual data may not align perfectly with FIFA ranking dates
4. **GDP measurement**: Current US$ (not PPP), subject to exchange rate fluctuations

## Future Improvements

1. Add data validation tests
2. Create data quality reports
3. Document exact FIFA ranking calculation methodology
4. Add version control for raw data sources
5. Create data update workflow for extending beyond 2010
