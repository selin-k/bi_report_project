# Development Backlog Document for Solar Panel BI Dashboard

## PythonPackageName

solar_panel_dashboard

## DependenciesandTools

- ['pandas', 'For data loading and manipulation tasks such as data ingestion, curation, and transformation.']
- ['plotly', 'To create interactive visualizations for the dashboard.']
- ['flask', 'To serve the dashboard as a web application.']
- ['python-dotenv', 'To manage environment variables for configuration settings.']

## RequiredPythonPackages

pandas==1.3.4
plotly==5.5.0
flask==2.0.2
python-dotenv==0.19.2


## TaskList

- ['main.py', 'Contains the orchestration logic for the ETL pipeline and serves the dashboard. It will call the classes and methods in sequence as per the program flow defined in the technical design document.']
- ['data_ingestion.py', 'Implements the DataIngestion class for loading the solar sensor data from the CSV file. It will include a method load_data(file_path: str) that returns a pandas DataFrame.']
- ['data_curation.py', 'Implements the DataCuration class for validating and normalizing the ingested data. It will include methods validate_data(data: DataFrame) and normalize_data(data: DataFrame) that each return a pandas DataFrame.']
- ['data_transformation.py', 'Implements the DataTransformation class for applying business logic to calculate KPIs. It will include a method transform_data(data: DataFrame) that returns a pandas DataFrame.']
- ['data_visualization.py', 'Implements the DataVisualization class for generating interactive visualizations using Plotly. It will include a method generate_visuals(data: DataFrame) that does not return a value but generates the dashboard components.']
- ['models.py', 'Defines the classes FACT_SOLAR_OUTPUT, DIM_PANEL, DIM_WEATHER_CONDITION, and DIM_FAILURE that represent the fact and dimension tables. Each class will have attributes as per the class diagram and methods for any required calculations or data manipulations.']
- ['dashboard.py', 'Contains the Flask application to serve the dashboard. It will define routes for the dashboard and any necessary API endpoints for interaction.']
- ['config.py', 'Contains configuration settings for the application, such as file paths and database connection strings, which can be loaded from environment variables or a .env file.']

## FullAPISpec

openapi: 3.0.0
info:
  title: "Solar Panel Dashboard API"
  version: "1.0.0"
paths:
  /data/ingest:
    post:
      summary: "Ingest data from the solar_sensors.csv file"
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
  /data/curate:
    post:
      summary: "Validate and normalize ingested data"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                data:
                  type: object
                  additionalProperties: true
      responses:
        '200':
          description: "Data curation successful"
  /data/transform:
    post:
      summary: "Transform curated data into the data model"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                data:
                  type: object
                  additionalProperties: true
      responses:
        '200':
          description: "Data transformation successful"
  /visualize:
    get:
      summary: "Generate visualizations for the dashboard"
      responses:
        '200':
          description: "Visualizations generated successfully"


