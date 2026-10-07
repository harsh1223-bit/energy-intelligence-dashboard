import json
from .download_data import download_if_needed
from .config import RAW_FILE, REPORT_DIR
from .inspect_data import inspect_dataset
from .clean_data import load_raw, clean_dataset
from .validate_data import write_report
from .load_database import load_tables
from .db import create_views


def main():
    meta = download_if_needed()
    print('Pinned source:'); print(json.dumps(meta, indent=2))
    check = inspect_dataset(RAW_FILE)
    print('\nRequested-column inspection:')
    print(check.to_string(index=False))
    raw = load_raw(RAW_FILE)
    countries, aggregates, duplicate_count = clean_dataset(raw)
    metrics = write_report(countries, aggregates, duplicate_count)
    print(f"\nCountry rows: {len(countries):,}; aggregate rows: {len(aggregates):,}")
    print(f"Validation report: {REPORT_DIR / 'validation_report.md'}")
    load_tables(raw, countries, aggregates)
    create_views()
    print('Database tables and SQL views created.')
    print('\nNext: open the Streamlit dashboard. No analytical finding is printed here; use dashboard/SQL results for actual findings.')

if __name__ == '__main__': main()
