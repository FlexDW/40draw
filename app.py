import os
import json
import dash
from dash import html
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

server = app.server

if __name__ == '__main__':
    app.run_server(
        host='0.0.0.0',
        port=3539,
        debug=True,
    )
