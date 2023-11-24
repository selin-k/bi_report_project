# Development Backlog Document for Solar Panel Performance Monitoring BI Dashboard

## PythonPackageName

```python
solar_panel_monitoring
```

## DependenciesandTools

- ['azure-synapse-analytics', 'For data warehousing and big data analytics.']
- ['azure-kubernetes-service', 'For deploying containerized microservices.']
- ['python-dotenv', 'To manage environment variables for configuration.']
- ['requests', 'To make HTTP requests between microservices.']
- ['pandas', 'For data manipulation and analysis.']
- ['numpy', 'For numerical operations on data.']
- ['plotly', 'For creating interactive visualizations.']
- ['powerbi-embedded', 'For embedding Power BI visualizations.']
- ['azure-data-factory', 'For orchestrating and automating data flows.']

## RequiredPythonPackages

azure-synapse-analytics==0.5.0
azure-kubernetes-service==1.0.0
python-dotenv==0.19.2
requests==2.26.0
pandas==1.3.4
numpy==1.21.4
plotly==5.3.1
powerbi-embedded==1.1.0
azure-data-factory==0.3.0


## TaskList

- ['main.py', 'Serves as the entry point for the program. Orchestrates the flow of the program according to the sequence diagram in the technical design document.']
- ['config.yaml', 'Contains all the data source configuration information required by the data_ingestion service.']
- ['data_ingestion_service.py', 'Create a microservice for ingesting data from CSV files into Azure Synapse Analytics. Include CSV validation and schema checks.']
- ['data_curation_service.py', 'Develop a microservice to handle data quality issues such as missing values and inconsistencies. Implement imputation and normalization methods.']
- ['data_transformation_service.py', 'Build a microservice to apply business logic to curated data, calculate KPIs, and populate fact and dimension tables in the conformed data store.']
- ['data_visualization_service.py', 'Implement a microservice to retrieve conformed data and generate interactive visualizations using Plotly or Power BI Embedded.']
- ['orchestration_service.py', 'Set up the orchestration layer using Azure Data Factory to coordinate the execution of microservices and manage data flow.']
- ['data_models.py', 'Define all the table structures and related functions for the FACT and DIM tables.']

## FullAPISpec

```python
openapi: 3.0.0
info:
  title: "Solar Panel Performance Monitoring API"
  version: "1.0.0"
paths:
  /ingest_data:
    post:
      summary: "Ingest solar sensor data"
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
  /curate_data:
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
  /transform_data:
    post:
      summary: "Transform curated data into KPIs and performance metrics"
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
          description: "Data transformation successful"
  /visualize_data:
    get:
      summary: "Retrieve visualizations for the BI Dashboard"
      parameters:
        - in: query
          name: panel_id
          schema:
            type: integer
          description: "The ID of the solar panel"
      responses:
        '200':
          description: "Data visualization successful"
        '404':
          description: "Visualization not found for the specified panel ID"
```

