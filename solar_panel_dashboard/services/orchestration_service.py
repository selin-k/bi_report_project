# filename: solar_panel_dashboard/services/orchestration_service.py
from solar_panel_dashboard.services.data_ingestion_service import DataIngestionService
from solar_panel_dashboard.services.data_curation_service import DataCurationService
from solar_panel_dashboard.services.data_transformation_service import DataTransformationService

class OrchestrationService:
    def __init__(self, source_path, schema, performance_threshold):
        """
        Constructor for the OrchestrationService class.
        :param source_path: The file path to the CSV data source.
        :param schema: The schema for data validation.
        :param performance_threshold: The threshold for identifying underperforming panels.
        """
        self.source_path = source_path
        self.schema = schema
        self.performance_threshold = performance_threshold

    def orchestrate_etl(self):
        """
        Manages the workflow of the ETL pipeline, schedules tasks, handles service dependencies,
        and provides monitoring and logging.
        """
        # Instantiate the services
        ingestion_service = DataIngestionService()
        curation_service = DataCurationService(self.schema)
        transformation_service = DataTransformationService(self.performance_threshold)

        # Run the ETL process
        try:
            raw_data = ingestion_service.ingest_data(self.source_path)
            curated_data = curation_service.curate_data(raw_data)
            transformed_data = transformation_service.transform_data(curated_data)
            print("ETL process completed successfully.")
            return transformed_data
        except Exception as e:
            print(f"An error occurred during the ETL process: {e}")
            raise

# Example usage:
# orchestration_service = OrchestrationService('/path/to/solar_sensors.csv', schema, performance_threshold)
# final_data = orchestration_service.orchestrate_etl()