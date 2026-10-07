import os

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# =========================================================
# CONFIG
# =========================================================

load_dotenv()

DB_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://energy_user:energy_password@localhost:5432/energy_db"
)

engine = create_engine(DB_URL)

st.set_page_config(
    page_title="Energy Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

.stApp {
    background: #071421;
    color: #EAF4F7;
}

header {
    background: transparent !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #0A1D2A;
    border-right: 1px solid #183C4C;
}

section[data-testid="stSidebar"] * {
    color: #DCEBF0 !important;
}


/* SECTION TITLES */

.section-title {
    color: #F1F7F9;
    font-size: 25px;
    font-weight: 750;
    margin-top: 28px;
    margin-bottom: 18px;
}


/* CHART SPACING */

div[data-testid="stPlotlyChart"] {
    background: #0A1D2A;
    border-radius: 16px;
    padding: 4px;
}


/* EXPANDER */

div[data-testid="stExpander"] {
    background: #0A1D2A;
    border: 1px solid #183B4B;
    border-radius: 14px;
}


/* SELECTBOX */

div[data-baseweb="select"] > div {
    background-color: #102A38;
    border-color: #275263;
}


/* FOOTER */

.dashboard-footer {
    text-align: center;
    color: #607D88;
    font-size: 12px;
    padding: 35px 0 15px 0;
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# DATABASE
# =========================================================

@st.cache_data(ttl=300)
def run_query(query, params=None):

    with engine.connect() as conn:

        return pd.read_sql(
            text(query),
            conn,
            params=params
        )


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data(ttl=300)
def load_energy_data():

    query = """
        SELECT
            country,
            year,
            iso_code,
            population,
            gdp,
            primary_energy_consumption,
            energy_per_capita,
            electricity_generation,
            renewables_electricity,
            solar_electricity,
            wind_electricity,
            renewables_share_energy,
            fossil_share_energy,
            oil_production,
            gas_production,
            greenhouse_gas_emissions
        FROM clean_energy
        WHERE entity_type = 'country'
        ORDER BY country, year
    """

    return run_query(query)


try:

    df = load_energy_data()

except Exception as e:

    st.error("Unable to connect to PostgreSQL.")

    st.code(str(e))

    st.stop()


# =========================================================
# DATA PREPARATION
# =========================================================

df["year"] = pd.to_numeric(
    df["year"],
    errors="coerce"
)

numeric_columns = [
    "population",
    "gdp",
    "primary_energy_consumption",
    "energy_per_capita",
    "electricity_generation",
    "renewables_electricity",
    "solar_electricity",
    "wind_electricity",
    "renewables_share_energy",
    "fossil_share_energy",
    "oil_production",
    "gas_production",
    "greenhouse_gas_emissions",
]

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


df["gdp_per_capita"] = (
    df["gdp"] / df["population"]
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            color:#35D8B8;
            font-size:21px;
            font-weight:800;
            margin-bottom:4px;
        ">
            ⚡ Energy Intelligence
        </div>

        <div style="
            color:#829DA8;
            font-size:12px;
            margin-bottom:25px;
        ">
            Data & Research Analytics Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Analysis Controls")

    countries = sorted(
        df["country"]
        .dropna()
        .unique()
        .tolist()
    )

    if "India" in countries:

        default_index = countries.index("India")

    else:

        default_index = 0

    country = st.selectbox(
        "Country",
        countries,
        index=default_index
    )

    year_range = st.slider(
        "Analysis Period",
        min_value=2000,
        max_value=2024,
        value=(2015, 2024)
    )

    st.markdown("---")

    st.markdown(
        """
        **Data Source**

        Our World in Data  
        Energy Dataset

        **Pipeline**

        Python → PostgreSQL  
        SQL → Streamlit
        """
    )


# =========================================================
# HERO
# =========================================================

st.html(
    """
    <div style="
        background:
            radial-gradient(
                circle at 88% 20%,
                rgba(53,216,184,0.18),
                transparent 32%
            ),
            linear-gradient(
                135deg,
                #0B2233 0%,
                #0B2E3A 55%,
                #0C3940 100%
            );

        border:1px solid #1D5A65;
        border-radius:22px;

        padding:42px 48px;
        margin-bottom:32px;

        box-shadow:
            0 18px 45px rgba(0,0,0,0.25);
    ">

        <div style="
            display:inline-block;
            background:rgba(53,216,184,0.10);
            color:#35D8B8;
            border:1px solid rgba(53,216,184,0.35);
            padding:7px 14px;
            border-radius:20px;
            font-size:11px;
            font-weight:800;
            letter-spacing:1.6px;
            margin-bottom:17px;
        ">
            DATA & RESEARCH ANALYTICS
        </div>

        <div style="
            color:#F4FAFC;
            font-size:42px;
            font-weight:850;
            line-height:1.15;
            margin-bottom:13px;
        ">
            ⚡ Energy Intelligence Dashboard
        </div>

        <div style="
            color:#AFC6CF;
            font-size:17px;
            line-height:1.65;
            max-width:850px;
        ">
            India-focused energy analytics combining
            Python data engineering, PostgreSQL analytics,
            SQL and interactive research visualization.
        </div>

    </div>
    """
)


# =========================================================
# SELECTED COUNTRY DATA
# =========================================================

country_df = df[
    (df["country"] == country) &
    (df["year"] >= year_range[0]) &
    (df["year"] <= year_range[1])
].copy()

country_df = country_df.sort_values("year")


# =========================================================
# YOY
# =========================================================

country_df["yoy_growth_pct"] = (
    country_df[
        "primary_energy_consumption"
    ].pct_change() * 100
)


# =========================================================
# LATEST VALUES
# =========================================================

valid_energy = country_df[
    country_df[
        "primary_energy_consumption"
    ].notna()
]

if not valid_energy.empty:

    latest_energy_row = valid_energy.iloc[-1]

    latest_year = int(
        latest_energy_row["year"]
    )

    latest_energy = latest_energy_row[
        "primary_energy_consumption"
    ]

    latest_growth = latest_energy_row[
        "yoy_growth_pct"
    ]

else:

    latest_year = None
    latest_energy = None
    latest_growth = None


valid_renewable = country_df[
    country_df[
        "renewables_share_energy"
    ].notna()
]

if not valid_renewable.empty:

    latest_renewable = valid_renewable.iloc[-1][
        "renewables_share_energy"
    ]

    renewable_year = int(
        valid_renewable.iloc[-1]["year"]
    )

else:

    latest_renewable = None
    renewable_year = None


# =========================================================
# SECTION TITLE
# =========================================================

st.markdown(
    f"""
    <div class="section-title">
        {country} — Key Indicators
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# KPI CARDS
# =========================================================

k1, k2, k3, k4 = st.columns(4)


def kpi_card(label, value, description, accent=False):

    value_color = "#35D8B8" if accent else "#F3FAFC"

    return f"""
    <div style="
        background:linear-gradient(
            145deg,
            #0D2331,
            #0B1D2A
        );

        border:1px solid #1B4353;
        border-radius:17px;

        padding:23px 24px;

        min-height:145px;

        box-shadow:
            0 8px 25px rgba(0,0,0,0.18);
    ">

        <div style="
            color:#8EAAB5;
            font-size:12px;
            font-weight:700;
            text-transform:uppercase;
            letter-spacing:1px;
            margin-bottom:12px;
        ">
            {label}
        </div>

        <div style="
            color:{value_color};
            font-size:30px;
            font-weight:850;
            margin-bottom:8px;
        ">
            {value}
        </div>

        <div style="
            color:#6F8D99;
            font-size:12px;
        ">
            {description}
        </div>

    </div>
    """


with k1:

    value = (
        f"{latest_energy:,.2f}"
        if pd.notna(latest_energy)
        else "N/A"
    )

    st.html(
        kpi_card(
            "Primary Energy",
            value,
            f"Latest available · {latest_year}",
        )
    )


with k2:

    value = (
        f"{latest_growth:.2f}%"
        if pd.notna(latest_growth)
        else "N/A"
    )

    st.html(
        kpi_card(
            "YoY Energy Growth",
            value,
            "Year-over-year change",
            accent=True
        )
    )


with k3:

    value = (
        f"{latest_renewable:.2f}%"
        if pd.notna(latest_renewable)
        else "N/A"
    )

    st.html(
        kpi_card(
            "Renewable Share",
            value,
            f"Latest available · {renewable_year}",
            accent=True
        )
    )


with k4:

    st.html(
        kpi_card(
            "Observations",
            f"{len(country_df):,}",
            "Selected analysis period"
        )
    )


# =========================================================
# ENERGY CONSUMPTION TREND
# =========================================================

st.markdown(
    '<div class="section-title">Energy Consumption Trend</div>',
    unsafe_allow_html=True
)

trend_df = country_df[
    country_df[
        "primary_energy_consumption"
    ].notna()
].copy()


if not trend_df.empty:

    fig = px.line(
        trend_df,
        x="year",
        y="primary_energy_consumption",
        markers=True,
        labels={
            "year": "Year",
            "primary_energy_consumption":
                "Primary Energy"
        }
    )

    fig.update_traces(
        line=dict(
            color="#35D8B8",
            width=3
        ),
        marker=dict(
            size=7,
            color="#35D8B8"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0A1D2A",
        plot_bgcolor="#0A1D2A",
        font=dict(
            color="#C8D9DF"
        ),
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        hovermode="x unified",
        xaxis=dict(
            gridcolor="#183747",
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#183747",
            zeroline=False
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# RENEWABLE COMPARISON
# =========================================================

st.markdown(
    '<div class="section-title">Renewable Energy Share — 2024</div>',
    unsafe_allow_html=True
)

renewable_df = df[
    (df["year"] == 2024) &
    (df["renewables_share_energy"].notna())
].copy()

renewable_df = renewable_df[
    [
        "country",
        "renewables_share_energy"
    ]
].drop_duplicates()

renewable_df = renewable_df.sort_values(
    "renewables_share_energy",
    ascending=False
).head(10)

renewable_df = renewable_df.sort_values(
    "renewables_share_energy"
)


if not renewable_df.empty:

    fig = px.bar(
        renewable_df,
        x="renewables_share_energy",
        y="country",
        orientation="h",
        labels={
            "renewables_share_energy":
                "Renewable Share (%)",
            "country":
                "Country"
        }
    )

    fig.update_traces(
        marker_color="#35D8B8"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0A1D2A",
        plot_bgcolor="#0A1D2A",
        font=dict(
            color="#C8D9DF"
        ),
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        xaxis=dict(
            gridcolor="#183747",
            zeroline=False
        ),
        yaxis=dict(
            gridcolor="#183747",
            zeroline=False
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# TWO COLUMN ANALYSIS
# =========================================================

left, right = st.columns(2)


# =========================================================
# YOY GROWTH
# =========================================================

with left:

    st.markdown(
        '<div class="section-title">Year-over-Year Growth</div>',
        unsafe_allow_html=True
    )

    growth_df = country_df[
        country_df["yoy_growth_pct"].notna()
    ].copy()

    if not growth_df.empty:

        fig = px.bar(
            growth_df,
            x="year",
            y="yoy_growth_pct",
            labels={
                "year": "Year",
                "yoy_growth_pct":
                    "YoY Growth (%)"
            }
        )

        fig.update_traces(
            marker_color="#4AA3DF"
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0A1D2A",
            plot_bgcolor="#0A1D2A",
            font=dict(
                color="#C8D9DF"
            ),
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis=dict(
                gridcolor="#183747"
            ),
            yaxis=dict(
                gridcolor="#183747",
                zeroline=True,
                zerolinecolor="#54717C"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# ENERGY VS GDP
# =========================================================

with right:

    st.markdown(
        '<div class="section-title">Energy vs GDP per Capita</div>',
        unsafe_allow_html=True
    )

    scatter_df = country_df[
        country_df[
            "energy_per_capita"
        ].notna() &
        country_df[
            "gdp_per_capita"
        ].notna()
    ].copy()

    if not scatter_df.empty:

        fig = px.scatter(
            scatter_df,
            x="gdp_per_capita",
            y="energy_per_capita",
            size="year",
            hover_name="year",
            labels={
                "gdp_per_capita":
                    "GDP per Capita",
                "energy_per_capita":
                    "Energy per Capita"
            }
        )

        fig.update_traces(
            marker=dict(
                color="#35D8B8",
                line=dict(
                    color="#C7FFF4",
                    width=1
                )
            )
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0A1D2A",
            plot_bgcolor="#0A1D2A",
            font=dict(
                color="#C8D9DF"
            ),
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis=dict(
                gridcolor="#183747"
            ),
            yaxis=dict(
                gridcolor="#183747"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# ENERGY MIX
# =========================================================

st.markdown(
    '<div class="section-title">Energy Mix</div>',
    unsafe_allow_html=True
)

if latest_year is not None:

    mix_df = country_df[
        country_df["year"] == latest_year
    ].copy()

    if not mix_df.empty:

        mix = mix_df.iloc[0]

        renewable = mix[
            "renewables_share_energy"
        ]

        fossil = mix[
            "fossil_share_energy"
        ]

        if pd.notna(renewable) and pd.notna(fossil):

            other = max(
                0,
                100 - renewable - fossil
            )

            energy_mix = pd.DataFrame(
                {
                    "Category": [
                        "Fossil",
                        "Renewable",
                        "Other"
                    ],
                    "Share": [
                        fossil,
                        renewable,
                        other
                    ]
                }
            )

            fig = px.bar(
                energy_mix,
                x="Category",
                y="Share",
                text="Share",
                labels={
                    "Share":
                        "Share of Energy (%)",
                    "Category":
                        "Energy Source"
                }
            )

            fig.update_traces(
                marker_color=[
                    "#4AA3DF",
                    "#35D8B8",
                    "#607D88"
                ],
                texttemplate="%{text:.2f}%",
                textposition="outside"
            )

            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="#0A1D2A",
                plot_bgcolor="#0A1D2A",
                font=dict(
                    color="#C8D9DF"
                ),
                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                ),
                yaxis=dict(
                    range=[0, 105],
                    gridcolor="#183747"
                ),
                xaxis=dict(
                    gridcolor="#183747"
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# =========================================================
# RESEARCH INSIGHT
# =========================================================

st.html(
    """
    <div style="
        background:
            linear-gradient(
                135deg,
                rgba(53,216,184,0.08),
                rgba(39,113,136,0.08)
            );

        border-left:4px solid #35D8B8;
        border-radius:12px;

        padding:19px 22px;
        margin:25px 0;

        color:#BBD0D8;
        line-height:1.65;
    ">

        <div style="
            color:#35D8B8;
            font-size:16px;
            font-weight:750;
        ">
            📊 Research Insight
        </div>

        <br>

        India's primary energy consumption has increased
        substantially over the recent decade, while renewable
        energy's share has gradually expanded.

        <br><br>

        However, fossil fuels continue to represent the
        majority of India's energy mix.

        <br><br>

        <strong>Note:</strong>
        These are descriptive historical relationships and
        should not be interpreted as evidence of causality.

    </div>
    """
)


# =========================================================
# METHODOLOGY
# =========================================================

with st.expander("📚 Data & Methodology"):

    st.markdown(
        """
### Data Pipeline

**Raw OWID Energy Dataset**

↓

**Python / Pandas**

Data cleaning, validation and transformation

↓

**PostgreSQL**

Raw and cleaned analytical tables

↓

**SQL Analytics**

Trend analysis, growth calculations and energy metrics

↓

**Streamlit**

Interactive research dashboard

---

### Validation Performed

- Country-year duplicate checks
- Negative-value checks
- Renewable/fossil share validation
- Missing-value profiling
- IQR-based outlier detection
- Sparse-year identification

---

### Important Data Note

The latest calendar year does not necessarily represent
the latest analytically usable observation because some
variables have incomplete coverage.

For India, the latest usable primary-energy observation
in the current dataset is 2024.

---

### Source

Our World in Data — Energy Dataset
"""
    )


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="dashboard-footer">

        Energy Intelligence Dashboard
        · Data & Research Analytics

        <br><br>

        Built with Python · Pandas · PostgreSQL · SQL · Streamlit

    </div>
    """
)