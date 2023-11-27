# filename: main.py
import streamlit as st
from data_ingest.data_ingestion import DataIngestionService
from data_curate.data_curation import DataCurationService
from data_transformation.data_transformation import DataTransformationService
from data_visualization.dashboard import setup_dashboard
from orchestration.orchestration_service import OrchestrationService
from config.config import Config

# Load the configuration
config = Config()

# Initialize services
data_ingestion_service = DataIngestionService(config)
data_curation_service = DataCurationService(config)
data_transformation_service = DataTransformationService(config)
orchestration_service = OrchestrationService(
    data_ingestion_service,
    data_curation_service,
    data_transformation_service
)

def main():
    # Orchestrate the ETL process
    orchestration_service.orchestrate_etl()
    
    # Set up the Streamlit dashboard
    setup_dashboard()

if __name__ == "__main__":
    main()