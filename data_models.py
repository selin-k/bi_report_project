# filename: data_models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, Date

Base = declarative_base()

class FACT_SOLAR_OUTPUT(Base):
    __tablename__ = 'fact_solar_output'
    OutputID = Column(Integer, primary_key=True)
    Timestamp = Column(DateTime)
    S1_Power_kwh = Column(Float)
    S2_Power_kwh = Column(Float)
    Total_Power_kwh = Column(Float)

class FACT_PANEL_STATE(Base):
    __tablename__ = 'fact_panel_state'
    StateID = Column(Integer, primary_key=True)
    Timestamp = Column(DateTime)
    PanelID = Column(Integer)
    State = Column(String)

class DIM_PANEL(Base):
    __tablename__ = 'dim_panel'
    PanelID = Column(Integer, primary_key=True)
    PanelType = Column(String)
    InstallationDate = Column(Date)

class DIM_ENVIRONMENT(Base):
    __tablename__ = 'dim_environment'
    EnvironmentID = Column(Integer, primary_key=True)
    Light_kiloLux = Column(Float)
    Temp_degC = Column(Float)
    Weather = Column(String)