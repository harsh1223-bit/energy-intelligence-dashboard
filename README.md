# Energy Data Pipeline and Dashboard

Small, reproducible energy-data project for an Analyst (Data & Research) interview.

## Scope
- Source: Our World in Data legacy energy dataset, pinned to the exact CSV downloaded by `src/download_data.py`.
- Main focus: India, with comparisons against 9 other countries.
- Stack: Python/pandas, PostgreSQL, SQL, Streamlit, Plotly, pytest, Docker Compose.
- No cloud deployment.

## Important source note
OWID states that the legacy energy dataset is **no longer updated** and recommends the newer release. This project deliberately uses the legacy URL requested for reproducibility. The pipeline records the download UTC timestamp and SHA-256 checksum in `data/raw/metadata.json` so a run can be reproduced against the same downloaded file.

OWID also says to cite both OWID and the underlying data sources, and warns that third-party data may have separate license terms. **Check the license in the OWID repository README before publishing this project or redistributing the downloaded data.**

Primary source: https://github.com/owid/energy-data
Legacy CSV requested for this project: https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv

Underlying sources represented in the OWID legacy release include the Energy Institute Statistical Review of World Energy, U.S. EIA international energy data, and Ember electricity data.

## Design decisions
1. `raw_energy` keeps the downloaded dataset with minimal transformation.
2. `clean_energy` contains rows classified as real countries using a conservative rule: a non-null three-letter uppercase ISO code. Rows without ISO codes are treated as aggregates/non-country entities. The raw dataset remains untouched.
3. `aggregates` stores the excluded aggregate rows for auditability.
4. Numeric columns are coerced to numeric. Negative values are flagged rather than blindly deleted because zero/negative values can be meaningful for some metrics; the validation report identifies them.
5. Shares are expected to be between 0 and 100 and are flagged when outside that range.
6. Duplicate `(country, year)` records are reported. The pipeline keeps the first occurrence only after recording the duplicate count.
7. Sparse years are reported rather than dropped globally. Analytics choose years based on field availability.
8. The project uses the actual legacy file at runtime; no data is hand-edited.

## Quick start on macOS
Prerequisites: Docker Desktop and Python 3.12+.

```bash
cd energy_data_pipeline
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./run.sh
```

`run.sh`:
1. starts PostgreSQL with Docker Compose;
2. waits for PostgreSQL;
3. downloads the exact CSV if it is not already present;
4. records checksum/download metadata;
5. inspects the available columns;
6. cleans and validates the data;
7. loads raw, clean and aggregate tables;
8. creates SQL views;
9. prints a validation summary;
10. launches Streamlit.

Open the Streamlit URL shown by the command, normally `http://localhost:8501`.

## Re-running
If `data/raw/owid-energy-data.csv` already exists, the pipeline reuses it and does not silently replace it. Delete that file only when you intentionally want a new pinned download. The new checksum and timestamp will then be recorded.

To stop PostgreSQL:
```bash
docker compose down
```

To remove the database volume too:
```bash
docker compose down -v
```

## Project structure
```text
energy_data_pipeline/
├── dashboard/app.py
├── data/raw/                 # downloaded source; not committed to Git
├── data/processed/
├── reports/
├── sql/analytics.sql
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── download_data.py
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── db.py
│   ├── load_database.py
│   └── pipeline.py
├── tests/test_pipeline.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── run.sh
└── README.md
```

## Actual usable columns
The pipeline checks the downloaded file rather than assuming every requested column exists. The requested analytical set is:
- `country`, `year`, `iso_code`
- `population`, `gdp`
- `primary_energy_consumption`, `energy_per_capita`
- `electricity_generation`
- `renewables_electricity`, `solar_electricity`, `wind_electricity`
- `renewables_share_energy`, `fossil_share_energy`
- `oil_production`, `gas_production`
- `greenhouse_gas_emissions`

At runtime, `inspect_data.py` writes `reports/data_dictionary_check.csv`, showing which of these columns are actually present, their dtype, non-null count and missing percentage. Do not claim a column is usable until that report is generated from the downloaded file.

## Validation report
`reports/validation_report.md` is generated from the real CSV. It includes:
- missing values by column;
- missingness by year;
- duplicate country-year keys;
- negative numeric values;
- shares outside 0–100;
- basic IQR-based outlier flags;
- sparse-year coverage;
- rows dropped/kept/flagged and why.

This is an audit report, not a claim that every statistical anomaly is an error.

## SQL business questions
See `sql/analytics.sql`. The views cover:
1. Year-on-year primary energy consumption growth by country — uses `LAG()`.
2. Renewable-share trend for 10 selected countries.
3. Energy mix in the latest year with good coverage.
4. Top 10 oil and gas producers and rank change across a 20-year window — uses `RANK()`.
5. Energy-per-capita vs GDP-per-capita style comparison.

## Tests
`tests/test_pipeline.py` uses tiny **fake rows** only to test functions. The fixtures are not analysis results. All actual findings must come from the downloaded OWID data.

## What to say in an interview
You can explain the architecture as:
`download -> pin/checksum -> inspect -> clean/validate -> PostgreSQL raw+clean tables -> SQL views -> Streamlit dashboard`.

Be explicit that the raw layer is retained for traceability, the clean layer is analysis-ready, validation is separate from cleaning, and SQL is used for business questions rather than doing everything in pandas.

## Limitations
- The source is the legacy OWID release and is no longer updated.
- OWID indicators are compiled/processed from multiple sources; units and methodologies should be read from OWID's codebook.
- Simple range/outlier checks are flags, not proof of erroneous observations.
- The dashboard is local only.
- This project does not establish causal relationships.

## Publishing
Before publishing the downloaded dataset, verify the current OWID repository README and all applicable third-party source licenses. Credit OWID and the underlying sources as required.
