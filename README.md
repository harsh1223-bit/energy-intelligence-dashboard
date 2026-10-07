# ⚡ Energy Intelligence Dashboard

An India-focused energy data and research analytics project that builds a reproducible pipeline from raw energy data to an interactive dashboard.

The project downloads the Our World in Data (OWID) energy dataset, performs data cleaning and quality checks with Python/pandas, loads the results into PostgreSQL, creates analytical SQL views, and presents key energy trends through a Streamlit dashboard.

Built as a portfolio project for a **Data & Research Analyst** role.

> **Status:** Local portfolio project. Not deployed or real-time.

---

## Overview

The project follows an end-to-end data analytics workflow:

```text
OWID Energy Dataset
        │
        ▼
   Data Ingestion
        │
        ▼
 Python / Pandas
 Cleaning + Validation
        │
        ▼
    PostgreSQL
 Raw + Clean Tables
        │
        ▼
   SQL Analytics
        │
        ▼
 Streamlit Dashboard