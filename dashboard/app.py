import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import os

df = pd.read_csv('data/cleaned_macro_data.csv')

app = dash.Dash(__name__)
app.title = "Nigeria Economic Dashboard"

app.layout = html.Div([
    html.H1("🇳🇬 Nigeria Economic Dashboard", style={'textAlign': 'center'}),

    html.Label("Choose an Indicator:", style={'marginTop': '20px'}),
    dcc.Dropdown(
        id='indicator-dropdown',
        options=[{'label': col.replace("_", " "), 'value': col}
                 for col in df.columns if col != 'Year'],
        value='Inflation_Rate',
        clearable=False
    ),

    dcc.Graph(id='line-chart', style={'marginTop': '20px'})
])

@app.callback(
    Output('line-chart', 'figure'),
    Input('indicator-dropdown', 'value')
)
def update_chart(selected_indicator):
    fig = px.line(df, x='Year', y=selected_indicator,
                  markers=True, title=selected_indicator.replace("_", " "))
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run(debug=True, port=port, hosts='0.0.0.0')