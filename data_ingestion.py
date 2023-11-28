# filename: data_ingestion.py

import pandas as pd

class DataIngestion:
    @staticmethod
    def read_csv(file_path: str) -> pd.DataFrame:
        """
        Reads a CSV file from the given file path and returns a pandas DataFrame.

        :param file_path: str - The path to the CSV file.
        :return: DataFrame - The data from the CSV file as a pandas DataFrame.
        :raises FileNotFoundError: If the CSV file is not found at the path.
        :raises Exception: If an error occurs while reading the CSV file.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError as e:
            # Log the error
            print(f"The file {file_path} was not found: {e}")
            # Re-raise the exception to be handled by the caller
            raise
        except Exception as e:
            # Log the error
            print(f"An error occurred while reading the file: {e}")
            # Re-raise the exception to be handled by the caller
            raise

# Example usage (commented out):
# ingestion = DataIngestion()
# try:
#     df = ingestion.read_csv("~/Desktop/solar_sensors.csv")
#     print(df.head())
# except Exception as e:
#     print(f"An error occurred: {e}")