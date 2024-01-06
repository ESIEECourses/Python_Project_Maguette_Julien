# map.py
import pandas as pd
import folium
import numpy as np
from branca.colormap import LinearColormap

def create_map(csv_filename):
    df = pd.read_csv(csv_filename)
    df = df.dropna()

    centre_lat, centre_lon = 46.6031, 1.8883
    map_bounds = [[41, -5], [51, 9]]
    min_deces = df['Total Décès'].min()
    max_deces = df['Total Décès'].max()

    colormap = LinearColormap(
        colors=['#FFFF00', '#FFA500', '#FF0000'],
        index=[min_deces, (min_deces + max_deces) / 2, max_deces],
        vmin=min_deces, vmax=max_deces
    )

    m = folium.Map(location=[centre_lat, centre_lon], zoom_start=6,
                   max_bounds=True, min_zoom=6, max_zoom=10, bounds=map_bounds)

    add_markers(m, df, colormap)

    return m

def add_markers(m, df, colormap):
    for index, row in df.iterrows():
        radius = np.log1p(row['Total Décès']) * 1.5
        radius = max(radius, 3)
        radius = min(radius, 10)

        color = colormap(row['Total Décès'])

        tooltip_text = f"{row['Nom département']} - Total Décès: {row['Total Décès']}"

        folium.CircleMarker(
            location=[float(coord) for coord in row['geo_point_2d'].split(', ')],
            radius=radius,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            tooltip=tooltip_text
        ).add_to(m)
