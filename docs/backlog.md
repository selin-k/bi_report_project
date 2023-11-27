# Development Backlog Document for Solar Panel BI Dashboard

## PythonPackageName

solar_panel_dashboard

## DependenciesandTools

- ['pandas', 'For data loading and manipulation tasks such as data ingestion, curation, and transformation.']
- ['numpy', 'For numerical operations on data.']
- ['sqlalchemy', 'For database interactions.']
- ['flask', 'For creating the API endpoints for the microservices.']
- ['plotly', 'For creating interactive visualizations for the dashboard.']
- ['dash', 'For building the interactive web-based dashboard.']
- ['pytest', 'For writing and running tests to ensure code quality.']

## RequiredPythonPackages

pandas==1.3.4
numpy==1.21.4
sqlalchemy==1.4.27
flask==2.0.2
plotly==5.4.0
dash==2.0.0
pytest==6.2.5


## TaskList

- ['main.py', 'Contains the orchestration logic for creating the dashboard with curated data and metrics. It will initialize the Flask application and register the microservices as blueprints.']
- ['config/config.yaml', 'Contains the configuration for the data ingestion framework. The configurations include file paths, database connection strings, and other necessary parameters.']
- ['config/config.py', 'Contains a singleton Config class that loads the config.yaml file for easy access throughout the framework.']
- ['data_ingest/data_ingestion.py', 'Implements the DataIngestion class for orchestrating the data ingestion process from the solar_sensors.csv file.']
- ['data_curate/data_curation.py', 'Contains the logic for data curation tasks such as removing duplicates, handling missing values, and mapping source data to the target schema.']
- ['data_transformation/data_transformation.py', 'Contains the logic for applying business logic to calculate KPIs and transforming the curated data according to the logical data model.']
- ['data_visualization/dashboard.py', 'Contains the logic for loading transformed data into the BI tool and creating visualizations such as time series graphs, heat maps, and bar charts.']
- ['orchestration/orchestrator.py', 'Manages the workflow of the ETL pipeline, ensuring that data is ingested, curated, and transformed in a timely manner. Includes error logging and retry mechanisms.']

## FullAPISpec

openapi: 3.0.0
info:
  title: "Solar Panel Dashboard API"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest data from solar_sensors.csv data source"
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
      summary: "Curate ingested data"
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
      summary: "Transform curated data into KPIs and metrics"
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
      summary: "Load transformed data into BI tool and create visualizations"
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
          description: "Data visualization successful"


