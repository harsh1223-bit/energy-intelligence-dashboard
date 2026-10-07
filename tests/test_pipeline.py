import pandas as pd
from src.clean_data import classify_entity, clean_dataset
from src.validate_data import validation_metrics


def fake_rows():
    return pd.DataFrame([
        {'country':'India','year':2020,'iso_code':'IND','population':100,'gdp':1000,'primary_energy_consumption':50,'energy_per_capita':0.5,'renewables_electricity':10,'renewables_share_energy':20,'fossil_share_energy':80,'oil_production':1,'gas_production':2},
        {'country':'India','year':2021,'iso_code':'IND','population':101,'gdp':1100,'primary_energy_consumption':55,'energy_per_capita':0.54,'renewables_electricity':11,'renewables_share_energy':21,'fossil_share_energy':79,'oil_production':1,'gas_production':2},
        {'country':'World','year':2021,'iso_code':None,'population':1000,'gdp':10000,'primary_energy_consumption':500,'energy_per_capita':0.5,'renewables_electricity':100,'renewables_share_energy':20,'fossil_share_energy':80,'oil_production':10,'gas_production':20},
    ])


def test_classify_entity_separates_country_and_aggregate():
    out = classify_entity(fake_rows())
    assert out.loc[out.country == 'India', 'entity_type'].eq('country').all()
    assert out.loc[out.country == 'World', 'entity_type'].eq('aggregate').all()


def test_clean_dataset_returns_country_and_aggregate_tables():
    countries, aggregates, duplicate_count = clean_dataset(fake_rows())
    assert set(countries['country']) == {'India'}
    assert set(aggregates['country']) == {'World'}
    assert duplicate_count == 0


def test_validation_flags_negative_and_bad_share():
    df = fake_rows()
    df.loc[0, 'oil_production'] = -1
    df.loc[1, 'renewables_share_energy'] = 120
    m = validation_metrics(df)
    assert m['negative']['oil_production'] == 1
    assert m['share_violations']['renewables_share_energy'] == 1


def test_validation_counts_duplicate_country_year():
    df = fake_rows()
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    assert validation_metrics(df)['duplicates'] == 1

# These fixtures are intentionally fake. They test transformation logic only.
# All project findings must be computed from the real OWID download.
