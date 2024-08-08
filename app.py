import dash
from dash import dcc, html
import pandas as pd
from get_data import get_data

# Load the dataset
new_train = get_data('new_train')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1(f"Enefit Dashboard for {pd.Timestamp.now().strftime('%Y-%m-%d')}"),
    
    html.Div([
        dcc.DatePickerSingle(
            id='date-picker',
            date=pd.Timestamp.now().date()
        ),
        dcc.Dropdown(
            id='county-dropdown',
            options=[{'label': name, 'value': id} for id, name in zip(new_train['county'], new_train['county_name'])],
            value=new_train['county'].iloc[0]
        )
    ]),
    
    dcc.Graph(id='consumption-line-chart'),
    dcc.Graph(id='production-line-chart'),
    dcc.Graph(id='hor-cyl-histogram'),
    dcc.Graph(id='ver-cyl-histogram'),
    dcc.Graph(id='county-bar-chart'),
    dcc.Graph(id='scatter-plot-hor'),
    dcc.Graph(id='scatter-plot-ver'),
    dcc.Graph(id='correlation-heatmap')
])

# Import the callbacks
import callbacks

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
