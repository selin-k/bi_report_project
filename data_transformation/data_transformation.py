# filename: data_transformation/data_transformation.py
import pandas as pd

class DataTransformationService:
    def __init__(self, config):
        self.config = config

    def transform_data(self, curated_data):
        try:
            # Apply business logic to calculate KPIs such as 'Total Energy Output', 'Panel Efficiency', and 'Failure Rate'
            # For simplicity, let's assume we're calculating 'Total Energy Output' as the sum of all power columns
            if 'S1_Power(kwh)' in curated_data.columns and 'S2_Power(kwh)' in curated_data.columns:
                curated_data['Total_Power_kwh'] = curated_data['S1_Power(kwh)'] + curated_data['S2_Power(kwh)']
            
            # Additional transformation steps can be added here to align with the logical data model
            
            return curated_data
        except Exception as e:
            print(f"An error occurred during data transformation: {e}")
            raise

# Example usage:
# config = Config()
# data_transformation_service = DataTransformationService(config)
# transformed_df = data_transformation_service.transform_data(curated_df)