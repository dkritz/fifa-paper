"""Build data/analysis/panel.csv from raw inputs.

Inputs:
- data/fifa_points/fifa_excel_long_93_10_sheet1.csv (FIFA points + some WDI)
- data/club_rankings/fifa_club_merge_2000_plus.csv (club strength + confed)
- data/wdi_and_gdf_csv/wdi_gdf_data.csv (WDI series)
- data/wdi_and_gdf_csv/wdi_gdf_country.csv (country code mapping)
"""

import os

import pandas as pd


FIFA_PATH = "data/fifa_points/fifa_excel_long_93_10_sheet1.csv"
CLUB_PATH = "data/club_rankings/fifa_club_merge_2000_plus.csv"
WDI_PATH = "data/wdi_and_gdf_csv/wdi_gdf_data.csv"
COUNTRY_PATH = "data/wdi_and_gdf_csv/wdi_gdf_country.csv"
OUTPUT_PATH = "data/analysis/panel.csv"

YEARS = list(range(1993, 2011))

WDI_CODES = {
    "NY.GDP.PCAP.CD": "gdp_pc",
    "SP.POP.TOTL": "pop",
    "NE.TRD.GNFS.ZS": "trade",
    "FP.CPI.TOTL.ZG": "infl",
    "NY.GDP.PETR.RT.ZS": "oil",
    "SP.DYN.LE00.IN": "leb",
    "SP.URB.TOTL.IN.ZS": "urbpop",
}

CONFED_MAP = {
    1: "UEFA",
    2: "CONMEBOL",
    3: "CONCACAF",
    4: "AFC",
    5: "CAF",
    6: "OFC",
}

COUNTRY_REMAP = {
    "Bahamas": "Bahamas, The",
    "Bosnia-Herzegovina": "Bosnia and Herzegovina",
    "Cape Verde Islands": "Cape Verde",
    "China PR": "China",
    "Congo": "Congo, Rep.",
    "Congo DR": "Congo, Dem. Rep.",
    "Egypt": "Egypt, Arab Rep.",
    "FYR Macedonia": "Macedonia, FYR",
    "Gambia": "Gambia, The",
    "Hong Kong": "Hong Kong SAR, China",
    "Iran": "Iran, Islamic Rep.",
    "Korea DPR": "Korea, Dem. Rep.",
    "Korea Republic": "Korea, Rep.",
    "Kyrgyzstan": "Kyrgyz Republic",
    "Laos": "Lao PDR",
    "Macau": "Macao SAR, China",
    "Russia": "Russian Federation",
    "Slovakia": "Slovak Republic",
    "Syria": "Syrian Arab Republic",
    "USA": "United States",
    "Venezuela": "Venezuela, RB",
    "Yemen": "Yemen, Rep.",
    "Faroe Islands": None,
}


def load_fifa():
    fifa = pd.read_csv(FIFA_PATH)
    fifa = fifa.rename(columns={"fps": "fifa_points"})
    fifa["year"] = fifa["year"].astype(int) + 1992
    fifa = fifa[fifa["year"].isin(YEARS)]
    mapped = fifa["country"].map(COUNTRY_REMAP)
    fifa["country_wdi"] = mapped.where(mapped.notna(), fifa["country"])
    return fifa


def load_country_map():
    countries = pd.read_csv(COUNTRY_PATH, encoding="cp1252")
    name_to_code = {}
    for col in ["Table Name", "Short Name"]:
        for _, row in countries[[col, "Country Code"]].dropna().iterrows():
            name_to_code[row[col]] = row["Country Code"]
    return name_to_code


def load_wdi():
    year_cols = [str(y) for y in YEARS]
    wdi = pd.read_csv(WDI_PATH, usecols=["Series Code", "Country Code"] + year_cols)
    wdi = wdi[wdi["Series Code"].isin(WDI_CODES.keys())]
    wdi = wdi.melt(
        id_vars=["Series Code", "Country Code"],
        var_name="year",
        value_name="value",
    )
    wdi["year"] = wdi["year"].astype(int)
    wdi["variable"] = wdi["Series Code"].map(WDI_CODES)
    wdi = (
        wdi.pivot_table(
            index=["Country Code", "year"],
            columns="variable",
            values="value",
            aggfunc="first",
        )
        .reset_index()
    )
    return wdi


def load_club():
    club = pd.read_csv(CLUB_PATH)
    club_cols = [c for c in club.columns if c.startswith("CLUB")]
    club_long = club.melt(
        id_vars=["TEAM", "CODE", "CONF-Code"],
        value_vars=club_cols,
        var_name="year",
        value_name="club",
    )
    club_long["year"] = club_long["year"].str.replace("CLUB", "", regex=False).astype(int)
    club_long = club_long[club_long["year"].isin(YEARS)]
    confed = (
        club[["CODE", "CONF-Code"]]
        .dropna()
        .drop_duplicates()
        .rename(columns={"CODE": "country_code", "CONF-Code": "conf_code"})
    )
    confed["confed"] = confed["conf_code"].map(CONFED_MAP)
    club_long = club_long.rename(columns={"CODE": "country_code"})
    name_to_fifa = club[["TEAM", "CODE"]].dropna().drop_duplicates()
    return club_long, confed[["country_code", "confed"]], name_to_fifa


def main():
    fifa = load_fifa()
    name_to_code = load_country_map()
    fifa["country_code"] = fifa["country_wdi"].map(name_to_code)
    fifa = fifa[fifa["country_wdi"].ne("Faroe Islands")]

    wdi = load_wdi()
    club_long, confed, name_to_fifa = load_club()
    fifa = fifa.merge(name_to_fifa, how="left", left_on="country", right_on="TEAM")
    fifa = fifa.rename(columns={"CODE": "fifa_code"})

    panel = fifa.merge(
        wdi,
        how="left",
        left_on=["country_code", "year"],
        right_on=["Country Code", "year"],
    )
    panel = panel.merge(
        club_long[["country_code", "year", "club"]],
        how="left",
        left_on=["fifa_code", "year"],
        right_on=["country_code", "year"],
    )
    panel = panel.merge(
        confed,
        how="left",
        left_on="fifa_code",
        right_on="country_code",
    )

    # Fill from FIFA data where WDI missing
    if "gdppercapitacurrentus" in panel.columns:
        panel["gdp_pc"] = panel["gdp_pc"].fillna(panel["gdppercapitacurrentus"])
    if "tradeofgdp" in panel.columns:
        panel["trade"] = panel["trade"].fillna(panel["tradeofgdp"])
    if "inflation" in panel.columns:
        panel["infl"] = panel["infl"].fillna(panel["inflation"])
    if "lifeexpect" in panel.columns:
        panel["leb"] = panel["leb"].fillna(panel["lifeexpect"])

    panel["gdp_pc_sq"] = panel["gdp_pc"] ** 2
    panel["pop_sq"] = panel["pop"] ** 2
    panel["urbpop_sq"] = panel["urbpop"] ** 2

    columns = [
        "country",
        "year",
        "confed",
        "fifa_points",
        "gdp_pc",
        "gdp_pc_sq",
        "pop",
        "pop_sq",
        "trade",
        "infl",
        "oil",
        "leb",
        "club",
        "urbpop",
        "urbpop_sq",
    ]

    panel = panel[columns]
    panel = panel.sort_values(["country", "year"])

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    panel.to_csv(OUTPUT_PATH, index=False)

    missing_codes = fifa.loc[fifa["country_code"].isna(), "country"].unique().tolist()
    if missing_codes:
        print("Missing country code mappings:", missing_codes)


if __name__ == "__main__":
    main()
