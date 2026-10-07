-- 1) Business question: How quickly did each country's primary energy consumption change year over year?
DROP VIEW IF EXISTS vw_energy_yoy_growth CASCADE;
CREATE VIEW vw_energy_yoy_growth AS
SELECT
    country,
    iso_code,
    year,
    primary_energy_consumption,
    LAG(primary_energy_consumption) OVER (PARTITION BY country ORDER BY year) AS previous_year_energy,
    CASE
        WHEN LAG(primary_energy_consumption) OVER (PARTITION BY country ORDER BY year) > 0
        THEN 100.0 * (primary_energy_consumption - LAG(primary_energy_consumption) OVER (PARTITION BY country ORDER BY year))
             / LAG(primary_energy_consumption) OVER (PARTITION BY country ORDER BY year)
        ELSE NULL
    END AS yoy_growth_pct
FROM clean_energy
WHERE primary_energy_consumption IS NOT NULL;

-- 2) Business question: How has renewable energy's share changed in 10 selected countries?
DROP VIEW IF EXISTS vw_renewable_share_10_countries CASCADE;
CREATE VIEW vw_renewable_share_10_countries AS
SELECT country, iso_code, year, renewables_share_energy
FROM clean_energy
WHERE country IN ('India','China','United States','Russia','Japan','Germany','Brazil','Canada','United Kingdom','France')
  AND renewables_share_energy IS NOT NULL;

-- 3) Business question: What does the energy mix look like in the latest year with broad country coverage?
DROP VIEW IF EXISTS vw_latest_energy_mix CASCADE;
CREATE VIEW vw_latest_energy_mix AS
WITH latest AS (
    SELECT MAX(year) AS year
    FROM clean_energy
    WHERE primary_energy_consumption IS NOT NULL
      AND renewables_share_energy IS NOT NULL
      AND fossil_share_energy IS NOT NULL
    GROUP BY year
    HAVING COUNT(DISTINCT iso_code) >= 150
    ORDER BY year DESC
    LIMIT 1
)
SELECT
    c.country,
    c.iso_code,
    c.year,
    c.primary_energy_consumption,
    c.renewables_share_energy,
    c.fossil_share_energy,
    c.electricity_generation
FROM clean_energy c
JOIN latest l ON c.year = l.year
WHERE c.primary_energy_consumption IS NOT NULL;

-- 4) Business question:
-- Who are the top oil and gas producers, and how did their ranks change over 20 years?
DROP VIEW IF EXISTS vw_producer_rank_change CASCADE;

CREATE VIEW vw_producer_rank_change AS
WITH coverage AS (
    SELECT
        year,
        COUNT(*) FILTER (WHERE oil_production IS NOT NULL) AS oil_rows,
        COUNT(*) FILTER (WHERE gas_production IS NOT NULL) AS gas_rows
    FROM clean_energy
    WHERE entity_type = 'country'
    GROUP BY year
),
latest AS (
    SELECT MAX(year) AS latest_year
    FROM coverage
    WHERE oil_rows >= 100
      AND gas_rows >= 100
),
years AS (
    SELECT
        latest_year,
        latest_year - 20 AS old_year
    FROM latest
),
ranked AS (
    SELECT
        c.country,
        c.iso_code,
        c.year,
        c.oil_production,
        c.gas_production,

        RANK() OVER (
            PARTITION BY c.year
            ORDER BY c.oil_production DESC NULLS LAST
        ) AS oil_rank,

        RANK() OVER (
            PARTITION BY c.year
            ORDER BY c.gas_production DESC NULLS LAST
        ) AS gas_rank

    FROM clean_energy c
    CROSS JOIN years y

    WHERE c.entity_type = 'country'
      AND c.year IN (y.old_year, y.latest_year)
      AND (
          c.oil_production IS NOT NULL
          OR c.gas_production IS NOT NULL
      )
)
SELECT
    r.country,
    r.iso_code,
    r.year,
    r.oil_production,
    r.gas_production,
    r.oil_rank,
    r.gas_rank,
    y.old_year,
    y.latest_year,

    MAX(
        CASE
            WHEN r.year = y.old_year
            THEN r.oil_rank
        END
    ) OVER (PARTITION BY r.country) AS oil_rank_20y_ago,

    MAX(
        CASE
            WHEN r.year = y.latest_year
            THEN r.oil_rank
        END
    ) OVER (PARTITION BY r.country) AS oil_rank_latest,

    MAX(
        CASE
            WHEN r.year = y.old_year
            THEN r.gas_rank
        END
    ) OVER (PARTITION BY r.country) AS gas_rank_20y_ago,

    MAX(
        CASE
            WHEN r.year = y.latest_year
            THEN r.gas_rank
        END
    ) OVER (PARTITION BY r.country) AS gas_rank_latest

FROM ranked r
CROSS JOIN years y;
-- 5) Business question: How does energy consumption per person relate to GDP per person?
DROP VIEW IF EXISTS vw_energy_vs_gdp_per_capita CASCADE;
CREATE VIEW vw_energy_vs_gdp_per_capita AS
SELECT
    country,
    iso_code,
    year,
    population,
    gdp,
    primary_energy_consumption,
    energy_per_capita,
    CASE WHEN population > 0 THEN gdp / population ELSE NULL END AS gdp_per_capita
FROM clean_energy
WHERE population > 0
  AND gdp IS NOT NULL
  AND energy_per_capita IS NOT NULL;
