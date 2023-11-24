# filename: solar_panel_monitoring/orchestration_service.py
from solar_panel_monitoring.data_ingestion_service import ingest_data
from solar_panel_monitoring.data_curation_service import curate_data
from solar_panel_monitoring.data_transformation_service import transform_data
from solar_panel_monitoring.data_visualization_service import visualize_data

def orchestrate_pipeline():
    """
    Orchestrate the execution of the microservices for the data pipeline.
    """
    # Ingest data from the CSV file
    ingest_data()

    # Curate the ingested data
    curate_data()

    # Transform the curated data into KPIs and performance metrics
    transform_data()

    # Generate visualizations for the BI Dashboard
    visualize_data()