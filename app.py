import dash
import pandas as pd
from dash import Dash, html, dash_table, dcc
from dash.dependencies import Input, Output
from dataReader import download_data
import plotly.express as px

csv_filename = download_data()
df = pd.read_csv(csv_filename)
app = dash.Dash(__name__)

# Liste des colonnes pour la liste déroulante
column_options = [{'label': col, 'value': col} for col in df.columns]

app.layout = html.Div([
    html.Div(children='DASHBOARD DONNEES '),

    # Ajouter la liste déroulante pour sélectionner la colonne
    dcc.Dropdown(
        id='column-dropdown',
        options=column_options,
        value=df.columns[0],  # Sélectionner la première colonne par défaut
        style={'width': '50%'}
    ),

    # Remplacer le tableau par un graphique à barres
    dcc.Graph(id='bar-chart'),
])


# Mettre à jour le graphique en fonction de la colonne sélectionnée
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_chart(selected_column):
    try:
        chart_figure = px.bar(df, x=df.index, y=selected_column, title=f'Graphique de {selected_column}')
        print(f'Successfully updated chart for {selected_column}')
        return chart_figure
    except Exception as e:
        print(f'Error updating chart: {str(e)}')
        return px.scatter(title='Error Updating Chart')


if __name__ == "__main__":
    app.run_server(debug=True)
