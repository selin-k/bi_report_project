# filename: solar_panel_dashboard/config.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    # Configuration settings with default values or values from environment variables
    CSV_FILE_PATH = os.getenv('CSV_FILE_PATH', '/Users/selinkayay/appgenpro/data/solar_sensors.csv')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///solar_panel_dashboard.db')

# You can add more configuration settings as needed