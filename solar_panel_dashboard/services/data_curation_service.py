# filename: solar_panel_dashboard/services/data_curation_service.py
import pandas as pd

class DataCurationService:
    def __init__(self, schema=None):
        """
        Constructor for the DataCurationService class.
        :param schema: A dictionary representing the expected schema for validation.
        """
        self.schema = schema

    def curate_data(self, raw_data: pd.DataFrame):
        """
        Cleans and prepares the ingested data for analysis.
        Handles missing values, deduplication, and schema validation.
        :param raw_data: The raw data as a pandas DataFrame.
        :return: A pandas DataFrame containing the curated data.
        """
        # Fill missing values with appropriate defaults or interpolations
        curated_data = raw_data.fillna(method='ffill').fillna(method='bfill')

        # Remove duplicates
        curated_data = curated_data.drop_duplicates()

        # Validate against the predefined schema
        if self.schema:
            self.validate_schema(curated_data)

        # Return the curated data
        return curated_data

    def validate_schema(self, data: pd.DataFrame):
        """
        Validates the data against a predefined schema.
        :param data: The data as a pandas DataFrame.
        :raises: ValueError if the schema does not match.
        """
        for column, expected_type in self.schema.items():
            if column not in data.columns or data[column].dtype != expected_type:
                raise ValueError(f"Column {column} does not match schema type {expected_type}")

# Example usage:
# Define the expected schema for the data
# schema = {'Column1': 'float64', 'Column2': 'int64', 'Column3': 'object'}
# curation_service = DataCurationService(schema)
# curated_data = curation_service.curate_data(raw_data)