# Technical Design Document for Solar Panel Performance Monitoring BI Dashboard

## HighLevelSystemDesign

The solution architecture is based on a microservices architecture pattern, leveraging Azure Synapse Analytics and Azure Kubernetes Service (AKS) for deployment. The architecture will consist of a series of independent microservices, each responsible for a specific aspect of the ETL process, including data ingestion, curation, transformation, and visualization. These microservices will be implemented using Python and will interact with each other via RESTful APIs.

## DataIngestion

The data_ingestion microservice is responsible for ingesting solar sensor data from the CSV file located at /project_name/data/solar_sensors.csv. It will validate the CSV format and ensure that the data adheres to the expected schema before loading it into the Azure Synapse Analytics dedicated pool for raw data storage.

## DataCuration

The data_curation microservice will handle data quality issues such as missing values and inconsistencies. It will apply imputation methods to fill in missing data and perform data normalization to ensure consistency across different data sources. The curated data will then be stored in a 'curated' data store within Azure Synapse Analytics.

## DataTransformation

The data_transformation microservice will apply business logic to the curated data to calculate KPIs and performance metrics as defined by the client. It will transform the data according to the logical semantic data model, populating the fact and dimension tables. The transformed data will be stored in a 'conformed' data store, ready for analysis and visualization.

## DataVisualization

The data_visualization microservice will retrieve the conformed data and generate interactive visualizations for the BI Dashboard. It will leverage visualization libraries such as Plotly or Power BI Embedded to create charts and graphs that allow users to monitor energy output, identify underperforming panels, and predict failures.

## Orchestration

The orchestration layer will coordinate the execution of the microservices, ensuring that data flows smoothly from ingestion to visualization. It will be implemented using Azure Data Factory or a similar orchestration tool, with scheduled triggers to process data on a daily basis.

## ClassDiagrams

```mermaid
classDiagram
    class DataIngestion{
        +ingest_data() -> None
    }
    class DataCuration{
        +curate_data() -> None
    }
    class DataTransformation{
        +transform_data() -> None
    }
    class DataVisualization{
        +visualize_data() -> None
    }
    class Orchestration{
        +orchestrate_pipeline() -> None
    }
    class FACT_ENERGY_OUTPUT{
        int EnergyOutputID PK
        int PanelID FK
        datetime Timestamp
        float EnergyProduced
        int WeatherConditionID FK
    }
    class FACT_PANEL_FAILURES{
        int PanelFailureID PK
        int PanelID FK
        datetime FailureTimestamp
        int FailureTypeID FK
        bit IsResolved
    }
    class DIM_PANEL{
        int PanelID PK
        varchar PanelType
        date InstallationDate
        float Capacity
        int LocationID FK
    }
    class DIM_WEATHER_CONDITION{
        int WeatherConditionID PK
        float Temperature
        float SunlightIntensity
        varchar WeatherDescription
    }
    class DIM_FAILURE_TYPE{
        int FailureTypeID PK
        varchar FailureDescription
        varchar PotentialCause
    }
    class DIM_LOCATION{
        int LocationID PK
        varchar Country
        varchar Region
        varchar GPS_Coordinates
    }
    DataIngestion --|> Orchestration: triggers
    DataCuration --|> Orchestration: triggers
    DataTransformation --|> Orchestration: triggers
    DataVisualization --|> Orchestration: triggers
    FACT_ENERGY_OUTPUT --|> DIM_PANEL: contains
    FACT_ENERGY_OUTPUT --|> DIM_WEATHER_CONDITION: contains
    FACT_PANEL_FAILURES --|> DIM_PANEL: contains
    FACT_PANEL_FAILURES --|> DIM_FAILURE_TYPE: contains
    DIM_PANEL --|> DIM_LOCATION: located_in
```

## ProgramFlow

```mermaid
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
    DataTransformation->>FACT_ENERGY_OUTPUT: populate_fact_table()
    DataTransformation->>FACT_PANEL_FAILURES: populate_fact_table()
    DataTransformation->>DIM_PANEL: populate_dimension_table()
    DataTransformation->>DIM_WEATHER_CONDITION: populate_dimension_table()
    DataTransformation->>DIM_FAILURE_TYPE: populate_dimension_table()
    DataTransformation->>DIM_LOCATION: populate_dimension_table()
```

