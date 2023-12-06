from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('synthese-fra.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Synthese France', style={'textAlign':'center'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=25),
    dcc.Graph(figure=px.histogram(df, x='date', y='total_cas_confirmes', histfunc='avg'))
])

if __name__ == '__main__':
    app.run(debug=True)