# filename: data_transformation/transform_data.py
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from azure.storage.blob import BlobServiceClient

def transform_data(curated_data_path):
    """
    Transforms curated data into a format suitable for BI analytics.
    """
    # Connect to Azure Blob Storage to retrieve the curated data
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_STORAGE_CONNECTION_STRING'))
    blob_client = blob_service_client.get_blob_client(container='curated-data', blob=curated_data_path)
    
    # Download the curated data as a stream
    curated_data_stream = blob_client.download_blob().readall()
    
    # Load the curated data into a DataFrame
    curated_data = pd.read_parquet(pd.io.common.BytesIO(curated_data_stream))
    
    # Perform transformation operations such as calculating KPIs and metrics
    # For simplicity, we'll assume the KPIs and metrics are already in the DataFrame
    # In a real-world scenario, we would perform the necessary calculations here
    
    # Convert the DataFrame to a Parquet table
    parquet_table = pa.Table.from_pandas(curated_data)
    
    # Upload the transformed data as a parquet file to Azure Blob Storage
    conformed_blob_client = blob_service_client.get_blob_client(container='conformed-data', blob='solar_data_conformed.parquet')
    conformed_blob_client.upload_blob(pq.write_table(parquet_table, where=pd.io.common.BytesIO()), overwrite=True)
    
    print("Data transformation completed successfully.")
    return "conformed-data/solar_data_conformed.parquet"  # Simulated path for the transformed data

# This function call is for testing purposes only
if __name__ == "__main__":
    transform_data('curated-data/solar_data_curated.parquet')