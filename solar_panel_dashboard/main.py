# filename: solar_panel_dashboard/main.py
from flask import Flask, render_template
from solar_panel_dashboard.data_ingestion import DataIngestion
from solar_panel_dashboard.data_curation import DataCuration
from solar_panel_dashboard.data_transformation import DataTransformation
from solar_panel_dashboard.data_visualization import DataVisualization
from solar_panel_dashboard.models import FACT_SOLAR_OUTPUT

# Initialize Flask application
app = Flask(__name__)

# Define the route for the index page
@app.route('/')
def index():
    # Orchestrate the ETL pipeline
    # Step 1: Data Ingestion
    ingestion = DataIngestion()
    data_frame = ingestion.load_data('/Users/selinkayay/appgenpro/data/solar_sensors.csv')
    
    # Step 2: Data Curation
    curation = DataCuration()
    validated_data = curation.validate_data(data_frame)
    normalized_data = curation.normalize_data(validated_data)
    
    # Step 3: Data Transformation
    transformation = DataTransformation()
    transformed_data = transformation.transform_data(normalized_data)
    
    # Step 4: KPI Calculation
    fact_solar_output = FACT_SOLAR_OUTPUT()
    fact_solar_output.calculate_kpis(transformed_data)
    
    # Step 5: Data Visualization
    visualization = DataVisualization()
    visualization.generate_visuals(transformed_data)
    
    # Render the dashboard template
    return render_template('dashboard.html')

# Run the Flask application if this file is executed as the main program
if __name__ == '__main__':
    app.run(debug=True)