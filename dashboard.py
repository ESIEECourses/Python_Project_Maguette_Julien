import dash
from dash import html, dcc
from dataReader import download_data
from histogram import create_histogram

def create_dash_application():
    csv_filename = download_data()

    app = dash.Dash(__name__)

    histogram_fig = create_histogram(csv_filename)

    app.layout = html.Div(
        id='app-container',
        children=[
            html.H1("DASHBOARD DONNEES"),
            dcc.Graph(figure=histogram_fig),  # Histogramme
            # Vous pouvez ajouter d'autres composants ici selon vos besoins
        ],
        style={'backgroundColor': '#0d0d26'},
    )

    return app
