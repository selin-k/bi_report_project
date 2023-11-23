# Development Backlog Document for Solar Panel KPIs BI Report

## PythonPackageName

solar_kpi_bi

## DependenciesandTools

- ['azure-synapse-analytics', 'For data warehousing and analytics.']
- ['azure-data-lake-storage', 'To store raw, curated, and conformed data in Azure Data Lake.']
- ['azure-kubernetes-service', 'For container orchestration of microservices.']
- ['azure-data-factory', 'To orchestrate and automate the data pipeline workflow.']
- ['powerbi-client', 'To create interactive dashboards and visualizations.']
- ['pandas', 'For data manipulation during the curation and transformation stages.']
- ['pyarrow', 'For handling parquet files during data curation.']
- ['azure-identity', 'To authenticate with Azure services.']
- ['requests', 'To make HTTP requests to IoT platform and MES if needed.']

## RequiredPythonPackages


azure-synapse-analytics==0.5.0
azure-data-lake-storage==12.3.2
azure-kubernetes-service==1.0.0
azure-data-factory==0.3.0
powerbi-client==1.0.0
pandas==1.3.4
pyarrow==5.0.0
azure-identity==1.6.1
requests==2.26.0


## TaskList

- ['data_ingestion/iot_platform_connector.py', "Implements the IoTPlatformConnector class for extracting data from the in-house IoT platform. This class will be used to ingest data into Azure Data Lake in a 'raw' format. The following functions will need to be implemented: connect(), fetch_data(), and store_raw_data()."]
- ['data_ingestion/mes_connector.py', "Implements the MESConnector class for extracting data from the manufacturing execution system (MES). This class will be used to ingest data into Azure Data Lake in a 'raw' format. The following functions will need to be implemented: connect(), fetch_data(), and store_raw_data()."]
- ['data_curation/curation_service.py', "Implements the DataCurationService class for deduplication, null value handling, and data normalization. The curated data will be mapped to the target schema and stored back into Azure Data Lake in a 'curated' folder. The following functions will need to be implemented: load_raw_data(), curate_data(), and store_curated_data()."]
- ['data_transformation/transformation_service.py', "Implements the DataTransformationService class for applying business logic to calculate the KPIs. It will transform the data into fact and dimension tables and store them in a 'conformed' folder. The following functions will need to be implemented: load_curated_data(), calculate_kpis(), and store_conformed_data()."]
- ['data_visualization/visualization_service.py', 'Implements the VisualizationService class for creating dashboards and visualizations using Power BI. The following functions will need to be implemented: load_conformed_data(), create_visualizations(), and publish_reports().']
- ['orchestration/orchestration_service.py', 'Implements the OrchestrationService class for managing the workflow of the data pipeline using Azure Data Factory. The following functions will need to be implemented: setup_pipeline(), run_pipeline(), and monitor_pipeline().']

## FullAPISpec


openapi: 3.0.0
info:
  title: "Solar Panel KPIs Data Pipeline API"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest data from IoT platform and MES"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                source:
                  type: string
                  description: "The data source to ingest from"
      responses:
        '200':
          description: "Data ingestion successful"
  /curate:
    post:
      summary: "Curate raw data"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                raw_data:
                  type: string
                  description: "Raw data to be curated"
      responses:
        '200':
          description: "Data curation successful"
  /transform:
    post:
      summary: "Transform curated data into KPIs"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                curated_data:
                  type: string
                  description: "Curated data to be transformed"
      responses:
        '200':
          description: "Data transformation successful"
  /visualize:
    post:
      summary: "Create visualizations from transformed data"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                conformed_data:
                  type: string
                  description: "Transformed data for visualization"
      responses:
        '200':
          description: "Data visualization successful"


## AnythingUnclear

We need to clarify the specifics of the KPIs to be calculated during the data transformation stage and the exact visualizations required for the BI report.

