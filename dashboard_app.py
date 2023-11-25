# filename: dashboard_app.py
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
from flask import Flask
from solar_panel_dashboard.services.orchestration_service import OrchestrationService

# Initialize Flask and Dash applications
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Solar Panel BI Dashboard'),

    html.Div(children='''
        Dashboard for monitoring and analyzing solar panel data.
    '''),

    dcc.Graph(
        id='energy-output-graph',
    ),

    dcc.Graph(
        id='underperforming-panels-graph',
    ),

    dcc.Graph(
        id='panel-failure-rate-graph',
    ),

    # Interval component for live updates
    dcc.Interval(
        id='interval-component',
        interval=1*60*1000,  # in milliseconds
        n_intervals=0
    )
])

# Assuming orchestration_service is set up with the correct parameters
orchestration_service = OrchestrationService('/path/to/solar_sensors.csv', schema, performance_threshold)

# Callback for updating the energy output graph
@app.callback(
    Output('energy-output-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_energy_output(n):
    final_data = orchestration_service.orchestrate_etl()
    fig = px.line(final_data, x='timestamp', y='average_energy_output', title='Current Energy Output')
    return fig

# Callback for updating the underperforming panels graph
@app.callback(
    Output('underperforming-panels-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_underperforming_panels(n):
    final_data = orchestration_service.orchestrate_etl()
    underperforming_data = final_data[final_data['is_underperforming']]
    fig = px.bar(underperforming_data, x='panel_id', y='energy_output', title='Underperforming Solar Panels')
    return fig

# Callback for updating the panel failure rate graph
@app.callback(
    Output('panel-failure-rate-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_panel_failure_rate(n):
    final_data = orchestration_service.orchestrate_etl()
    # Assuming 'failure_rate' is a column in the final_data DataFrame
    fig = px.bar(final_data, x='panel_id', y='failure_rate', title='Panel Failure Rates')
    return fig

# Run the Flask server
if __name__ == '__main__':
    app.run_server(debug=True)