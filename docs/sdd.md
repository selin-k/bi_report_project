# Technical Design Document for Solar Panel Performance BI Dashboard

## HighLevelSystemDesign

The solution architecture is based on a microservices architecture pattern, where each microservice is implemented using Python and orchestrated using Azure Kubernetes Service (AKS) to deliver an ETL Data Pipeline. This architecture will enable scalability, reliability, and maintainability of the data processing workflows. The microservices will interact with Azure Synapse Analytics dedicated SQL pool for data storage and processing, and Spark pool for data transformation and analytics.

## DataIngestion

The data_ingestion microservice is responsible for ingesting solar sensor data from CSV files. It will utilize a configurable adapter to fetch data from the local file system or Azure Data Lake Store, depending on the deployment. The ingested data will be stored in a 'raw' data folder within Azure Data Lake Store, partitioned by ingestion date.

## DataCuration

The data_curation microservice will load raw data from the 'raw' data folder, perform data cleaning such as deduplication and null value imputation, and map source data to the target schema. The curated data will be stored in a 'curated' folder in Azure Data Lake Store as parquet files to optimize for analytical queries.

## DataTransformation

The data_transformation microservice will transform curated data into a format suitable for BI analytics, based on the logical data model provided. It will calculate KPIs and metrics as per business logic aligned with IEC61970 standards. The transformed data will be stored in a 'conformed' folder within Azure Data Lake Store, ready for visualization and reporting.

## DataVisualization

The data_visualization microservice will utilize the conformed data to generate visualizations using tools like Power BI or Tableau. It will create interactive dashboards that display energy production trends, performance comparisons, and predictive analytics for solar panel failures.

## Orchestration

Orchestration will be managed by Azure Data Factory, which will create and manage a data pipeline to orchestrate the execution of microservices in sequence. The pipeline will be scheduled to run daily, ensuring that the BI dashboard is updated with the latest data. Error handling and logging mechanisms will be in place to capture and report any issues during the pipeline execution.

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
    Orchestration --|> AzureDataFactory: uses

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

