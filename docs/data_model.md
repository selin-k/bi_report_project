# Solar Panel Performance BI Dashboard Data Model Documentation

## Standards

IEC 61970 for Energy Management System Integration

## LogicalDataModel

The logical data model is designed to support the BI Dashboard requirements for monitoring and analyzing solar panel performance. It includes entities for Solar Panels, Performance Metrics, and Environmental Conditions, with relationships that allow for the analysis of energy output, underperformance, and failure rates.

## ERDiagram


```mermaid
erDiagram
    SOLAR_PANEL ||--o{ PERFORMANCE_METRICS : measures
    SOLAR_PANEL ||--o{ ENVIRONMENTAL_CONDITIONS : experiences
    SOLAR_PANEL {
        string panelID
        string state
    }
    PERFORMANCE_METRICS {
        float S1_Amp
        float S2_Amp
        float S1_Volt
        float S2_Volt
        float S1_Power_kwh
        float S2_Power_kwh
    }
    ENVIRONMENTAL_CONDITIONS {
        float Light_kiloLux
        float Temp_degC
        string Weather
    }
```


