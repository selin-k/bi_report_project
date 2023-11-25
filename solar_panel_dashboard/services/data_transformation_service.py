# filename: solar_panel_dashboard/services/data_transformation_service.py
import pandas as pd

class DataTransformationService:
    def __init__(self, performance_threshold):
        """
        Constructor for the DataTransformationService class.
        :param performance_threshold: The threshold for identifying underperforming panels.
        """
        self.performance_threshold = performance_threshold

    def transform_data(self, curated_data: pd.DataFrame):
        """
        Applies business logic to calculate KPIs such as average energy output,
        performance comparison, and failure rates.
        :param curated_data: The curated data as a pandas DataFrame.
        :return: A pandas DataFrame containing the transformed data.
        """
        # Calculate average energy output
        curated_data['average_energy_output'] = curated_data['energy_output'].mean()

        # Identify underperforming panels
        curated_data['is_underperforming'] = curated_data['energy_output'] < self.performance_threshold

        # Additional transformations can be added here

        # Return the transformed data
        return curated_data

# Example usage:
# Define the performance threshold for the panels
# performance_threshold = 100.0
# transformation_service = DataTransformationService(performance_threshold)
# transformed_data = transformation_service.transform_data(curated_data)