import dash
import pandas as pd
from dash import html, dcc, dash_table, callback, Output, Input
import plotly.express as px

# Charger les données depuis le fichier CSV
df = pd.read_csv('stocks-es-par-dep.csv')

# Créer une application Dash avec des styles externes
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/darkly/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def create_layout():
    """
    Crée la mise en page du tableau de bord avec une carte interactive.

    Returns:
        dash.html.Div: La mise en page du tableau de bord.
    """
    return html.Div(
        id='main-layout',
        style={'backgroundColor': '#343a40', 'color': 'white', 'padding': '20px'},
        children=[
            html.H1(id='main-title', children='Carte interactive de la vaccination COVID-19 par département',
                    style={'textAlign': 'center'}),
            create_data_table(),
            create_histogram_graph(),
            create_controls_and_graph(),
            create_pie_chart()
        ]
    )

def create_data_table():
    """
    Crée un tableau de données interactif.

    Returns:
        dash.dash_table.DataTable: Le tableau de données interactif.
    """
    return html.Div([
        dash_table.DataTable(
            id='data-table',
            data=df.to_dict('records'),
            page_size=10,
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={'backgroundColor': '#444', 'color': 'white'}
        )
    ], style={'margin': '20px'})

def create_histogram_graph():
    """
    Crée un graphique d'histogramme interactif.

    Returns:
        dcc.Graph: Le graphique d'histogramme interactif.
    """
    return html.Div([
        dcc.Graph(
            id='histogram-graph',
            figure=px.histogram(df, x='Date', y='Nombres De Doses', color='Type De Vaccin',
                                title='Histogramme des doses par date et type de vaccin'),
            style={'backgroundColor': '#444'}
        )
    ], style={'margin': '20px'})

def create_controls_and_graph():
    """
    Crée des contrôles pour interagir avec le graphique.

    Returns:
        dash.html.Div: Les contrôles et le graphique interactif.
    """
    return html.Div([
        dcc.Dropdown(
            id='controls-and-radio-item',
            options=[
                {'label': col, 'value': col} for col in df.columns[2:]
            ],
            value='Nombres De Doses',
            style={'width': '50%', 'margin': '10px auto', 'backgroundColor': '#444'}
        ),
        dcc.Graph(id='controls-and-graph', style={'backgroundColor': '#444'}),
    ], style={'margin': '20px'})

def create_pie_chart():
    """
    Crée un graphique en cercle (pie chart) interactif.

    Returns:
        dcc.Graph: Le graphique en cercle (pie chart) interactif.
    """
    return html.Div([
        dcc.Graph(id='pie-chart', style={'backgroundColor': '#444'})
    ], style={'margin': '20px'})

# Ajout des callbacks pour interagir avec le graphique
@app.callback(
    Output('controls-and-graph', 'figure'),
    Input('controls-and-radio-item', 'value')
)
def update_graph(col_chosen):
    if col_chosen == 'Type De Vaccin':
        fig = px.histogram(df, x='Date', y='Nombres De Doses', color=col_chosen, title=f'Données par {col_chosen}')
    else:
        fig = px.histogram(df, x='Date', y=col_chosen, title=f'Données par {col_chosen}')
    return fig

# Callback pour le graphique en cercle (pie chart)
@app.callback(
    Output('pie-chart', 'figure'),
    Input('controls-and-radio-item', 'value')
)
def update_pie_chart(col_chosen):
    if col_chosen == 'Type De Vaccin':
        fig = px.pie(df, names='Type De Vaccin', title='Répartition des types de vaccin')
    else:
        fig = px.pie(df, names='Type De Vaccin', title='Répartition des types de vaccin')
    return fig

if __name__ == '__main__':
    app.layout = create_layout()
    app.run_server(host='127.0.0.1', port=8050, debug=True)
