# filename: data_ingestion/mes_connector.py
import json
import requests
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

class MESConnector:
    def __init__(self, base_url, api_key, storage_account_name, storage_account_key):
        # Initialize connection parameters
        self.base_url = base_url
        self.api_key = api_key
        self.storage_account_name = storage_account_name
        self.storage_account_key = storage_account_key
        self.data_lake_service_client = self.authenticate_with_datalake()

    def authenticate_with_datalake(self):
        # Authenticate with Azure Data Lake using the storage account name and key
        try:
            credential = DefaultAzureCredential()
            service_client = DataLakeServiceClient(account_url=f"https://{self.storage_account_name}.dfs.core.windows.net",
                                                   credential=credential)
            return service_client
        except Exception as e:
            print(f"Authentication failed: {e}")
            return None

    def connect(self):
        # Placeholder method for establishing a connection to the MES
        print("Connecting to the MES...")

    def fetch_data(self):
        # Placeholder method for fetching data from the MES
        try:
            response = requests.get(f"{self.base_url}/data", headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()
            print("Data fetched successfully from MES.")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data from MES: {e}")
            return None

    def store_raw_data(self, data, filesystem_name, file_path):
        # Method for storing fetched data into Azure Data Lake in 'raw' format
        try:
            file_system_client = self.data_lake_service_client.get_file_system_client(filesystem=filesystem_name)
            file_client = file_system_client.get_file_client(file_path)
            file_client.create_file()
            # Serialize the JSON data to a string and encode to bytes
            data_bytes = json.dumps(data).encode('utf-8')
            file_client.append_data(data_bytes, 0, len(data_bytes))
            file_client.flush_data(len(data_bytes))
            print("Raw data from MES stored successfully.")
        except Exception as e:
            print(f"Failed to store raw data from MES: {e}")

# Example usage
if __name__ == "__main__":
    # These values should be configured in a secure manner, such as environment variables or a config file
    base_url = "http://mes-system-url/api"
    api_key = "your_api_key_here"
    storage_account_name = "your_storage_account_name"
    storage_account_key = "your_storage_account_key"

    connector = MESConnector(base_url, api_key, storage_account_name, storage_account_key)
    connector.connect()
    data = connector.fetch_data()
    if data:
        filesystem_name = "raw-datalake"
        file_path = "mes-data.json"
        connector.store_raw_data(data, filesystem_name, file_path)