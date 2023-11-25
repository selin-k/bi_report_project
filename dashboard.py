# filename: solar_panel_dashboard/dashboard.py
from flask import Flask, jsonify, request
from solar_panel_dashboard.data_ingestion import DataIngestion
from solar_panel_dashboard.data_curation import DataCuration
from solar_panel_dashboard.data_transformation import DataTransformation
from solar_panel_dashboard.data_visualization import DataVisualization

# Initialize Flask application
app = Flask(__name__)

# Define the route for the index page
@app.route('/')
def index():
    # This function will render the dashboard page
    return "Solar Panel Dashboard"

# Define API endpoint for data ingestion
@app.route('/data/ingest', methods=['POST'])
def ingest_data():
    file_path = request.json.get('file_path')
    ingestion = DataIngestion()
    data_frame = ingestion.load_data(file_path)
    return jsonify(success=True, message="Data ingestion successful")

# Define API endpoint for data curation
@app.route('/data/curate', methods=['POST'])
def curate_data():
    data = request.json.get('data')
    curation = DataCuration()
    validated_data = curation.validate_data(data)
    normalized_data = curation.normalize_data(validated_data)
    return jsonify(success=True, message="Data curation successful")

# Define API endpoint for data transformation
@app.route('/data/transform', methods=['POST'])
def transform_data():
    data = request.json.get('data')
    transformation = DataTransformation()
    transformed_data = transformation.transform_data(data)
    return jsonify(success=True, message="Data transformation successful")

# Define API endpoint for visualization generation
@app.route('/visualize', methods=['GET'])
def visualize_data():
    # This function will generate visualizations for the dashboard
    # For now, it returns a placeholder message
    return jsonify(success=True, message="Visualizations generated successfully")

# Run the Flask application if this file is executed as the main program
if __name__ == '__main__':
    app.run(debug=True)