# filename: orchestration/orchestrate_pipeline.py
import sys
sys.path.append('..')  # Include the parent directory in the module search path

from data_ingestion.ingest_data import ingest_data
from data_curation.curate_data import curate_data
from data_transformation.transform_data import transform_data
from data_visualization.visualize_data import visualize_data

def orchestrate_pipeline():
    """
    Orchestrates the execution of the data pipeline.
    """
    try:
        # Ingest data
        raw_data_path = ingest_data()
        
        # Curate data
        curated_data_path = curate_data(raw_data_path)
        
        # Transform data
        conformed_data_path = transform_data(curated_data_path)
        
        # Visualize data
        visualize_data(conformed_data_path)
        
        print("Pipeline executed successfully.")
    except Exception as e:
        print(f"An error occurred during pipeline execution: {e}")

if __name__ == "__main__":
    # Run the orchestration as the main process
    orchestrate_pipeline()