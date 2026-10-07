import pandas as pd
from .config import RAW_FILE, REPORT_DIR, REQUESTED_COLUMNS


def inspect_dataset(path=RAW_FILE) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    rows = []
    for c in REQUESTED_COLUMNS:
        rows.append({
            'column': c,
            'present': c in df.columns,
            'dtype': str(df[c].dtype) if c in df.columns else '',
            'non_null': int(df[c].notna().sum()) if c in df.columns else 0,
            'missing_pct': round(float(df[c].isna().mean() * 100), 2) if c in df.columns else 100.0,
        })
    out = pd.DataFrame(rows)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(REPORT_DIR / 'data_dictionary_check.csv', index=False)
    return out

if __name__ == '__main__':
    result = inspect_dataset()
    print(result.to_string(index=False))
