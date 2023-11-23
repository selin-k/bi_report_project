# Development Backlog Document for Solar Panel Performance BI Dashboard

## PythonPackageName

solar_panel_dashboard

## DependenciesandTools

- ['pandas', 'For data manipulation during the curation and transformation stages.']
- ['pyarrow', 'For efficient serialization of data frames to parquet format.']
- ['powerbi-api', 'To programmatically push data to Power BI for visualization.']
- ['azure-identity', 'To authenticate and manage credentials securely.']
- ['azure-storage-blob', 'To interact with Azure Blob Storage for data ingestion and storage.']
- ['azure-synapse-spark', 'To perform data transformation and analytics within Azure Synapse Analytics.']
- ['azure-data-factory', 'To orchestrate the data pipeline and manage microservices execution.']
- ['PyYAML', 'To parse YAML configuration files.']

## RequiredPythonPackages


azure-storage-blob==12.9.0
azure-synapse-spark==0.1.0
azure-data-factory==0.1.0
pandas==1.3.4
pyarrow==5.0.0
powerbi-api==1.0.0
azure-identity==1.6.1
PyYAML==5.4.1


## TaskList

- ['data_ingestion/ingest_data.py', "Implements the data ingestion logic. It should be able to read CSV files from the local file system or Azure Data Lake Store, depending on the configuration. The ingested data will be stored in a 'raw' data folder within Azure Data Lake Store, partitioned by ingestion date."]
- ['data_curation/curate_data.py', "Responsible for loading raw data, performing data cleaning such as deduplication and null value imputation, and mapping source data to the target schema. The curated data will be stored as parquet files in a 'curated' folder in Azure Data Lake Store."]
- ['data_transformation/transform_data.py', "Handles the transformation of curated data into a format suitable for BI analytics, calculating KPIs and metrics as per business logic aligned with IEC61970 standards. The transformed data will be stored in a 'conformed' folder within Azure Data Lake Store."]
- ['data_visualization/visualize_data.py', 'Utilizes the conformed data to generate visualizations using Power BI or Tableau. It will create interactive dashboards displaying energy production trends, performance comparisons, and predictive analytics for solar panel failures.']
- ['orchestration/orchestrate_pipeline.py', 'Manages the orchestration of the data pipeline using Azure Data Factory. It will schedule the pipeline to run daily and include error handling and logging mechanisms.']
- ['config/config.yaml', 'Contains the configuration settings for the data sources to be ingested. This file will be used by the data_ingestion microservice to pull the data source information.']
- ['data_ingestion/config_loader.py', 'Implements the logic to load and parse the config.yaml file. This will provide the data_ingestion microservice with the necessary configurations for data sources.']

## FullAPISpec


openapi: 3.0.0
info:
  title: "Solar Panel Performance Data Services"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest solar sensor data from CSV files into the raw data folder."
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                file_path:
                  type: string
      responses:
        '200':
          description: "Data ingestion successful"
  /curate:
    post:
      summary: "Curate raw data by cleaning and mapping to target schema."
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                raw_data_path:
                  type: string
      responses:
        '200':
          description: "Data curation successful"
  /transform:
    post:
      summary: "Transform curated data into BI-ready format."
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                curated_data_path:
                  type: string
      responses:
        '200':
          description: "Data transformation successful"
  /visualize:
    post:
      summary: "Generate visualizations for the BI dashboard."
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                conformed_data_path:
                  type: string
      responses:
        '200':
          description: "Data visualization successful"


## AnythingUnclear

We need to clarify the specifics of the predictive analytics model for solar panel failures, including the data points required and the expected output format for integration with the BI dashboard.

