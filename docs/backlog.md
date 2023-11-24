# Development Backlog Document for Solar Panel Performance Monitoring BI Dashboard

## PythonPackageName

solar_panel_monitoring

## DependenciesandTools

- ['pandas', 'For data loading and manipulation tasks such as data ingestion, curation, and transformation.']
- ['pyarrow', 'To support parquet file format operations during data curation.']
- ['azure-storage-blob', 'To interact with Azure Blob Storage for storing raw, curated, and conformed data.']
- ['azure-identity', 'To authenticate with Azure services.']
- ['azure-datafactory', 'To orchestrate the data pipeline workflows.']
- ['plotly', 'To create interactive visualizations for the dashboard.']
- ['dash', 'To build the interactive web-based dashboard.']
- ['pytest', 'For writing and running tests to ensure code quality.']

## RequiredPythonPackages

pandas==1.3.4
pyarrow==5.0.0
azure-storage-blob==12.9.0
azure-identity==1.7.0
azure-datafactory==0.0.1
plotly==5.5.0
dash==2.0.0
pytest==6.2.5


## TaskList

- ['setup/environment_setup.py', 'Sets up the development environment, including the installation of required Python packages and configuration of Azure services.']
- ['data_ingestion/ingest_data.py', "Implements the DataIngestion class to ingest data from CSV files and store it in the 'raw' data store in Azure Data Lake."]
- ['data_curation/curate_data.py', "Implements the DataCuration class to clean, deduplicate, and normalize raw data, and store it as a parquet table in the 'curated' folder within Azure Data Lake."]
- ['data_transformation/transform_data.py', "Implements the DataTransformation class to calculate KPIs and metrics, and store the results in the 'conformed' data store."]
- ['data_visualization/visualize_data.py', 'Implements the DataVisualization class to create interactive charts and graphs using Plotly and Dash for the BI Dashboard.']
- ['orchestration/orchestrate_pipeline.py', 'Implements the Orchestration class to manage the execution sequence of the microservices using Azure Data Factory.']
- ['tests/test_data_ingestion.py', 'Contains unit tests for the data ingestion process.']
- ['tests/test_data_curation.py', 'Contains unit tests for the data curation process.']
- ['tests/test_data_transformation.py', 'Contains unit tests for the data transformation process.']
- ['tests/test_data_visualization.py', 'Contains unit tests for the data visualization process.']

## FullAPISpec

openapi: 3.0.0
info:
  title: "Solar Panel Performance Monitoring API"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest data from CSV data source"
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
      summary: "Curate raw data"
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
      summary: "Transform curated data into actionable insights"
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
    get:
      summary: "Generate visualizations for the BI Dashboard"
      responses:
        '200':
          description: "Data visualization successful"
          content:
            text/html:
              schema:
                type: string


