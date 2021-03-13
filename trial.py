from dash_html_components.Center import Center
import plotly.graph_objects as go
import dash

import dash_html_components as html

app = dash.Dash()

# Define the HTML Component
app.layout = html.Div([
    html.Div("Hello all!", style={"color": "red", "text-align": "center"}),
    html.Div("How are you")
])




if __name__ == '__main__':
    app.run_server()

