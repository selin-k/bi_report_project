# filename: solar_panel_dashboard/data_curation.py
import pandas as pd

class DataCuration:
    def validate_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Validate the data by checking for missing or corrupt values.

        :param data: The pandas DataFrame to validate.
        :return: The validated pandas DataFrame.
        """
        # Check for missing values and handle them (e.g., fill with default values or drop)
        if data.isnull().values.any():
            # Here you can choose a strategy to handle missing values
            data = data.dropna()  # For example, dropping rows with missing values

        # Additional validation checks can be added here

        return data

    def normalize_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize the data to ensure consistency.

        :param data: The pandas DataFrame to normalize.
        :return: The normalized pandas DataFrame.
        """
        # Normalize data types, scale data, or perform other consistency checks
        # For example, ensure all numeric columns are of type float
        for column in data.select_dtypes(include=['int64']).columns:
            data[column] = data[column].astype(float)

        # Additional normalization steps can be added here

        return data