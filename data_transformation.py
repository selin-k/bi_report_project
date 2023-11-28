# filename: data_transformation.py

import pandas as pd

class DataTransformation:
    @staticmethod
    def calculate_current_energy_output(data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates the current energy output for each solar panel.
        Assumes 'S1_Power_kwh' and 'S2_Power_kwh' are the columns for solar panel outputs.
        """
        if 'S1_Power_kwh' in data.columns and 'S2_Power_kwh' in data.columns:
            data['Current_Energy_Output'] = data['S1_Power_kwh'] + data['S2_Power_kwh']
        else:
            raise KeyError("Required columns for calculating energy output are missing.")
        return data

    @staticmethod
    def identify_underperforming_panels(data: pd.DataFrame, threshold: float) -> pd.DataFrame:
        """
        Identifies underperforming solar panels based on the threshold.
        """
        if 'Current_Energy_Output' not in data.columns:
            raise KeyError("Current_Energy_Output column is missing.")
        data['Underperforming'] = data['Current_Energy_Output'] < threshold
        return data

    @staticmethod
    def calculate_failure_rates(data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates the failure rates of solar panels based on 'PanelState'.
        """
        if 'PanelState' not in data.columns:
            raise KeyError("PanelState column is missing.")
        # Example logic: count 'failed' states as failures
        data['Failure'] = data['PanelState'] == 'failed'
        data['Failure_Rate'] = data['Failure'].rolling(window=30).mean()  # 30-day rolling average
        return data

    @staticmethod
    def populate_fact_table(data: pd.DataFrame) -> pd.DataFrame:
        """
        Populates the FACT_SOLAR_OUTPUT table with relevant data.
        """
        required_columns = ['OutputID', 'Timestamp', 'S1_Power_kwh', 'S2_Power_kwh',
                            'Light_kiloLux', 'Temp_degC', 'WeatherID', 'StateID',
                            'Current_Energy_Output', 'Underperforming', 'Failure_Rate']
        for column in required_columns:
            if column not in data.columns:
                raise KeyError(f"Required column {column} is missing for FACT_SOLAR_OUTPUT table.")
        fact_table = data[required_columns]
        return fact_table

    @staticmethod
    def populate_dimension_tables(data: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
        """
        Populates the DIM_WEATHER and DIM_PANEL_STATE tables with relevant data.
        """
        if 'WeatherID' not in data.columns or 'WeatherCondition' not in data.columns:
            raise KeyError("Required columns for DIM_WEATHER table are missing.")
        if 'StateID' not in data.columns or 'PanelState' not in data.columns:
            raise KeyError("Required columns for DIM_PANEL_STATE table are missing.")
        weather_table = data[['WeatherID', 'WeatherCondition']].drop_duplicates()
        panel_state_table = data[['StateID', 'PanelState']].drop_duplicates()
        return weather_table, panel_state_table

    @staticmethod
    def transform_data(data: pd.DataFrame, underperformance_threshold: float) -> dict:
        """
        Applies all transformation steps to the data and returns a dictionary of DataFrames.
        """
        data = DataTransformation.calculate_current_energy_output(data)
        data = DataTransformation.identify_underperforming_panels(data, underperformance_threshold)
        data = DataTransformation.calculate_failure_rates(data)
        fact_table = DataTransformation.populate_fact_table(data)
        weather_table, panel_state_table = DataTransformation.populate_dimension_tables(data)
        return {
            'fact_table': fact_table,
            'weather_table': weather_table,
            'panel_state_table': panel_state_table
        }

# Example usage (commented out):
# transformation = DataTransformation()
# df = pd.read_csv('path_to_csv_file')
# transformed_data = transformation.transform_data(df, underperformance_threshold=10)
# print(transformed_data['fact_table'].head())
# print(transformed_data['weather_table'].head())
# print(transformed_data['panel_state_table'].head())