# filename: solar_panel_monitoring/data_transformation_service.py
import pandas as pd

def transform_data(curated_data):
    """
    Transform the curated data into KPIs and performance metrics.

    :param curated_data: The DataFrame containing the curated solar sensor data.
    :return: The transformed DataFrame ready for analysis and visualization.
    """
    # Apply business logic to calculate KPIs and performance metrics
    # For example, we could calculate the energy output efficiency for each solar panel
    # This is a placeholder for the actual business logic calculations
    # The actual implementation would depend on the specific KPIs and metrics required by the client
    transformed_data = curated_data  # Placeholder for actual transformation logic

    # Transform the data according to the logical semantic data model
    # This would involve populating the fact and dimension tables
    # For simplicity, we assume the transformed data is already in the correct format

    # Populate the fact and dimension tables
    # This is a placeholder for the actual code to populate the tables in the data warehouse
    # The specifics of this operation are not included here due to lack of actual environment details

    print("Data transformation successful.")
    return transformed_data

# For testing purposes, we can create a sample DataFrame representing curated data
# In a real-world scenario, the data would come from the data_curation_service
# sample_curated_data = pd.DataFrame({'PanelID': [1, 2, 3], 'EnergyProduced': [100, 150, 120]})
# transformed_data = transform_data(sample_curated_data)