# Technical Design Document for Local Solar Panel BI Dashboard ETL Pipeline

## HighLevelSystemDesign

The solution architecture is designed for local execution, leveraging Python and its libraries such as pandas for data manipulation and Plotly for interactive visualizations. The application will consist of a series of Python classes that encapsulate the functionality for data ingestion, curation, transformation, and visualization.

## DataIngestion

The DataIngestion class will be responsible for loading the solar sensor data from the local CSV file using pandas. It will read the data into a pandas DataFrame for further processing.

## DataCuration

The DataCuration class will perform data validation and normalization on the ingested data. It will ensure that there are no missing or corrupt values and that the data is consistent. The curated data will be stored in a pandas DataFrame.

## DataTransformation

The DataTransformation class will apply business logic to calculate the KPIs defined in the requirements document. It will transform the curated data into the format specified by the logical data model, using classes that represent the fact and dimension tables.

## DataVisualization

The DataVisualization class will use the transformed data to generate the required visualizations such as time series graphs, heatmaps, pie charts, and scatter plots using Plotly. These visualizations will be interactive and can be viewed in a web browser.

## Orchestration

The orchestration of the ETL pipeline will be managed by a main driver script that sequentially executes the methods of the DataIngestion, DataCuration, DataTransformation, and DataVisualization classes. Error handling will be implemented to log and manage any issues that arise during execution.

## ClassDiagrams

```mermaid
classDiagram
    class DataIngestion {
        +load_data(file_path: str) DataFrame
    }
    class DataCuration {
        +validate_data(data: DataFrame) DataFrame
        +normalize_data(data: DataFrame) DataFrame
    }
    class DataTransformation {
        +transform_data(data: DataFrame) DataFrame
    }
    class DataVisualization {
        +generate_visuals(data: DataFrame) None
    }
    class FACT_SOLAR_OUTPUT {
        int OutputID
        int PanelID
        datetime Timestamp
        float EnergyOutput
        int WeatherConditionID
        int FailureID
        +calculate_kpis() None
    }
    class DIM_PANEL {
        int PanelID
        string PanelType
        date InstallationDate
        string Location
    }
    class DIM_WEATHER_CONDITION {
        int WeatherConditionID
        float Temperature
        float WindSpeed
        float Humidity
        float Irradiance
    }
    class DIM_FAILURE {
        int FailureID
        string FailureType
        string FailureDescription
        date FailureDate
    }
    DataIngestion -- DIM_PANEL
    DataIngestion -- DIM_WEATHER_CONDITION
    DataIngestion -- DIM_FAILURE
    DataCuration -- DIM_PANEL
    DataCuration -- DIM_WEATHER_CONDITION
    DataCuration -- DIM_FAILURE
    DataTransformation -- FACT_SOLAR_OUTPUT
    DataVisualization -- FACT_SOLAR_OUTPUT
```

## ProgramFlow

```mermaid
sequenceDiagram
    participant Main as Main
    participant Ingestion as DataIngestion
    participant Curation as DataCuration
    participant Transformation as DataTransformation
    participant Visualization as DataVisualization
    participant FACT_SOLAR_OUTPUT as FACT_SOLAR_OUTPUT
    participant DIM_PANEL as DIM_PANEL
    participant DIM_WEATHER_CONDITION as DIM_WEATHER_CONDITION
    participant DIM_FAILURE as DIM_FAILURE

    Main->>Ingestion: Load CSV
    Ingestion-->>Curation: Validate and Normalize Data
    Curation-->>Transformation: Transform to Data Model
    Transformation-->>FACT_SOLAR_OUTPUT: Calculate KPIs
    FACT_SOLAR_OUTPUT-->>Visualization: Generate Visualizations
```

