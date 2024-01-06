import pandas as pd
import plotly.express as px

def create_histogram(csv_filename):
    data = pd.read_csv(csv_filename)
    column_filter = 'total_cas_confirmes'
    for_display_y = "Pourcentage de doses n°1"
    for_display_x = "Pourcentage de doses n°1 par tranche d'âges"
    color_dash = "blue"

    # Convertir la colonne 'date' en format datetime
    data['date'] = pd.to_datetime(data['date'])

    # Utilisation de la colonne 'date' au lieu de 'Valeur de la variable'
    grouped_data = data.groupby(pd.cut(data['date'], bins=pd.date_range(start=data['date'].min(), end=data['date'].max(), freq='10D'), include_lowest=True))[column_filter].sum().reset_index()
    total_doses = grouped_data[column_filter].sum()
    grouped_data['Pourcentage'] = (grouped_data[column_filter] / total_doses) * 100
    grouped_data['Intervalles'] = grouped_data['date'].astype(str)

    fig = px.bar(
        grouped_data,
        x='Intervalles',
        y='Pourcentage',
        labels={"Pourcentage": for_display_y, "Intervalles": "Tranches d'âges"},
        title=for_display_x,
        color='Intervalles',
        color_discrete_sequence=[color_dash]
    )

    fig.update_traces(texttemplate='%{y:f}%', textposition='outside')
    fig.update_layout(margin=dict(l=50, r=20, t=50, b=50))

    return fig
