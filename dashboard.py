from streamlit_geolocation import streamlit_geolocation

import sqlite3
import pandas as pd
import streamlit as st
import folium

from streamlit_folium import st_folium

from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

def haversine(lat1, lon1, lat2, lon2):

    R = 6371.0

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        +
        cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return R * c

col1, col2 = st.columns([1,1])

with col1:

    if st.button("🔄 Atualizar dados RBMC"):
        import subprocess

        subprocess.run(
            ["python", "atualizar_rbmc.py"]
        )

        st.rerun()

with col2:

    st.link_button(
        "🌐 Dado retirado diretamente do IBGE",
        "http://170.84.40.52:2101/"
    )
    


st.set_page_config(
    page_title="RBMC Dashboard",
    layout="wide"
)

conn = sqlite3.connect("rbmc.db")

df = pd.read_sql("""
SELECT *
FROM estacoes
""", conn)

conn.close()
st.subheader("📍 Minha localização")

location = streamlit_geolocation()

lat_usuario = None
lon_usuario = None

if location:

    lat_usuario = location.get("latitude")
    lon_usuario = location.get("longitude")

    if lat_usuario and lon_usuario:

        st.success(
            f"Latitude: {lat_usuario:.6f} | Longitude: {lon_usuario:.6f}"
        )

st.divider()

CARTO_KEY = "cb1_5b4e_1_ec7796dac313c8b382271e46"

m = folium.Map(
    location=[-15.8, -47.9],
    zoom_start=4,
    tiles=None
)
if lat_usuario and lon_usuario:

    folium.Marker(
        [lat_usuario, lon_usuario],
        popup="📍 Minha posição",
        tooltip="Minha posição",
        icon=folium.Icon(
            color="red",
            icon="user"
        )
    ).add_to(m)
    from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return R * c


if lat_usuario and lon_usuario:

    df["distancia_km"] = df.apply(
        lambda r: haversine(
            lat_usuario,
            lon_usuario,
            float(r["latitude"]),
            float(r["longitude"])
        ),
        axis=1
    )
if lat_usuario and lon_usuario:

    df["distancia_km"] = df.apply(

        lambda x: haversine(

            lat_usuario,
            lon_usuario,

            float(x["latitude"]),
            float(x["longitude"])

        ),

        axis=1

    )

    estacao_proxima = (

        df
        .sort_values("distancia_km")
        .iloc[0]

    )

    st.success(

        f"""
        🛰 Estação mais próxima: {estacao_proxima['mountpoint']}

        📏 Distância: {estacao_proxima['distancia_km']:.2f} km
        """

    )
    st.info(

    f"""
    🎯 Estação recomendada:

    {estacao_proxima['mountpoint']}

    📏 Distância em linha reta:
    {estacao_proxima['distancia_km']:.2f} km
    """

)

    proximas = (

        df
        .sort_values("distancia_km")
        .head(10)

    )

    folium.TileLayer(
    tiles=f"https://basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}.png?key={CARTO_KEY}",
    attr="CARTO Voyager",
    name="CARTO Voyager",
    overlay=False,
    control=True
).add_to(m)

for _, r in df.iterrows():

    distancia = ""

    cor = "blue"

    if lat_usuario and lon_usuario:

        distancia = f"""
        <br>
        Distância até você:
        {r['distancia_km']:.2f} km
        """

        if r["mountpoint"] == estacao_proxima["mountpoint"]:
            cor = "green"

    popup = f"""
    <b>{r['mountpoint']}</b><br>

    Nome: {r['nome']}<br>

    RTCM: {r['formato_rtcm']}<br>

    Rede: {r['rede']}<br>

    Receptor: {r['receptor']}<br>

    Constelações: {r['constelacoes']}

    {distancia}
    """

    folium.CircleMarker(

        location=[
            float(r["latitude"]),
            float(r["longitude"])
        ],

        radius=6,

        popup=folium.Popup(
            popup,
            max_width=350
        ),

        color=cor,

        fill=True,

        fill_color=cor,

        fill_opacity=0.8

    ).add_to(m)

    distancia = ""

if lat_usuario and lon_usuario:

    distancia = f"""

    <br>

    Distância até você: {r['distancia_km']:.2f} km

    """
    popup = f"""
    <b>{r['mountpoint']}</b><br>
    Nome: {r['nome']}<br>
    RTCM: {r['formato_rtcm']}<br>
    Rede: {r['rede']}<br>
    Receptor: {r['receptor']}<br>
    Constelações: {r['constelacoes']}<br>
    {distancia}
    """

    folium.CircleMarker(

        location=[
            float(r["latitude"]),
            float(r["longitude"])
        ],

        radius=5,

        popup=popup,

        color="blue",

        fill=True

    ).add_to(m)

st_folium(
    m,
    width=1400,
    height=700
)
