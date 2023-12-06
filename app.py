import dash
import pandas as pd
from dash import Dash, html, dash_table
from dataReader import download_data

csv_filename = download_data()
df = pd.read_csv(csv_filename)
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(children='DASHBOARD DONNEES '),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

if __name__ == "__main__":
    app.run_server(debug=True)
