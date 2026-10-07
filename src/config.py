from pathlib import Path
import os
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / '.env')
RAW_DIR = ROOT / 'data' / 'raw'
PROCESSED_DIR = ROOT / 'data' / 'processed'
REPORT_DIR = ROOT / 'reports'
RAW_FILE = RAW_DIR / 'owid-energy-data.csv'
METADATA_FILE = RAW_DIR / 'metadata.json'

DATA_URL = 'https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv'
REQUESTED_COLUMNS = [
    'country', 'year', 'iso_code', 'population', 'gdp',
    'primary_energy_consumption', 'energy_per_capita',
    'electricity_generation', 'renewables_electricity',
    'solar_electricity', 'wind_electricity', 'renewables_share_energy',
    'fossil_share_energy', 'oil_production', 'gas_production',
    'greenhouse_gas_emissions'
]
COUNTRIES = ['India', 'China', 'United States', 'Russia', 'Japan', 'Germany', 'Brazil', 'Canada', 'United Kingdom', 'France']

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://energy_user:energy_password@localhost:5432/energy_db')
