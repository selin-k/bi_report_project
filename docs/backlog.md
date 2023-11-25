# Development Backlog Document for Solar Panel BI Dashboard ETL Pipeline

## PythonPackageName

solar_panel_dashboard

## DependenciesandTools

- ['pandas', 'For data loading and manipulation tasks such as data ingestion, curation, and transformation.']
- ['numpy', 'For numerical operations on data.']
- ['sqlalchemy', 'To interface with the database and perform SQL operations.']
- ['azure-storage-blob', 'To store and retrieve data from Azure Blob Storage.']
- ['azure-synapse-spark', 'To process data using Azure Synapse Analytics spark pools.']
- ['flask', 'To create the web application and API endpoints for microservices.']
- ['plotly', 'To create interactive visualizations for the BI dashboard.']
- ['dash', 'To build the interactive web-based dashboard that integrates with Plotly charts.']
- ['gunicorn', 'To serve the Flask application in a production environment.']

## RequiredPythonPackages

pandas==1.3.4
numpy==1.21.4
sqlalchemy==1.4.27
azure-storage-blob==12.9.0
azure-synapse-spark==0.1.0
flask==2.0.2
plotly==5.3.1
dash==2.0.0
gunicorn==20.1.0


## TaskList

- ['data_ingestion_service.py', 'Implements the DataIngestionService class. This class will handle reading data from the CSV file, validating the format, and ensuring data integrity. It will also support incremental data loads.']
- ['data_curation_service.py', 'Implements the DataCurationService class. This class will clean and prepare the ingested data, including handling missing values, deduplication, and schema validation.']
- ['data_transformation_service.py', 'Implements the DataTransformationService class. This class will apply business logic to calculate KPIs such as average energy output, performance comparison, and failure rates.']
- ['orchestration_service.py', 'Implements the OrchestrationService class. This class will manage the workflow of the ETL pipeline, schedule tasks, handle service dependencies, and provide monitoring and logging.']
- ['dashboard_app.py', 'Contains the logic for the BI dashboard application. It will use the processed data to provide real-time and historical visualizations using Plotly and Dash.']
- ['config.py', 'Contains configuration settings for the ETL pipeline, such as file paths, database connection strings, and API endpoint URLs.']
- ['requirements.txt', 'Lists all the necessary Python packages and their versions required for the project.']

## FullAPISpec

openapi: 3.0.0
info:
  title: "Solar Panel Data Services"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest data from the solar panel CSV data source"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                source_path:
                  type: string
      responses:
        '200':
          description: "Data ingestion successful"
  /curate:
    post:
      summary: "Curate ingested data"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                raw_data:
                  type: object
      responses:
        '200':
          description: "Data curation successful"
  /transform:
    post:
      summary: "Transform curated data into meaningful KPIs"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                curated_data:
                  type: object
      responses:
        '200':
          description: "Data transformation successful"


