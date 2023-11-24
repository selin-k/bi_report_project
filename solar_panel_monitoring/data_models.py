# filename: solar_panel_monitoring/data_models.py
from datetime import datetime

class FACT_ENERGY_OUTPUT:
    def __init__(self, EnergyOutputID, PanelID, Timestamp, EnergyProduced, WeatherConditionID):
        self.EnergyOutputID = EnergyOutputID
        self.PanelID = PanelID
        self.Timestamp = Timestamp
        self.EnergyProduced = EnergyProduced
        self.WeatherConditionID = WeatherConditionID

    # Placeholder for method to insert or update records in the data warehouse
    def save(self):
        pass

class FACT_PANEL_FAILURES:
    def __init__(self, PanelFailureID, PanelID, FailureTimestamp, FailureTypeID, IsResolved):
        self.PanelFailureID = PanelFailureID
        self.PanelID = PanelID
        self.FailureTimestamp = FailureTimestamp
        self.FailureTypeID = FailureTypeID
        self.IsResolved = IsResolved

    # Placeholder for method to insert or update records in the data warehouse
    def save(self):
        pass

class DIM_PANEL:
    def __init__(self, PanelID, PanelType, InstallationDate, Capacity, LocationID):
        self.PanelID = PanelID
        self.PanelType = PanelType
        self.InstallationDate = InstallationDate
        self.Capacity = Capacity
        self.LocationID = LocationID

    # Placeholder for method to insert or update records in the data warehouse
    def save(self):
        pass

class DIM_WEATHER_CONDITION:
    def __init__(self, WeatherConditionID, Temperature, SunlightIntensity, WeatherDescription):
        self.WeatherConditionID = WeatherConditionID
        self.Temperature = Temperature
        self.SunlightIntensity = SunlightIntensity
        self.WeatherDescription = WeatherDescription

    # Placeholder for method to insert or update records in the data warehouse
    def save(self):
        pass

class DIM_FAILURE_TYPE:
    def __init__(self, FailureTypeID, FailureDescription, PotentialCause):
        self.FailureTypeID = FailureTypeID
        self.FailureDescription = FailureDescription
        self.PotentialCause = PotentialCause

    # Placeholder for method to insert or update records in the data warehouse
    def save(self):
        pass

class DIM_LOCATION:
    def __init__(self, LocationID, Country, Region, GPS_Coordinates):
        self.LocationID = LocationID
        self.Country = Country
        self.Region = Region
        self.GPS_Coordinates = GPS_Coordinates

    # Placeholder for method to insert or update records in the data warehouse
    def save(self):
        pass