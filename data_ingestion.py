# filename: data_ingestion.py
import pandas as pd

class DataIngestion:
    def read_csv(self, file_path: str) -> pd.DataFrame:
        """
        Reads data from a CSV file and loads it into a pandas DataFrame.

        :param file_path: The path to the CSV file.
        :return: A pandas DataFrame containing the data.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")

# This is a simple test to ensure that the DataIngestion class is working correctly.
# In practice, this would be part of a separate test suite.
if __name__ == "__main__":
    ingestion = DataIngestion()
    df = ingestion.read_csv("~/Desktop/solar_sensors.csv")
    print(df.head())