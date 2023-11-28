# filename: orchestration.py

from data_ingestion import DataIngestion
from data_curation import DataCuration
from data_transformation import DataTransformation
from predictive_model import PredictiveModel
from data_visualization import DataVisualization

class Orchestration:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_visualization = DataVisualization()

    def coordinate_etl_process(self):
        try:
            # Ingest data
            raw_data = DataIngestion.read_csv(self.file_path)
            
            # Curate data
            curated_data = DataCuration.quality_checks(raw_data)
            
            # Transform data
            transformed_data = DataTransformation.transform_data(curated_data)
            
            # Feature engineering for predictive modeling
            features = PredictiveModel.perform_feature_engineering(transformed_data)
            target = transformed_data['Failure']  # Assuming 'Failure' is a binary column indicating panel failure
            
            # Train predictive model
            predictive_model = PredictiveModel()
            predictive_model.train_model(features, target)
            
            # Make predictions
            predictions = predictive_model.predict_failures(features)
            transformed_data['Predicted_Failure'] = predictions
            
            # Data visualization
            # Create visualizations and add them to the dashboard
            time_series_graph = self.data_visualization.create_time_series_graph(
                transformed_data, 'Timestamp', 'Current_Energy_Output', 'Energy Output Over Time'
            )
            self.data_visualization.add_visualization(time_series_graph, 'time-series-graph')
            
            # Additional visualizations can be added here
            
            # Run the dashboard
            self.data_visualization.run_dashboard()
        except Exception as e:
            print(f"An error occurred during the ETL process: {e}")

# Example usage (commented out):
# orchestrator = Orchestration('path_to_csv_file')
# orchestrator.coordinate_etl_process()