import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL

def render():
    return [
        html.H5('Configure Tiers'),
        html.Div(className="row", children=[
            html.Div("How many cards to win:", className="four columns"),
            dcc.Input(id="n-cards-to-win", type="number", value="5")
        ]),
        html.Div(className="row", children=[
            html.Div("How many simulations:", className="four columns"),
            dcc.Input(id="n-simulations", type="number", value="100000")
        ]),
        html.Div(id="input-fields", className="row", children=[
            html.Div(className="row tier", children=[
                html.Div("How many cards in each tier", className="six columns"),
            ])
        ]),
        html.Div(className="row", children=[
            html.Button('Add Tier', id='add-tier', n_clicks=0),
            html.Button('Submit', id='submit', n_clicks=0),
        ])
    ]

def render_tier(tier_number):
    return html.Div(className="row tier", children=[
                html.Div(f"Tier {tier_number}", className="one columns"),
                dcc.Input(id={'type': 'tier', 'index': tier_number}, className="four columns", type="number"),
            ])

def register_callbacks(app):
    @app.callback(
        Output("input-fields", "children"),
        Input("add-tier", "n_clicks"),
        State("input-fields", "children")
        )
    def add_tier(n_clicks, current_children):
        return current_children + [render_tier(n_clicks + 1)]
