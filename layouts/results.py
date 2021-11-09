import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
import run_simulations
from dash.exceptions import PreventUpdate

def render():
    return html.P('Press Submit to generate results', id='results-output')


def register_callbacks(app):
    @app.callback(
        Output("results-output", "children"),
        Input("submit", "n_clicks"),
        State("n-cards-to-win", "value"),
        State("n-simulations", "value"),
        State({'type': 'tier', 'index': ALL}, 'value')
        )
    def add_tier(n_clicks, n_cards_to_win, n_simulations, inputs):
        if n_clicks == 0:
            raise PreventUpdate
        else:
            # input_states = dash.callback_context.states

            # n_simulations = input_states["n-simulations.value"]
            # n_cards_to_win = input_states["n-cards-to-win.value"]
            tiers = dict( (f"{i+1}", v) for i, v in enumerate(inputs))

            n_cards_to_win = float(n_cards_to_win)
            n_simulations = float(n_simulations)
            if (
                n_cards_to_win is None
                or float(n_cards_to_win) <= 0
                or float(n_cards_to_win) != int(n_cards_to_win)
                ):
                return "Please enter a positive integer value for how many cards to win"
            else:
                n_cards_to_win = int(n_cards_to_win)

            if (
                n_simulations is None
                or float(n_simulations) <= 0
                or float(n_simulations) != int(n_simulations)
                ):
                return "Please enter a positive integer value for number of simulations"
            else:
                n_simulations = int(n_simulations)

            if (
                any([value is None for value in tiers.values()])
                or any([value <= 0 for value in tiers.values()])
                or any([value != round(value) for value in tiers.values()])
                ):
                return "Please enter a positive integer value for all tiers"
            
            return run_simulations.get_result(tiers, n_cards_to_win, n_simulations)