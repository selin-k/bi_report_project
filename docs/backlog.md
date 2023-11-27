# Development Backlog Document

## PythonPackageName

solar_bi_dashboard

## DependenciesandTools

- ['pandas', 'For data loading and manipulation tasks such as data ingestion, curation, and transformation.']
- ['sqlalchemy', 'To interface with the database and perform SQL operations.']
- ['matplotlib', 'For creating visualizations during the development phase.']
- ['streamlit', 'For creating the interactive BI dashboard.']
- ['numpy', 'For numerical operations on data.']
- ['pyyaml', 'To load the configuration file, config.yaml, into a singleton Config class for easy access.']

## RequiredPythonPackages

pandas==1.3.4
sqlalchemy==1.4.27
matplotlib==3.5.0
streamlit==1.2.0
numpy==1.21.4
PyYAML==6.0


## TaskList

- ['main.py', 'Contains the orchestration logic for creating the dashboard with curated data and metrics. It will call the necessary services in the correct order as defined in the program flow.']
- ['config/config.yaml', 'Contains the configuration for the data ingestion framework. The configurations include paths to data sources, database connection strings, and other necessary parameters.']
- ['config/config.py', 'Contains a singleton Config class that loads the config.yaml file for easy access throughout the framework.']
- ['data_ingest/data_ingestion.py', 'Implements the DataIngestion class for orchestrating the data ingestion process from the solar_sensors.csv file.']
- ['data_curate/data_curation.py', 'Contains the logic for applying data mappings to transform the raw data into a curated format. It will ensure data quality and prepare the data for transformation.']
- ['data_transformation/data_transformation.py', 'Contains the logic for transforming the curated data according to the logical data model provided, ensuring that the data is in the correct format for analysis within the BI dashboard.']
- ['data_visualization/dashboard.py', 'Contains the logic for setting up the interactive BI dashboard using Streamlit. It will include functions to create visualizations such as time-series graphs, heat maps, and bar charts.']
- ['data_models.py', 'Contains the data models such as the star schema, database tables etc. defined in the design document. The data models are used during data transformation to ensure the data is structured correctly for the BI tool.']
- ['orchestration/orchestration_service.py', 'Implements the OrchestrationService class that coordinates the execution of the microservices, handling scheduling, error handling, and recovery.']

## FullAPISpec

openapi: 3.0.0
info:
  title: "Solar Panel Performance BI Dashboard API"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest data from the solar_sensors.csv data source"
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
      summary: "Curate ingested data to ensure quality and prepare for transformation"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                data:
                  type: array
                  items:
                    type: object
      responses:
        '200':
          description: "Data curation successful"
  /transform:
    post:
      summary: "Transform curated data according to the logical data model"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                curated_data:
                  type: array
                  items:
                    type: object
      responses:
        '200':
          description: "Data transformation successful"
  /visualize:
    post:
      summary: "Generate visualizations for the BI dashboard"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                transformed_data:
                  type: array
                  items:
                    type: object
      responses:
        '200':
          description: "Visualization successful"

