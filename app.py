import os
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
from layouts import tiers, results

app = dash.Dash(__name__)
app.layout = html.Div([

    # Dashboard header
    html.H1(
        className='dash-header',
        children='40draw5',
    ),

    # Main layout
    html.Div(className='row', children=[
        html.Div(id='tiers', className="six columns", children=tiers.render()),
    ]),
    html.Div(className='row', children=[
        html.Div(id='results', className="six columns", children=results.render()),
    ]),
])

tiers.register_callbacks(app)
results.register_callbacks(app)


if __name__ == '__main__':
    app.run_server()