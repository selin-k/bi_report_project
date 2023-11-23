# Technical Design Document for Solar Panel KPIs BI Report

## HighLevelSystemDesign

The solution architecture is based on a microservices architecture pattern, which will facilitate the development, deployment, and scaling of the ETL data pipeline for the BI application. Each microservice will be implemented using Python and will be orchestrated using Azure services to deliver an ETL Data Pipeline that is robust, scalable, and maintainable. The microservices will be designed to work with Azure Synapse Analytics dedicated pool for data warehousing and Azure Kubernetes Service (AKS) for container orchestration, with the flexibility to be deployed locally if required.

## DataIngestion

The data_ingestion microservice is responsible for extracting data from various sources including the in-house IoT platform and the manufacturing execution system (MES). It will use configurable adapters to connect to these sources and ingest data into Azure Data Lake in a 'raw' format. The ingestion process will be designed to handle different data formats and convert them into a consistent format (e.g., CSV) for further processing.

## DataCuration

The data_curation microservice will take the raw data from the Azure Data Lake and perform necessary curation steps such as deduplication, null value handling, and data normalization. The curated data will be mapped to the target schema and stored back into Azure Data Lake in a 'curated' folder as parquet files to optimize for analytical queries.

## DataTransformation

The data_transformation microservice will load the curated data and apply business logic to calculate the KPIs as defined in the requirements document. It will leverage the logical data model to transform the data into fact and dimension tables, which will then be stored in a 'conformed' folder within Azure Data Lake, ready for analysis and reporting.

## DataVisualization

The data_visualization microservice will use the conformed data to create interactive dashboards and visualizations. It will utilize tools like Power BI or a similar platform to create time series charts, bar graphs, and heat maps that represent the production performance metrics in an intuitive and user-friendly manner.

## Orchestration

The orchestration of the data pipeline will be managed by Azure Data Factory or a similar cloud-based service. It will schedule and automate the workflow of the microservices, ensuring that data flows smoothly from ingestion to visualization. The orchestration service will also handle error logging and alerting to maintain high availability and reliability of the BI application.

## ClassDiagrams

classDiagram
    class DataIngestion{
        +ingest_data() None
    }
    class DataCuration{
        +curate_data() None
    }
    class DataTransformation{
        +transform_data() None
    }
    class DataVisualization{
        +visualize_data() None
    }
    class Orchestration{
        +orchestrate_pipeline() None
    }
    DataIngestion --|> AzureDataLakeStorageConnector: uses
    DataCuration --|> AzureDataLakeStorageConnector: uses
    DataTransformation --|> AzureDataLakeStorageConnector: uses
    DataVisualization --|> AzureDataLakeStorageConnector: uses
    Orchestration --|> AzureDataLakeStorageConnector: uses

## ProgramFlow

sequenceDiagram
    participant Orchestration as Orchestration
    participant DataIngestion as DataIngestion
    participant DataCuration as DataCuration
    participant DataTransformation as DataTransformation
    participant DataVisualization as DataVisualization

    Orchestration->>DataIngestion: ingest_data()
    DataIngestion->>DataCuration: curate_data()
    DataCuration->>DataTransformation: transform_data()
    DataTransformation->>DataVisualization: visualize_data()

