⚡ Energy Intelligence Dashboard

<p align="center">
  <b>India-focused Energy Data Pipeline, SQL Analytics & Interactive Research Dashboard</b>
</p>

<p align="center">
  <a href="https://github.com/harsh1223-bit/energy-intelligence-dashboard">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Tests-4%20Passed-2EA44F?style=for-the-badge&logo=pytest&logoColor=white" alt="Tests">
</p>

📌 Overview

Energy Intelligence Dashboard is an end-to-end energy analytics project designed to transform raw global energy data into a structured, validated and queryable analytical dataset.

The project combines:

🐍 Python & Pandas for data ingestion and transformation

🐘 PostgreSQL for structured storage and analytical SQL

📊 Streamlit for interactive visualization

🐳 Docker for reproducible database infrastructure

🧪 Pytest for data-quality and pipeline testing

📈 SQL window functions for ranking and trend analysis

The analysis is primarily focused on India's energy landscape, while also providing international comparisons.

Research objective: Convert large-scale energy data into reliable metrics, trends and comparisons that can support energy-market and policy research.

🎯 Key Objectives

Objective

Description

📥 Data Collection

Collect structured energy data from OWID

🧹 Data Quality

Validate, clean and flag questionable observations

🗄️ Data Storage

Store processed data in PostgreSQL

📊 Analytics

Perform SQL-based energy analysis

📈 Visualization

Present findings through an interactive dashboard

🏗️ System Architecture

                         ┌─────────────────────────┐
                         │       🌍 OWID Data      │
                         │    Global Energy CSV    │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    🐍 Python Pipeline   │
                         │                         │
                         │ • Download              │
                         │ • Validation            │
                         │ • Transformation       │
                         │ • Cleaning              │
                         │ • Quality Checks        │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │     🐘 PostgreSQL       │
                         │                         │
                         │ • raw_energy            │
                         │ • clean_energy          │
                         │ • aggregates            │
                         │ • analytical views      │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
                    ▼                                   ▼
          ┌───────────────────┐               ┌───────────────────┐
          │    📊 SQL         │               │    ⚡ Streamlit   │
          │    Analytics      │               │    Dashboard      │
          │                   │               │                   │
          │ • Trends          │               │ • KPI Cards       │
          │ • YoY Growth      │               │ • Energy Trends   │
          │ • Rankings        │               │ • Comparisons     │
          │ • Energy Mix      │               │ • GDP Analysis    │
          └───────────────────┘               └───────────────────┘

📊 Dashboard

The Streamlit dashboard provides an interactive view of energy indicators.

Dashboard Features

Feature

Description

🇮🇳 Country Selection

Analyze individual countries

📅 Year Range

Explore historical energy trends

⚡ Primary Energy

Track energy consumption

🌱 Renewable Share

Measure renewable penetration

📈 YoY Growth

Analyze annual changes

🌍 Country Comparison

Compare renewable-energy shares

💰 Energy vs GDP

Explore energy and economic indicators

🔥 Energy Mix

Compare fossil and renewable shares

🔎 Research Insight

Automatically surface key observations

📚 Methodology

Explain data and analytical assumptions

📷 Dashboard Preview

Run the dashboard locally using Streamlit to explore the interactive interface.



streamlit run dashboard/app.py

🌍 Data Source

The project uses the Our World in Data Energy Dataset.

🔗 Dataset:

https://github.com/owid/energy-data

🔗 OWID Energy Data Documentation:

https://ourworldindata.org/energy

The dataset aggregates energy information from sources including:

Energy Institute

International Energy Agency

U.S. Energy Information Administration

Ember

Other international statistical sources

Important Data Note

This project uses a downloaded snapshot of the OWID CSV.

The downloaded file is preserved locally and identified using a SHA-256 checksum to improve reproducibility.



SHA-256:
266f2e2baad7975351bc9bb4aa061d22b1da9fe4c47d51d2ac6071e01e171f76

The raw CSV is intentionally excluded from Git because of its size.

🔄 Data Pipeline

The pipeline follows a reproducible sequence:



Download
   ↓
Schema Validation
   ↓
Raw Data Storage
   ↓
Country / Aggregate Classification
   ↓
Data Type Conversion
   ↓
Duplicate Detection
   ↓
Missing Value Analysis
   ↓
Range Validation
   ↓
Outlier Flagging
   ↓
PostgreSQL Loading
   ↓
SQL Analytics
   ↓
Streamlit Dashboard

🧹 Data Cleaning & Validation

The project intentionally separates data cleaning from data destruction.

Questionable observations are flagged rather than blindly deleted.

Cleaning Rules

Check

Approach

Country identification

Valid 3-letter ISO codes

Aggregate entities

Stored separately

Duplicate (country, year)

Checked and removed if present

Numeric parsing

Invalid values converted to missing

Negative values

Flagged

Percentage values

Checked for 0–100 range

Missing values

Reported rather than automatically imputed

Outliers

IQR-based flags

Sparse years

Reported for investigation

Raw data

Preserved separately

Validation Results



Country rows after cleaning:        17,265
Aggregate / non-country rows:        6,112
Duplicate country-year rows:             0
Negative-value violations:               0
Share-range violations:                  0
Year range:                         1900–2025

Important

An outlier flag does not automatically mean the observation is incorrect.

Energy datasets naturally contain large differences between countries because of population, economic size and resource availability.

🗄️ Database Design

The PostgreSQL database contains the following primary tables:

raw_energy

Stores the downloaded source data with minimal transformation.

clean_energy

Stores validated country-level observations used for analysis.

aggregates

Stores non-country and aggregate entities separately.

📐 Analytical SQL Views

The project includes analytical views for:

📈 Renewable energy comparisons

⚡ India energy trends

🌍 Energy vs GDP analysis

🛢️ Producer rankings

📊 Year-over-year changes

SQL techniques used include:



GROUP BY
ORDER BY
CASE WHEN
CTEs
Window Functions
RANK()
LAG()
Aggregation
Filtering

📈 Key Research Findings

The current dataset produced several notable observations.

🇮🇳 1. India's Energy Consumption Increased

India's primary energy consumption increased from:



2017:  8,571.67
2024: 11,336.06

This represents an increase of approximately:

32.3%

📊 2. India's Energy Growth Was Not Uniform

Selected year-over-year changes:

Year

YoY Change

2017

+3.74%

2018

+5.74%

2019

+2.41%

2020

−5.27%

2021

+8.56%

2022

+5.39%

2023

+7.64%

2024

+4.69%

The sharp decline in 2020 was followed by a strong rebound in 2021.

🌱 3. Renewable Share Increased

India's renewable share of energy increased from:



2017: 6.79%
2024: 9.15%

At the same time, fossil-fuel share remained high:



2024 Fossil Share: 89.67%

This highlights the coexistence of increasing renewable penetration with continued dependence on fossil energy.

🌎 International Comparison

Selected countries' renewable energy shares in 2024:

Rank

Country

Renewable Share

🥇 1

🇧🇷 Brazil

49.62%

🥈 2

🇨🇦 Canada

27.16%

🥉 3

🇩🇪 Germany

23.97%

4

🇬🇧 United Kingdom

21.29%

5

🇨🇳 China

17.47%

6

🇫🇷 France

16.47%

7

🇯🇵 Japan

12.70%

8

🇺🇸 United States

12.05%

9

🇮🇳 India

9.15%

10

🇷🇺 Russia

6.00%

This comparison is descriptive and depends on the dataset's definitions and coverage.

💰 Energy & GDP Analysis

The dashboard also compares:

Energy consumption per capita

GDP per capita

for India.

The objective is to identify patterns and relationships, not to establish causality.

⚠️ Correlation between energy and economic indicators should not be interpreted as proof that one directly causes the other.

🔎 Data Quality Insights

The validation pipeline identified substantial missingness in several indicators.

Examples include:

Indicator

Missing Values

Renewable Share

12,806

Fossil Share

12,806

Greenhouse Gas Emissions

11,878

Electricity Generation

10,688

Wind Electricity

9,574

Solar Electricity

9,386

Primary Energy Consumption

6,910

GDP

5,706

This is important when interpreting cross-country or historical comparisons.

🧪 Testing

The project includes automated tests using Pytest.

Current test result:



.... [100%]

4 passed in 0.34s

Run tests with:



python -m pytest -q

🛠️ Technology Stack

Programming

<p> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white"> </p>

Data & Analytics

Pandas

NumPy

SQL

PostgreSQL

Visualization

Streamlit

Plotly

Infrastructure

Docker

Docker Compose

Testing

Pytest

Development Tools

Git

GitHub

VS Code

Make

📁 Project Structure



energy-intelligence-dashboard/
│
├── 📂 data/
│   ├── raw/
│   │   └── owid-energy-data.csv
│   └── metadata.json
│
├── 📂 dashboard/
│   └── app.py
│
├── 📂 src/
│   ├── __init__.py
│   ├── config.py
│   ├── ingest.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── pipeline.py
│
├── 📂 sql/
│   ├── schema.sql
│   ├── views.sql
│   └── analytics.sql
│
├── 📂 tests/
│   └── test_pipeline.py
│
├── 📂 reports/
│   └── validation_report.md
│
├── 🐳 docker-compose.yml
├── ⚙️ Makefile
├── 🚀 run.sh
├── 📄 requirements.txt
├── 📄 .env.example
├── 📄 .gitignore
└── 📄 README.md

🚀 Getting Started

1️⃣ Clone the Repository



git clone https://github.com/harsh1223-bit/energy-intelligence-dashboard.git
cd energy-intelligence-dashboard

2️⃣ Create a Virtual Environment

macOS / Linux



python3 -m venv .venv
source .venv/bin/activate

Windows



python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies



pip install -r requirements.txt

🐳 Start PostgreSQL

Make sure Docker Desktop is running.

Then:



docker-compose up -d

If your Docker installation supports the newer syntax:



docker compose up -d

Check running containers:



docker ps

⚙️ Environment Configuration

Create a .env file:



cp .env.example .env

Example configuration:



POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=energy
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

Never commit your real .env file or database credentials to GitHub.

▶️ Run the Data Pipeline

The easiest option is:



./run.sh

Or execute the pipeline manually:



python -m src.pipeline

The pipeline will:

Download the energy dataset

Validate the schema

Save the raw dataset

Clean and classify observations

Generate validation reports

Load data into PostgreSQL

Prepare analytical tables/views

📊 Run the Dashboard

Start Streamlit:



streamlit run dashboard/app.py

Then open the local Streamlit URL shown in the terminal.

Usually:



http://localhost:8501

🧮 Example SQL Analysis

Example: India's energy trend.



SELECT
    year,
    primary_energy_consumption,
    renewables_share_energy,
    fossil_share_energy
FROM clean_energy
WHERE country = 'India'
  AND entity_type = 'country'
ORDER BY year DESC;

📈 Example: Year-over-Year Growth

The project uses SQL window functions such as LAG():



SELECT
    country,
    year,
    primary_energy_consumption,
    LAG(primary_energy_consumption)
        OVER (
            PARTITION BY country
            ORDER BY year
        ) AS previous_year_energy
FROM clean_energy
WHERE entity_type = 'country';

This allows year-over-year changes to be calculated directly in SQL.

🔬 Research Methodology

The project follows a simple research workflow:



Raw Data
   ↓
Data Validation
   ↓
Data Cleaning
   ↓
Database Modeling
   ↓
SQL Analysis
   ↓
Visualization
   ↓
Research Interpretation

The methodology emphasizes:

Reproducibility

Transparent cleaning

Data-quality reporting

SQL-based analysis

Separation of raw and processed data

Explicit treatment of missing values

Avoidance of unsupported causal claims

⚠️ Limitations

This project has several limitations.

1. Data Coverage

Historical coverage varies considerably across countries and indicators.

2. Missing Values

Several variables contain substantial missingness.

3. Latest-Year Coverage

The latest calendar year may not have complete country-level coverage.

For example, the 2025 data contains fewer country observations than many previous years.

4. Outliers

Large values may represent legitimate differences in population, GDP or energy production rather than errors.

5. No Causal Inference

The dashboard identifies trends and relationships but does not establish causality.

6. Dataset Version

The project uses a specific downloaded snapshot of the OWID dataset. Results may change when the upstream dataset is updated.

🚧 Future Improvements

Potential improvements include:

Add automated scheduled data ingestion

Add more energy sources

Add country-level energy production rankings

Add CO₂ emissions analysis

Add energy intensity indicators

Add forecasting models

Add anomaly detection

Add automated data-quality alerts

Add CI/CD with GitHub Actions

Deploy dashboard publicly

Add PostgreSQL indexing optimization

Add interactive map visualizations

Add downloadable analytical reports

🔁 Reproducibility

The project attempts to make analytical results reproducible by:

Recording the source URL

Recording the download timestamp

Recording a SHA-256 checksum

Keeping raw and processed data separate

Version-controlling source code

Using Docker for PostgreSQL

Providing SQL scripts

Providing automated tests

Providing validation reports

Example metadata:



{
  "url": "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv",
  "file": "data/raw/owid-energy-data.csv",
  "sha256": "266f2e2baad7975351bc9bb4aa061d22b1da9fe4c47d51d2ac6071e01e171f76"
}

📚 References

Our World in Data

🔗 https://ourworldindata.org/energy

OWID Energy Data Repository

🔗 https://github.com/owid/energy-data

Python

🔗 https://www.python.org/

Pandas

🔗 https://pandas.pydata.org/

PostgreSQL

🔗 https://www.postgresql.org/

Streamlit

🔗 https://streamlit.io/

Docker

🔗 https://www.docker.com/

Pytest

🔗 https://pytest.org/

📜 Data Attribution

This project uses energy data provided through Our World in Data and its underlying sources.

The dataset and its licensing/attribution requirements should be reviewed before redistribution or commercial use.

This repository does not claim ownership of the underlying energy dataset.

👨‍💻 Author

Harsh Sharma

🎓 Integrated M.Tech in Computer Science

📊 Specialization: Computational & Data Science

🏫 VIT Bhopal

🔗 Connect

<p>   <a href="https://github.com/harsh1223-bit">     <img src="https://img.shields.io/badge/GitHub-harsh1223--bit-181717?style=for-the-badge&logo=github" alt="GitHub">   </a> </p>

⭐ Project Summary

Energy Intelligence Dashboard demonstrates an end-to-end workflow for turning large-scale public energy data into a structured analytical product.

The project combines:

Data Engineering + SQL Analytics + Data Quality + Research Analysis + Interactive Visualization

with a particular focus on understanding India's energy consumption, renewable penetration and broader energy trends.

<p align="center">   <b>⚡ Built for Data Analytics, Energy Research & Decision Intelligence</b> </p> <p align="center">   If you found this project useful, consider giving it a ⭐ on GitHub. </p> ```