import pandas as pd
from sqlalchemy import create_engine, text
from .config import DATABASE_URL


def load_tables(raw_df, countries_df, aggregates_df):
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    with engine.begin() as conn:
        conn.execute(text('DROP TABLE IF EXISTS clean_energy CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS aggregates CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS raw_energy CASCADE'))
    raw_df.to_sql('raw_energy', engine, if_exists='replace', index=False, method='multi', chunksize=2000)
    countries_df.to_sql('clean_energy', engine, if_exists='replace', index=False, method='multi', chunksize=2000)
    aggregates_df.to_sql('aggregates', engine, if_exists='replace', index=False, method='multi', chunksize=2000)
    with engine.begin() as conn:
        conn.execute(text('CREATE INDEX IF NOT EXISTS idx_clean_country_year ON clean_energy(country, year)'))
        conn.execute(text('CREATE INDEX IF NOT EXISTS idx_clean_iso_year ON clean_energy(iso_code, year)'))
