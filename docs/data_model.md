# Data Model Design Document for Solar Panel BI Dashboard

## Standards

IEC 61970 for Energy Management System Integration

## LogicalDataModel

The logical data model for the Solar Panel BI Dashboard includes entities such as Solar_Panel, Energy_Output, Panel_Failure, and Environmental_Factor. Each entity has attributes that capture the necessary details for analysis and reporting within the BI Dashboard.

## ERDiagram


```mermaid
ERDiagram
    SOLAR_PANEL ||--o{ ENERGY_OUTPUT : generates
    SOLAR_PANEL ||--o{ PANEL_FAILURE : experiences
    SOLAR_PANEL ||--o{ ENVIRONMENTAL_FACTOR : influenced_by
    SOLAR_PANEL {
        string panel_id PK
        string location
        string type
    }
    ENERGY_OUTPUT {
        string output_id PK
        string panel_id FK
        datetime timestamp
        float kWh
    }
    PANEL_FAILURE {
        string failure_id PK
        string panel_id FK
        string failure_type
        datetime failure_time
        int count
    }
    ENVIRONMENTAL_FACTOR {
        string factor_id PK
        string panel_id FK
        datetime timestamp
        float temperature
        float light_intensity
    }
```


