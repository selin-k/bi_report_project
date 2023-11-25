# filename: solar_panel_dashboard/data_ingestion.py
import pandas as pd

class DataIngestion:
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a CSV file into a pandas DataFrame.

        :param file_path: The path to the CSV file.
        :return: A pandas DataFrame containing the loaded data.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("No data found in the file.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            raise
