# filename: solar_panel_monitoring/data_visualization_service.py
import plotly.express as px

def visualize_data(transformed_data):
    """
    Generate interactive visualizations for the BI Dashboard.

    :param transformed_data: The DataFrame containing the transformed solar sensor data.
    :return: Interactive visualizations.
    """
    # Generate a simple line chart as an example visualization
    # In a real-world scenario, we would create more complex and specific visualizations
    fig = px.line(transformed_data, x='Timestamp', y='EnergyProduced', title='Energy Output Over Time')

    # Show the figure
    # In a real-world scenario, we would return the figure or embed it in the BI Dashboard
    fig.show()

    print("Data visualization successful.")

# For testing purposes, we can create a sample DataFrame representing transformed data
# In a real-world scenario, the data would come from the data_transformation_service
# sample_transformed_data = pd.DataFrame({
#     'Timestamp': pd.date_range(start='1/1/2021', periods=5, freq='H'),
#     'EnergyProduced': [100, 105, 95, 120, 110]
# })
# visualize_data(sample_transformed_data)