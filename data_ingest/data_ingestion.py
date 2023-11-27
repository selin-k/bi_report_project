# filename: data_ingest/data_ingestion.py
import pandas as pd

class DataIngestionService:
    def __init__(self, config):
        self.config = config
        # Assuming the first datasource in the list is the one we want to use
        self.data_source_path = self.config.get('datasources')[0]['connector']['folder_path']

    def ingest_data(self):
        try:
            # Read the CSV file into a DataFrame
            data = pd.read_csv(self.data_source_path)
            return data
        except Exception as e:
            print(f"An error occurred during data ingestion: {e}")
            raise

# Example usage:
# config = Config()
# data_ingestion_service = DataIngestionService(config)
# df = data_ingestion_service.ingest_data()