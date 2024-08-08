from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from app import app, new_train

@app.callback(
    [
        Output('consumption-line-chart', 'figure'),
        Output('production-line-chart', 'figure'),
        Output('hor-cyl-histogram', 'figure'),
        Output('ver-cyl-histogram', 'figure'),
        Output('county-bar-chart', 'figure'),
        Output('scatter-plot-hor', 'figure'),
        Output('scatter-plot-ver', 'figure'),
        Output('correlation-heatmap', 'figure')
    ],
    [
        Input('date-picker', 'date'),
        Input('county-dropdown', 'value')
    ]
)
def update_graphs(selected_date, selected_county):
    try:
        # Filter data based on selected date and county
        filtered_data = new_train[
            (pd.to_datetime(new_train['datetime']).dt.date == pd.to_datetime(selected_date).date()) &
            (new_train['county'] == selected_county)
        ]
        
        # Line charts for consumption and production
        consumption_line_chart = px.line(
            filtered_data, x='datetime', y='consumption_column', title='Energy Consumption Over Time'
        )
        production_line_chart = px.line(
            filtered_data, x='datetime', y='production_column', title='Energy Production Over Time'
        )
        
        # Histograms for turbine distributions
        hor_cyl_histogram = px.histogram(
            filtered_data, x='h3_n_hor_cyl', title='Distribution of Horizontal Cylindrical Turbines'
        )
        ver_cyl_histogram = px.histogram(
            filtered_data, x='h3_n_ver_cyl', title='Distribution of Vertical Cylindrical Turbines'
        )
        
        # Bar chart for average turbine counts per county
        county_avg = new_train.groupby('county_name').mean().reset_index()
        county_bar_chart = px.bar(
            county_avg, x='county_name', y=['h3_n_hor_cyl', 'h3_n_ver_cyl'], title='Average Turbine Counts per County'
        )
        
        # Scatter plots
        scatter_plot_hor = px.scatter(
            data_frame=filtered_data,
            x='temperature',  # Replaced 'wind_speed' with 'temperature'
            y='h3_n_hor_cyl',
            title='Temperature vs Horizontal Cylindrical Turbines'
        )

        scatter_plot_ver = px.scatter(
            data_frame=filtered_data,
            x='altitude',  # Replace 'altitude' with actual feature name
            y='h3_n_ver_cyl',
            title='Altitude vs Vertical Cylindrical Turbines'
        )
        
        # Correlation heatmap
        correlation_data = new_train.corr()
        correlation_heatmap = px.imshow(
            correlation_data, title='Correlation Heatmap'
        )
        
        return (
            consumption_line_chart, production_line_chart, hor_cyl_histogram,
            ver_cyl_histogram, county_bar_chart, scatter_plot_hor,
            scatter_plot_ver, correlation_heatmap
        )
    
    except Exception as e:
        print(f"Error: {e}")
        return {}, {}, {}, {}, {}, {}, {}, {}
