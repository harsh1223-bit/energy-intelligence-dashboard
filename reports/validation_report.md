# Energy data validation report

Generated from the downloaded OWID legacy CSV. This report contains observations/flags, not assumptions.

- Country rows after cleaning: **17265**
- Aggregate/non-country rows retained separately: **6112**
- Duplicate country-year rows removed during cleaning: **0**
- Year range: **1900–2025**

## Missing values by column

| Column | Missing rows | |
|---|---:|
| renewables_share_energy | 12806 |
| fossil_share_energy | 12806 |
| greenhouse_gas_emissions | 11878 |
| electricity_generation | 10688 |
| wind_electricity | 9574 |
| solar_electricity | 9386 |
| renewables_electricity | 9368 |
| energy_per_capita | 6967 |
| primary_energy_consumption | 6910 |
| gdp | 5706 |
| gas_production | 4023 |
| oil_production | 3477 |
| population | 153 |
| country | 0 |
| year | 0 |
| iso_code | 0 |
| entity_type | 0 |

## Negative-value flags

| Column | Negative rows |
|---|---:|

## Share violations (expected 0–100)

| Column | Violations |
|---|---:|
| renewables_share_energy | 0 |
| fossil_share_energy | 0 |

## IQR outlier flags

IQR flags identify observations far from the central distribution. They are **not automatically deleted** because large energy producers can be genuine extremes.

| Column | Flagged rows |
|---|---:|
| population | 2082 |
| gdp | 1537 |
| primary_energy_consumption | 1414 |
| energy_per_capita | 626 |
| electricity_generation | 933 |
| renewables_electricity | 1145 |
| solar_electricity | 1633 |
| wind_electricity | 1812 |
| renewables_share_energy | 240 |
| fossil_share_energy | 223 |
| oil_production | 2570 |
| gas_production | 2744 |
| greenhouse_gas_emissions | 810 |

## Year coverage

| Year | Country rows |
|---|---:|
| 1900 | 92 |
| 1901 | 92 |
| 1902 | 92 |
| 1903 | 92 |
| 1904 | 92 |
| 1905 | 92 |
| 1906 | 92 |
| 1907 | 92 |
| 1908 | 92 |
| 1909 | 92 |
| 1910 | 92 |
| 1911 | 92 |
| 1912 | 92 |
| 1913 | 92 |
| 1914 | 92 |
| 1915 | 92 |
| 1916 | 92 |
| 1917 | 92 |
| 1918 | 92 |
| 1919 | 92 |
| 1920 | 92 |
| 1921 | 92 |
| 1922 | 92 |
| 1923 | 92 |
| 1924 | 92 |
| 1925 | 92 |
| 1926 | 92 |
| 1927 | 92 |
| 1928 | 92 |
| 1929 | 92 |
| 1930 | 92 |
| 1931 | 92 |
| 1932 | 92 |
| 1933 | 92 |
| 1934 | 92 |
| 1935 | 92 |
| 1936 | 92 |
| 1937 | 92 |
| 1938 | 92 |
| 1939 | 92 |
| 1940 | 92 |
| 1941 | 92 |
| 1942 | 92 |
| 1943 | 92 |
| 1944 | 92 |
| 1945 | 92 |
| 1946 | 92 |
| 1947 | 92 |
| 1948 | 92 |
| 1949 | 92 |
| 1950 | 92 |
| 1951 | 92 |
| 1952 | 92 |
| 1953 | 92 |
| 1954 | 92 |
| 1955 | 92 |
| 1956 | 92 |
| 1957 | 92 |
| 1958 | 92 |
| 1959 | 92 |
| 1960 | 92 |
| 1961 | 92 |
| 1962 | 92 |
| 1963 | 92 |
| 1964 | 92 |
| 1965 | 107 |
| 1966 | 107 |
| 1967 | 107 |
| 1968 | 107 |
| 1969 | 107 |
| 1970 | 107 |
| 1971 | 107 |
| 1972 | 107 |
| 1973 | 107 |
| 1974 | 107 |
| 1975 | 107 |
| 1976 | 107 |
| 1977 | 107 |
| 1978 | 107 |
| 1979 | 107 |
| 1980 | 193 |
| 1981 | 193 |
| 1982 | 193 |
| 1983 | 193 |
| 1984 | 193 |
| 1985 | 203 |
| 1986 | 204 |
| 1987 | 204 |
| 1988 | 204 |
| 1989 | 204 |
| 1990 | 209 |
| 1991 | 209 |
| 1992 | 215 |
| 1993 | 215 |
| 1994 | 216 |
| 1995 | 216 |
| 1996 | 216 |
| 1997 | 217 |
| 1998 | 217 |
| 1999 | 217 |
| 2000 | 217 |
| 2001 | 217 |
| 2002 | 217 |
| 2003 | 218 |
| 2004 | 218 |
| 2005 | 219 |
| 2006 | 219 |
| 2007 | 219 |
| 2008 | 219 |
| 2009 | 219 |
| 2010 | 219 |
| 2011 | 219 |
| 2012 | 220 |
| 2013 | 220 |
| 2014 | 220 |
| 2015 | 220 |
| 2016 | 220 |
| 2017 | 220 |
| 2018 | 220 |
| 2019 | 220 |
| 2020 | 220 |
| 2021 | 220 |
| 2022 | 220 |
| 2023 | 220 |
| 2024 | 199 |
| 2025 | 90 |

## Sparse years
Years below the project coverage threshold are flagged for caution rather than globally dropped.

| Year | Rows |
|---|---:|
| 1900 | 92 |
| 1901 | 92 |
| 1902 | 92 |
| 1903 | 92 |
| 1904 | 92 |
| 1905 | 92 |
| 1906 | 92 |
| 1907 | 92 |
| 1908 | 92 |
| 1909 | 92 |
| 1910 | 92 |
| 1911 | 92 |
| 1912 | 92 |
| 1913 | 92 |
| 1914 | 92 |
| 1915 | 92 |
| 1916 | 92 |
| 1917 | 92 |
| 1918 | 92 |
| 1919 | 92 |
| 1920 | 92 |
| 1921 | 92 |
| 1922 | 92 |
| 1923 | 92 |
| 1924 | 92 |
| 1925 | 92 |
| 1926 | 92 |
| 1927 | 92 |
| 1928 | 92 |
| 1929 | 92 |
| 1930 | 92 |
| 1931 | 92 |
| 1932 | 92 |
| 1933 | 92 |
| 1934 | 92 |
| 1935 | 92 |
| 1936 | 92 |
| 1937 | 92 |
| 1938 | 92 |
| 1939 | 92 |
| 1940 | 92 |
| 1941 | 92 |
| 1942 | 92 |
| 1943 | 92 |
| 1944 | 92 |
| 1945 | 92 |
| 1946 | 92 |
| 1947 | 92 |
| 1948 | 92 |
| 1949 | 92 |
| 1950 | 92 |
| 1951 | 92 |
| 1952 | 92 |
| 1953 | 92 |
| 1954 | 92 |
| 1955 | 92 |
| 1956 | 92 |
| 1957 | 92 |
| 1958 | 92 |
| 1959 | 92 |
| 1960 | 92 |
| 1961 | 92 |
| 1962 | 92 |
| 1963 | 92 |
| 1964 | 92 |
| 1965 | 107 |
| 1966 | 107 |
| 1967 | 107 |
| 1968 | 107 |
| 1969 | 107 |
| 1970 | 107 |
| 1971 | 107 |
| 1972 | 107 |
| 1973 | 107 |
| 1974 | 107 |
| 1975 | 107 |
| 1976 | 107 |
| 1977 | 107 |
| 1978 | 107 |
| 1979 | 107 |
| 2025 | 90 |

## Cleaning decisions
1. Raw rows are retained in the raw table and are never hand-edited.
2. Rows with a valid three-letter uppercase ISO code are classified as countries; rows without one are treated as aggregates/non-country entities and stored separately.
3. Duplicate `(country, year)` rows are counted and the first occurrence is retained for the clean analysis table.
4. Numeric parsing errors become missing values and are visible in the missingness report.
5. Negative values and share violations are flagged; they are not silently deleted.
6. Sparse years are flagged because early historical coverage can be incomplete.

## Interpretation rule
A validation flag is a reason to inspect a value, not proof that the source value is wrong. OWID performs its own source-specific processing; this project adds a lightweight analyst QA layer.