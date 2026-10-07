# ⚡ Energy Intelligence Dashboard

<p align="center">
  <strong>India-focused Energy Data Pipeline, SQL Analytics & Interactive Research Dashboard</strong>
</p>

<p align="center">
  <a href="https://github.com/harsh1223-bit/energy-intelligence-dashboard">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Tests-4%20Passed-2EA44F?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
</p>

<p align="center">
  <a href="https://github.com/harsh1223-bit/energy-intelligence-dashboard">⭐ View Repository</a>
  &nbsp;•&nbsp;
  <a href="https://ourworldindata.org/energy">🌍 Data Source</a>
</p>

---

## 📌 Overview

**Energy Intelligence Dashboard** is an end-to-end energy analytics project that transforms large-scale energy data into a structured, validated and queryable analytical dataset.

The project combines:

- 🐍 **Python & Pandas** for ingestion and transformation
- 🐘 **PostgreSQL** for structured storage and analytical SQL
- 📊 **Streamlit** for interactive visualization
- 🐳 **Docker** for reproducible database infrastructure
- 🧪 **Pytest** for pipeline testing
- 📈 **SQL window functions** for trend and ranking analysis

The analysis focuses primarily on **India's energy landscape**, while also providing international comparisons.

> 🎯 **Research objective:** Convert large-scale energy data into reliable metrics, trends and comparisons that can support energy-market and research analysis.

---

## 🎯 Key Objectives

| Objective | Description |
|:---|:---|
| 📥 **Data Collection** | Collect structured energy data from a reliable public source |
| 🧹 **Data Quality** | Validate, clean and flag questionable observations |
| 🗄️ **Data Storage** | Store processed data in PostgreSQL |
| 📊 **Analytics** | Perform SQL-based energy analysis |
| 📈 **Visualization** | Present findings through an interactive dashboard |

---

## 🏗️ System Architecture

```text
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
```

---

## 📊 Dashboard Features

<table>
<thead>
<tr><th>Icon</th><th>Feature</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>🇮🇳</td><td><strong>Country Selection</strong></td><td>Analyze individual countries</td></tr>
<tr><td>📅</td><td><strong>Year Range</strong></td><td>Explore historical energy trends</td></tr>
<tr><td>⚡</td><td><strong>Primary Energy</strong></td><td>Track energy consumption</td></tr>
<tr><td>🌱</td><td><strong>Renewable Share</strong></td><td>Measure renewable penetration</td></tr>
<tr><td>📈</td><td><strong>YoY Growth</strong></td><td>Analyze annual changes</td></tr>
<tr><td>🌍</td><td><strong>Country Comparison</strong></td><td>Compare renewable-energy shares</td></tr>
<tr><td>💰</td><td><strong>Energy vs GDP</strong></td><td>Explore energy and economic indicators</td></tr>
<tr><td>🔥</td><td><strong>Energy Mix</strong></td><td>Compare fossil and renewable shares</td></tr>
<tr><td>🔎</td><td><strong>Research Insight</strong></td><td>Surface key observations</td></tr>
<tr><td>📚</td><td><strong>Methodology</strong></td><td>Explain data and analytical assumptions</td></tr>
</tbody>
</table>

---

## 📷 Dashboard Preview

Run the dashboard locally:

```bash
streamlit run dashboard/app.py
```

Then open:

**http://localhost:8501**

> 💡 Add a screenshot of your Streamlit dashboard here later for a stronger GitHub presentation.

---

## 🌍 Data Source

The project uses the **Our World in Data Energy Dataset**.

### 🔗 Data & Documentation

- 🌍 [Our World in Data — Energy](https://ourworldindata.org/energy)
- 💻 [OWID Energy Data Repository](https://github.com/owid/energy-data)

The dataset aggregates energy information from sources including:

- Energy Institute
- International Energy Agency
- U.S. Energy Information Administration
- Ember
- Other international statistical sources

### 🔐 Dataset Snapshot

This project uses a downloaded snapshot of the OWID CSV.

The downloaded file is preserved locally and identified using a SHA-256 checksum for reproducibility.

```text
SHA-256:
266f2e2baad7975351bc9bb4aa061d22b1da9fe4c47d51d2ac6071e01e171f76
```

> 📌 The raw CSV is intentionally excluded from Git because of its size.

---

## 🔄 Data Pipeline

```text
📥 Download
     ↓
✅ Schema Validation
     ↓
💾 Raw Data Storage
     ↓
🌍 Country / Aggregate Classification
     ↓
🔢 Data Type Conversion
     ↓
🔍 Duplicate Detection
     ↓
❓ Missing Value Analysis
     ↓
📏 Range Validation
     ↓
🚩 Outlier Flagging
     ↓
🐘 PostgreSQL Loading
     ↓
📊 SQL Analytics
     ↓
⚡ Streamlit Dashboard
```

---

## 🧹 Data Cleaning & Validation

The project intentionally separates **data cleaning** from **data destruction**.

Questionable observations are flagged rather than blindly deleted.

### Cleaning Rules

> 📌 **Rendering note:** The analytical tables below use GitHub-compatible HTML table markup for consistent rendering across GitHub's README viewer.


<table>
<thead><tr><th>Check</th><th>Approach</th></tr></thead>
<tbody>
<tr><td>🌍 Country identification</td><td>Valid 3-letter ISO codes</td></tr>
<tr><td>🗂️ Aggregate entities</td><td>Stored separately</td></tr>
<tr><td>🔁 Duplicate <code>(country, year)</code></td><td>Checked and removed if present</td></tr>
<tr><td>🔢 Numeric parsing</td><td>Invalid values converted to missing</td></tr>
<tr><td>➖ Negative values</td><td>Flagged</td></tr>
<tr><td>📊 Percentage values</td><td>Checked for 0–100 range</td></tr>
<tr><td>❓ Missing values</td><td>Reported rather than automatically imputed</td></tr>
<tr><td>🚩 Outliers</td><td>IQR-based flags</td></tr>
<tr><td>📅 Sparse years</td><td>Reported for investigation</td></tr>
<tr><td>💾 Raw data</td><td>Preserved separately</td></tr>
</tbody>
</table>

### Validation Results

<table>
<thead><tr><th>Metric</th><th>Result</th></tr></thead>
<tbody>
<tr><td>🌍 Country rows after cleaning</td><td><strong>17,265</strong></td></tr>
<tr><td>🗂️ Aggregate / non-country rows</td><td><strong>6,112</strong></td></tr>
<tr><td>🔁 Duplicate country-year rows</td><td><strong>0</strong></td></tr>
<tr><td>➖ Negative-value violations</td><td><strong>0</strong></td></tr>
<tr><td>📊 Share-range violations</td><td><strong>0</strong></td></tr>
<tr><td>📅 Year range</td><td><strong>1900–2025</strong></td></tr>
</tbody>
</table>

> ⚠️ An outlier flag does **not** automatically mean that an observation is incorrect.

Energy datasets naturally contain large differences between countries because of population, economic size and resource availability.

---

## 🗄️ Database Design

The PostgreSQL database contains three primary tables:

### `raw_energy`

Stores the downloaded source data with minimal transformation.

### `clean_energy`

Stores validated country-level observations used for analysis.

### `aggregates`

Stores non-country and aggregate entities separately.

---

## 📐 Analytical SQL

The project uses SQL for:

- 📈 Renewable-energy comparisons
- ⚡ India energy trends
- 🌍 Energy vs GDP analysis
- 🛢️ Producer rankings
- 📊 Year-over-year changes

### SQL Techniques

```text
GROUP BY
ORDER BY
CASE WHEN
CTEs
Window Functions
RANK()
LAG()
Aggregation
Filtering
```

---

## 📈 Key Research Findings

### 🇮🇳 1. India's Energy Consumption Increased

India's primary energy consumption increased from:

<table>
<thead><tr><th>Year</th><th>Primary Energy</th></tr></thead>
<tbody>
<tr><td><strong>2017</strong></td><td>8,571.67</td></tr>
<tr><td><strong>2024</strong></td><td>11,336.06</td></tr>
</tbody>
</table>

📈 This represents an increase of approximately **32.3%**.

---

### 📊 2. India's Energy Growth Was Not Uniform

<table>
<thead><tr><th>Year</th><th>YoY Change</th></tr></thead>
<tbody>
<tr><td>2017</td><td>+3.74%</td></tr>
<tr><td>2018</td><td>+5.74%</td></tr>
<tr><td>2019</td><td>+2.41%</td></tr>
<tr><td>2020</td><td>🔻 <strong>−5.27%</strong></td></tr>
<tr><td>2021</td><td>🟢 <strong>+8.56%</strong></td></tr>
<tr><td>2022</td><td>+5.39%</td></tr>
<tr><td>2023</td><td>+7.64%</td></tr>
<tr><td>2024</td><td>+4.69%</td></tr>
</tbody>
</table>

The sharp decline in 2020 was followed by a strong rebound in 2021.

---

### 🌱 3. Renewable Share Increased

India's renewable share of energy increased from:

<table>
<thead><tr><th>Year</th><th>Renewable Share</th></tr></thead>
<tbody>
<tr><td><strong>2017</strong></td><td>6.79%</td></tr>
<tr><td><strong>2024</strong></td><td>9.15%</td></tr>
</tbody>
</table>

At the same time:

**2024 Fossil Share: 89.67%**

This highlights the coexistence of increasing renewable penetration with continued dependence on fossil energy.

---

## 🌎 International Comparison

Selected countries' renewable energy shares in 2024:

<table>
<thead><tr><th>Rank</th><th>Country</th><th>Renewable Share</th></tr></thead>
<tbody>
<tr><td>🥇 1</td><td>🇧🇷 Brazil</td><td><strong>49.62%</strong></td></tr>
<tr><td>🥈 2</td><td>🇨🇦 Canada</td><td><strong>27.16%</strong></td></tr>
<tr><td>🥉 3</td><td>🇩🇪 Germany</td><td><strong>23.97%</strong></td></tr>
<tr><td>4</td><td>🇬🇧 United Kingdom</td><td><strong>21.29%</strong></td></tr>
<tr><td>5</td><td>🇨🇳 China</td><td><strong>17.47%</strong></td></tr>
<tr><td>6</td><td>🇫🇷 France</td><td><strong>16.47%</strong></td></tr>
<tr><td>7</td><td>🇯🇵 Japan</td><td><strong>12.70%</strong></td></tr>
<tr><td>8</td><td>🇺🇸 United States</td><td><strong>12.05%</strong></td></tr>
<tr><td>9</td><td>🇮🇳 India</td><td><strong>9.15%</strong></td></tr>
<tr><td>10</td><td>🇷🇺 Russia</td><td><strong>6.00%</strong></td></tr>
</tbody>
</table>

> ℹ️ This comparison is descriptive and depends on the dataset's definitions and coverage.

---

## 💰 Energy & GDP Analysis

The dashboard compares:

- ⚡ Energy consumption per capita
- 💰 GDP per capita

for India.

The objective is to identify **patterns and relationships**, not to establish causality.

> ⚠️ Correlation between energy and economic indicators should not be interpreted as proof that one directly causes the other.

---

## 🔎 Data Quality Insights

The validation pipeline identified substantial missingness in several indicators.

<table>
<thead><tr><th>Indicator</th><th>Missing Values</th></tr></thead>
<tbody>
<tr><td>🌱 Renewable Share</td><td>12,806</td></tr>
<tr><td>🔥 Fossil Share</td><td>12,806</td></tr>
<tr><td>🌫️ Greenhouse Gas Emissions</td><td>11,878</td></tr>
<tr><td>⚡ Electricity Generation</td><td>10,688</td></tr>
<tr><td>💨 Wind Electricity</td><td>9,574</td></tr>
<tr><td>☀️ Solar Electricity</td><td>9,386</td></tr>
<tr><td>⚡ Primary Energy Consumption</td><td>6,910</td></tr>
<tr><td>💰 GDP</td><td>5,706</td></tr>
</tbody>
</table>

> 📌 This is important when interpreting cross-country or historical comparisons.

---

## 🧪 Testing

The project includes automated tests using **Pytest**.

### Test Result

```text
.... [100%]

4 passed in 0.34s
```

Run the tests:

```bash
python -m pytest -q
```

---

## 🛠️ Technology Stack

### 💻 Programming

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL">
</p>

### 📊 Data & Analytics

<p>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
</p>

### 📈 Visualization

<p>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
</p>

### 🐳 Infrastructure

<p>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose">
</p>

### 🧪 Testing

<p>
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
</p>

### 🔧 Development Tools

<p>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code">
</p>

---

## 📁 Project Structure

```text
energy-intelligence-dashboard/
│
├── 📂 data/
│   ├── 📂 raw/
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
├── 🔐 .env.example
├── 🚫 .gitignore
└── 📖 README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/harsh1223-bit/energy-intelligence-dashboard.git
cd energy-intelligence-dashboard
```

### 2️⃣ Create a Virtual Environment

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐳 Start PostgreSQL

Make sure Docker Desktop is running.

```bash
docker-compose up -d
```

Or:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

---

## ⚙️ Environment Configuration

Create your local `.env` file:

```bash
cp .env.example .env
```

Example configuration:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=energy
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

> 🔒 Never commit your real `.env` file or database credentials to GitHub.

---

## ▶️ Run the Data Pipeline

The easiest option:

```bash
./run.sh
```

Or manually:

```bash
python -m src.pipeline
```

The pipeline will:

1. 📥 Download the energy dataset
2. ✅ Validate the schema
3. 💾 Save the raw dataset
4. 🧹 Clean and classify observations
5. 📋 Generate validation reports
6. 🐘 Load data into PostgreSQL
7. 📐 Prepare analytical tables and views

---

## 📊 Run the Dashboard

```bash
streamlit run dashboard/app.py
```

Open:

```text
http://localhost:8501
```

---

## 🧮 Example SQL Analysis

Example: India's energy trend.

```sql
SELECT
    year,
    primary_energy_consumption,
    renewables_share_energy,
    fossil_share_energy
FROM clean_energy
WHERE country = 'India'
  AND entity_type = 'country'
ORDER BY year DESC;
```

---

## 📈 Example: Year-over-Year Growth

The project uses SQL window functions such as `LAG()`:

```sql
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
```

---

## 🔬 Research Methodology

```text
📥 Raw Data
     ↓
✅ Data Validation
     ↓
🧹 Data Cleaning
     ↓
🗄️ Database Modeling
     ↓
📊 SQL Analysis
     ↓
📈 Visualization
     ↓
🔬 Research Interpretation
```

The methodology emphasizes:

- 🔁 Reproducibility
- 🧹 Transparent cleaning
- 🔎 Data-quality reporting
- 🗄️ SQL-based analysis
- 📂 Separation of raw and processed data
- ❓ Explicit treatment of missing values
- 🚫 Avoidance of unsupported causal claims

---

## ⚠️ Limitations

### 1. 📅 Data Coverage

Historical coverage varies considerably across countries and indicators.

### 2. ❓ Missing Values

Several variables contain substantial missingness.

### 3. 🗓️ Latest-Year Coverage

The latest calendar year may not have complete country-level coverage.

For example, the 2025 data contains fewer country observations than many previous years.

### 4. 🚩 Outliers

Large values may represent legitimate differences in population, GDP or energy production rather than errors.

### 5. 🚫 No Causal Inference

The dashboard identifies trends and relationships but does not establish causality.

### 6. 🔄 Dataset Version

The project uses a specific downloaded snapshot of the OWID dataset. Results may change when the upstream dataset is updated.

---

## 🚧 Future Improvements

- [ ] ⏱️ Automated scheduled data ingestion
- [ ] 🌱 Add more energy sources
- [ ] 🛢️ Country-level energy production rankings
- [ ] 🌫️ CO₂ emissions analysis
- [ ] 📊 Energy intensity indicators
- [ ] 🔮 Forecasting models
- [ ] 🚨 Anomaly detection
- [ ] 🔔 Automated data-quality alerts
- [ ] 🔄 CI/CD with GitHub Actions
- [ ] ☁️ Public dashboard deployment
- [ ] ⚡ PostgreSQL indexing optimization
- [ ] 🗺️ Interactive map visualizations
- [ ] 📄 Downloadable analytical reports

---

## 🔁 Reproducibility

The project attempts to make analytical results reproducible by:

- 🔗 Recording the source URL
- 🕒 Recording the download timestamp
- 🔐 Recording a SHA-256 checksum
- 📂 Keeping raw and processed data separate
- 🧑‍💻 Version-controlling source code
- 🐳 Using Docker for PostgreSQL
- 🗄️ Providing SQL scripts
- 🧪 Providing automated tests
- 📋 Providing validation reports

### Dataset Metadata

```json
{
  "url": "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv",
  "file": "data/raw/owid-energy-data.csv",
  "sha256": "266f2e2baad7975351bc9bb4aa061d22b1da9fe4c47d51d2ac6071e01e171f76"
}
```

---

## 📚 References

- 🌍 [Our World in Data — Energy](https://ourworldindata.org/energy)
- 💻 [OWID Energy Data Repository](https://github.com/owid/energy-data)
- 🐍 [Python](https://www.python.org/)
- 🐼 [Pandas](https://pandas.pydata.org/)
- 🐘 [PostgreSQL](https://www.postgresql.org/)
- 📊 [Streamlit](https://streamlit.io/)
- 🐳 [Docker](https://www.docker.com/)
- 🧪 [Pytest](https://pytest.org/)

---

## 📜 Data Attribution

This project uses energy data provided through **Our World in Data** and its underlying sources.

The dataset and its licensing/attribution requirements should be reviewed before redistribution or commercial use.

This repository does **not** claim ownership of the underlying energy dataset.

---

# 👨‍💻 Author

## Harsh Sharma

🎓 **Integrated M.Tech in Computer Science**  
📊 **Specialization: Computational & Data Science**  
🏫 **VIT Bhopal**

<p align="left">
  <a href="https://github.com/harsh1223-bit">
    <img src="https://img.shields.io/badge/GitHub-harsh1223--bit-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

---

<p align="center">
  <strong>⚡ Built for Data Analytics, Energy Research & Decision Intelligence</strong>
</p>

<p align="center">
  ⭐ If you found this project useful, consider giving it a star!
</p>
