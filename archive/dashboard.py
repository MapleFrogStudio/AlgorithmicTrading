import dash
import dash_core_components as dcc
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Div import Div

import stocks

companies = stocks.NasdaqSymbols()

app = dash.Dash(__name__)
prices = stocks.GrabPrices("TSLA","2020-01-01", "2021-01-31")

app.layout = html.Div(children=[
    html.H1("Hello Stocks"),
    dcc.Dropdown(
        id = "slct_stock", 
        options=[
            {"label":"TSLA", "value": "TSLA"},
            {"label":"AAPL", "value": "AAPL"},
            {"label":"MSFT", "value": "MSFT"}],
        multi=False,
        value="TSLA",
        style={'width': "70%"}
    ),

    html.Div(id='display_selected_ticker', children=[]),
    dcc.Graph(id='show_graph_01', figure={})
])



@app.callback(
    [Output(component_id='display_selected_ticker', component_property='children'),
     Output(component_id='show_graph_01'          , component_property='figure'  )],
    [Input(component_id='slct_stock'              , component_property='value')]
)
def update_graph(stock_ticker_value):
    print(stock_ticker_value)  
    prices = stocks.GrabPrices(stock_ticker_value, "2020-01-01", "2020-12-31")
    info = companies[companies['NASDAQ Symbol'] == stock_ticker_value]["Security Name"].values
    container = [f"Compnay name {info}"]
    fig, ax = stocks.fig_candlestick(prices) 
    return container, fig



# Run the web server
if __name__ == '__main__':
    app.run_server(debug=True)