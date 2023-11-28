# filename: data_curation.py

import pandas as pd

class DataCuration:
    # Define the data types as per the data model schema
    data_types = {
        'OutputID': 'int64',
        'Timestamp': 'datetime64[ns]',
        'S1_Power_kwh': 'float64',
        'S2_Power_kwh': 'float64',
        'Light_kiloLux': 'float64',
        'Temp_degC': 'float64',
        'WeatherID': 'int64',
        'StateID': 'int64'
    }

    @staticmethod
    def remove_duplicates(data: pd.DataFrame) -> pd.DataFrame:
        """
        Removes duplicate records from the DataFrame.

        :param data: DataFrame - The input data.
        :return: DataFrame - The data without duplicates.
        """
        return data.drop_duplicates()

    @classmethod
    def enforce_data_types(cls, data: pd.DataFrame) -> pd.DataFrame:
        """
        Enforces the data types of the DataFrame columns based on the data model.

        :param data: DataFrame - The input data.
        :return: DataFrame - The data with enforced data types.
        """
        for column, dtype in cls.data_types.items():
            if column in data.columns:
                try:
                    data[column] = data[column].astype(dtype)
                except ValueError as e:
                    raise ValueError(f"Column {column} cannot be cast to {dtype}: {e}")
        return data

    @classmethod
    def quality_checks(cls, data: pd.DataFrame) -> pd.DataFrame:
        """
        Performs quality checks on the data, including removing duplicates and enforcing data types.

        :param data: DataFrame - The input data.
        :return: DataFrame - The curated data.
        """
        data = cls.remove_duplicates(data)
        data = cls.enforce_data_types(data)
        # Future quality checks can be added here
        return data

# Example usage (commented out):
# curation = DataCuration()
# df = pd.read_csv('path_to_csv_file')
# try:
#     curated_df = curation.quality_checks(df)
#     print(curated_df.info())
# except ValueError as e:
#     print(f"Data curation error: {e}")