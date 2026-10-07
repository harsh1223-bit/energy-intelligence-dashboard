import re
import pandas as pd
from .config import REQUESTED_COLUMNS, PROCESSED_DIR, COUNTRIES


def classify_entity(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    iso = out['iso_code'].astype('string').str.strip() if 'iso_code' in out else pd.Series(pd.NA, index=out.index, dtype='string')
    out['entity_type'] = iso.str.fullmatch(r'[A-Z]{3}', na=False).map({True: 'country', False: 'aggregate'}).fillna('aggregate')
    return out


def clean_dataset(df: pd.DataFrame):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    present = [c for c in REQUESTED_COLUMNS if c in df.columns]
    df = df[present].copy()
    df['country'] = df['country'].astype('string').str.strip()
    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    if 'iso_code' in df:
        df['iso_code'] = df['iso_code'].astype('string').str.strip().str.upper()
    for c in present:
        if c not in {'country', 'iso_code', 'year'}:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    df = classify_entity(df)
    duplicate_mask = df.duplicated(['country', 'year'], keep='first')
    duplicate_count = int(duplicate_mask.sum())
    df = df.loc[~duplicate_mask].copy()
    countries = df[df['entity_type'] == 'country'].copy()
    aggregates = df[df['entity_type'] == 'aggregate'].copy()
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    countries.to_csv(PROCESSED_DIR / 'clean_countries.csv', index=False)
    aggregates.to_csv(PROCESSED_DIR / 'aggregates.csv', index=False)
    return countries, aggregates, duplicate_count


def load_raw(path):
    return pd.read_csv(path, low_memory=False)
