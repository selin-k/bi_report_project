# filename: solar_panel_monitoring/data_curation_service.py
import pandas as pd

def curate_data(data):
    """
    Curate the ingested data by handling missing values and inconsistencies.

    :param data: The DataFrame containing the ingested solar sensor data.
    :return: The curated DataFrame.
    """
    # Check for missing values and apply imputation methods
    # For example, we could fill missing values with the mean or median
    if data.isnull().values.any():
        data = data.fillna(data.mean())

    # Normalize the data to ensure consistency
    # This could involve scaling numerical features or encoding categorical variables
    # For simplicity, we assume all data is numerical and scale it to a range of 0 to 1
    data = (data - data.min()) / (data.max() - data.min())

    print("Data curation successful.")
    return data

# For testing purposes, we can create a sample DataFrame with missing values
# In a real-world scenario, the data would come from the data_ingestion_service
# sample_data = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
# curated_data = curate_data(sample_data)