# filename: solar_panel_dashboard/models.py
from datetime import datetime

class FACT_SOLAR_OUTPUT:
    def __init__(self, OutputID, PanelID, Timestamp, EnergyOutput, WeatherConditionID, FailureID):
        self.OutputID = OutputID
        self.PanelID = PanelID
        self.Timestamp = Timestamp
        self.EnergyOutput = EnergyOutput
        self.WeatherConditionID = WeatherConditionID
        self.FailureID = FailureID

    def calculate_kpis(self):
        # Placeholder for KPI calculation logic
        # This method would contain the logic to calculate KPIs based on the attributes of the class
        pass

class DIM_PANEL:
    def __init__(self, PanelID, PanelType, InstallationDate, Location):
        self.PanelID = PanelID
        self.PanelType = PanelType
        self.InstallationDate = InstallationDate if isinstance(InstallationDate, datetime) else datetime.strptime(InstallationDate, '%Y-%m-%d')
        self.Location = Location

class DIM_WEATHER_CONDITION:
    def __init__(self, WeatherConditionID, Temperature, WindSpeed, Humidity, Irradiance):
        self.WeatherConditionID = WeatherConditionID
        self.Temperature = Temperature
        self.WindSpeed = WindSpeed
        self.Humidity = Humidity
        self.Irradiance = Irradiance

class DIM_FAILURE:
    def __init__(self, FailureID, FailureType, FailureDescription, FailureDate):
        self.FailureID = FailureID
        self.FailureType = FailureType
        self.FailureDescription = FailureDescription
        self.FailureDate = FailureDate if isinstance(FailureDate, datetime) else datetime.strptime(FailureDate, '%Y-%m-%d')