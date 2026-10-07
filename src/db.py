import argparse
from sqlalchemy import create_engine, text
from .config import DATABASE_URL, ROOT

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def execute_sql_file(path):
    sql = path.read_text(encoding='utf-8')
    with engine.begin() as conn:
        for statement in sql.split(';'):
            if statement.strip(): conn.execute(text(statement))


def create_views():
    execute_sql_file(ROOT / 'sql' / 'analytics.sql')

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--create-views', action='store_true'); args = p.parse_args()
    if args.create_views: create_views(); print('SQL views created.')
