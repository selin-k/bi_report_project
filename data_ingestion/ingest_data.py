# filename: data_ingestion/ingest_data.py
import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
from config_loader import load_config

def ingest_data():
    """
    Ingests data from CSV files into the raw data folder in Azure Data Lake Store.
    """
    # Load the configuration settings for data sources
    config = load_config()
    
    # Assuming we have a configuration for a local folder connector for simplicity
    local_folder_connector = config['datasources'][0]['connector']
    
    # Read the CSV file using pandas
    file_path = os.path.join(local_folder_connector['folder_path'], local_folder_connector['file_path'])
    data = pd.read_csv(file_path)
    
    # Connect to Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_STORAGE_CONNECTION_STRING'))
    blob_client = blob_service_client.get_blob_client(container='raw-data', blob='solar_data.csv')
    
    # Convert DataFrame to CSV and upload it to Azure Blob Storage
    blob_client.upload_blob(data.to_csv(index=False), overwrite=True)
    
    print("Data ingestion completed successfully.")
    return "raw-data/solar_data.csv"  # Simulated path for the ingested data

# This function call is for testing purposes only
if __name__ == "__main__":
    ingest_data()