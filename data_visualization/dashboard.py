# filename: data_visualization/dashboard.py
import streamlit as st
import matplotlib.pyplot as plt

def create_time_series_chart(data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Timestamp'], data['Total_Power_kwh'])
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Total Power (kWh)')
    plt.grid(True)
    return plt

def setup_dashboard(transformed_data):
    st.title('Solar Panel Performance Dashboard')

    # Time-series chart for total energy output
    st.subheader('Total Energy Output Over Time')
    time_series_chart = create_time_series_chart(transformed_data, 'Total Energy Output')
    st.pyplot(time_series_chart)

    # Additional visualizations can be added here

# Example usage:
# setup_dashboard(transformed_df)