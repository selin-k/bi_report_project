# filename: data_visualization.py

import plotly.graph_objs as go
from dash import Dash, html, dcc

class DataVisualization:
    def __init__(self):
        self.app = Dash(__name__)
        self.app.layout = html.Div([
            html.H1("Solar Panel Performance Dashboard"),
            html.Div(id='visualization-container')
        ])

    def create_time_series_graph(self, data, x_column, y_column, title):
        if x_column not in data.columns or y_column not in data.columns:
            raise KeyError(f"One or more columns: {x_column}, {y_column} are not in the DataFrame")
        figure = go.Figure(
            data=[go.Scatter(x=data[x_column], y=data[y_column], mode='lines+markers')],
            layout=go.Layout(title=title, xaxis=dict(title=x_column), yaxis=dict(title=y_column))
        )
        return figure

    def create_performance_heatmap(self, data, x_column, y_column, z_column, title):
        if x_column not in data.columns or y_column not in data.columns or z_column not in data.columns:
            raise KeyError(f"One or more columns: {x_column}, {y_column}, {z_column} are not in the DataFrame")
        figure = go.Figure(
            data=[go.Heatmap(x=data[x_column], y=data[y_column], z=data[z_column])],
            layout=go.Layout(title=title)
        )
        return figure

    def create_bar_chart(self, data, x_column, y_column, title):
        if x_column not in data.columns or y_column not in data.columns:
            raise KeyError(f"One or more columns: {x_column}, {y_column} are not in the DataFrame")
        figure = go.Figure(
            data=[go.Bar(x=data[x_column], y=data[y_column])],
            layout=go.Layout(title=title, xaxis=dict(title=x_column), yaxis=dict(title=y_column))
        )
        return figure

    def add_visualization(self, figure, element_id):
        self.app.layout.children.append(html.Div([dcc.Graph(id=element_id, figure=figure)]))

    def run_dashboard(self):
        self.app.run_server(debug=True)

# Example usage (commented out):
# visualization = DataVisualization()
# df = pd.read_csv('path_to_csv_file')
# time_series_graph = visualization.create_time_series_graph(df, 'Timestamp', 'Current_Energy_Output', 'Energy Output Over Time')
# heatmap = visualization.create_performance_heatmap(df, 'Day', 'Hour', 'Temperature', 'Temperature Heatmap')
# bar_chart = visualization.create_bar_chart(df, 'PanelID', 'Failure_Rate', 'Failure Rate by Panel')
# visualization.add_visualization(time_series_graph, 'time-series-graph')
# visualization.add_visualization(heatmap, 'performance-heatmap')
# visualization.add_visualization(bar_chart, 'bar-chart')
# visualization.run_dashboard()