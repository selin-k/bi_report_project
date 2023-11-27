# filename: orchestration/orchestration_service.py

class OrchestrationService:
    def __init__(self, data_ingestion_service, data_curation_service, data_transformation_service):
        self.data_ingestion_service = data_ingestion_service
        self.data_curation_service = data_curation_service
        self.data_transformation_service = data_transformation_service

    def orchestrate_etl(self):
        try:
            # Ingest data
            raw_data = self.data_ingestion_service.ingest_data()
            
            # Curate data
            curated_data = self.data_curation_service.curate_data(raw_data)
            
            # Transform data
            transformed_data = self.data_transformation_service.transform_data(curated_data)
            
            # The transformed data would then be passed to the visualization service
            # However, as per the design document, the visualization service is not implemented here
            # Instead, the transformed data will be made available for the BI tool to create visualizations
            
            return transformed_data
        except Exception as e:
            print(f"An error occurred during the ETL orchestration: {e}")
            raise

# Example usage:
# orchestration_service = OrchestrationService(data_ingestion_service, data_curation_service, data_transformation_service)
# transformed_data = orchestration_service.orchestrate_etl()