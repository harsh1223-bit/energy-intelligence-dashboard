from pathlib import Path
import pandas as pd
import numpy as np
from .config import REPORT_DIR

SHARE_COLUMNS = ['renewables_share_energy', 'fossil_share_energy']
KEY_COLUMNS = ['country', 'year']


def validation_metrics(df: pd.DataFrame) -> dict:
    numeric = df.select_dtypes(include=np.number).columns.tolist()
    missing_by_column = df.isna().sum().sort_values(ascending=False)
    missing_by_year = df.groupby('year').apply(lambda x: int(x.isna().all(axis=1).sum()), include_groups=False)
    duplicates = int(df.duplicated(KEY_COLUMNS).sum())
    negative = {c: int((df[c] < 0).sum()) for c in numeric if c not in ['year']}
    share_violations = {c: int(((df[c] < 0) | (df[c] > 100)).sum()) for c in SHARE_COLUMNS if c in df.columns}
    outliers = {}
    for c in numeric:
        if c == 'year':
            continue
        s = df[c].dropna()
        if len(s) < 8:
            outliers[c] = 0
            continue
        q1, q3 = s.quantile([0.25, 0.75]); iqr = q3 - q1
        if iqr == 0:
            outliers[c] = 0
        else:
            outliers[c] = int(((s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)).sum())
    coverage = df.groupby('year').size().sort_index()
    sparse_years = coverage[coverage < max(20, int(coverage.max() * 0.5))].to_dict() if not coverage.empty else {}
    return {
        'rows': len(df), 'columns': len(df.columns), 'missing_by_column': missing_by_column.to_dict(),
        'duplicates': duplicates, 'negative': negative, 'share_violations': share_violations,
        'outliers': outliers, 'year_coverage': coverage.to_dict(), 'sparse_years': sparse_years,
        'min_year': int(df.year.min()) if df.year.notna().any() else None,
        'max_year': int(df.year.max()) if df.year.notna().any() else None,
    }


def write_report(df: pd.DataFrame, aggregates: pd.DataFrame, duplicate_count: int, path: Path = REPORT_DIR / 'validation_report.md'):
    m = validation_metrics(df)
    lines = [
        '# Energy data validation report', '',
        'Generated from the downloaded OWID legacy CSV. This report contains observations/flags, not assumptions.', '',
        f"- Country rows after cleaning: **{m['rows']}**",
        f"- Aggregate/non-country rows retained separately: **{len(aggregates)}**",
        f"- Duplicate country-year rows removed during cleaning: **{duplicate_count}**",
        f"- Year range: **{m['min_year']}–{m['max_year']}**", '',
        '## Missing values by column', '', '| Column | Missing rows | |', '|---|---:|',
    ]
    for c, n in m['missing_by_column'].items(): lines.append(f'| {c} | {n} |')
    lines += ['', '## Negative-value flags', '', '| Column | Negative rows |', '|---|---:|']
    for c, n in m['negative'].items():
        if n: lines.append(f'| {c} | {n} |')
    lines += ['', '## Share violations (expected 0–100)', '', '| Column | Violations |', '|---|---:|']
    for c, n in m['share_violations'].items(): lines.append(f'| {c} | {n} |')
    lines += ['', '## IQR outlier flags', '', 'IQR flags identify observations far from the central distribution. They are **not automatically deleted** because large energy producers can be genuine extremes.', '', '| Column | Flagged rows |', '|---|---:|']
    for c, n in m['outliers'].items(): lines.append(f'| {c} | {n} |')
    lines += ['', '## Year coverage', '', '| Year | Country rows |', '|---|---:|']
    for y, n in m['year_coverage'].items(): lines.append(f'| {y} | {n} |')
    lines += ['', '## Sparse years', 'Years below the project coverage threshold are flagged for caution rather than globally dropped.', '', '| Year | Rows |', '|---|---:|']
    for y, n in m['sparse_years'].items(): lines.append(f'| {y} | {n} |')
    lines += ['', '## Cleaning decisions',
              '1. Raw rows are retained in the raw table and are never hand-edited.',
              '2. Rows with a valid three-letter uppercase ISO code are classified as countries; rows without one are treated as aggregates/non-country entities and stored separately.',
              '3. Duplicate `(country, year)` rows are counted and the first occurrence is retained for the clean analysis table.',
              '4. Numeric parsing errors become missing values and are visible in the missingness report.',
              '5. Negative values and share violations are flagged; they are not silently deleted.',
              '6. Sparse years are flagged because early historical coverage can be incomplete.', '',
              '## Interpretation rule',
              'A validation flag is a reason to inspect a value, not proof that the source value is wrong. OWID performs its own source-specific processing; this project adds a lightweight analyst QA layer.']
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines), encoding='utf-8')
    return m
