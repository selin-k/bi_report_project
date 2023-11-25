# filename: solar_panel_dashboard/services/data_ingestion_service.py
import pandas as pd

class DataIngestionService:
    def __init__(self, expected_columns=None):
        """
        Constructor for the DataIngestionService class.
        :param expected_columns: A list of expected column names for validation.
        """
        self.expected_columns = expected_columns

    def ingest_data(self, source_path: str):
        """
        Reads data from the CSV file, validates the format, and ensures data integrity.
        Supports incremental data loads.
        :param source_path: The file path to the CSV data source.
        :return: A pandas DataFrame containing the ingested data.
        """
        try:
            # Read the CSV file into a pandas DataFrame
            data = pd.read_csv(source_path)
            
            # Perform basic validation checks
            if data.empty:
                raise ValueError("The CSV file is empty.")
            if self.expected_columns and list(data.columns) != self.expected_columns:
                raise ValueError("The CSV file does not have the expected columns.")
            
            # Additional integrity checks can be added here
            
            # Return the ingested data
            return data
        except Exception as e:
            # Handle any exceptions that occur during data ingestion
            print(f"An error occurred during data ingestion: {e}")
            raise

# Example usage:
# Define the expected columns for the CSV file
# expected_columns = ['Column1', 'Column2', 'Column3']
# ingestion_service = DataIngestionService(expected_columns)
# raw_data = ingestion_service.ingest_data('/path/to/solar_sensors.csv')