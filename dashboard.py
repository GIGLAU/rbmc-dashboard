import sqlite3
import pandas as pd
import streamlit as st
import folium

st.link_button(
    "🔗 Dado retirado diretamente do IBGE",
    "http://170.84.40.52:2101/"
)

st.sidebar.button(
    "Atualizar RBMC"
)
from streamlit_folium import st_folium

st.set_page_config(
    page_title="RBMC Dashboard",
    layout="wide"
)
st.title("🛰️ Rede NTRIP - IBGE")

conn = sqlite3.connect("rbmc.db")

df = pd.read_sql("""
SELECT *
FROM estacoes
""", conn)

conn.close()

st.title("🛰️ Rede RBMC - IBGE")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Estações",
    len(df)
)

c2.metric(
    "GPS",
    df["constelacoes"].str.contains("GPS").sum()
)

c3.metric(
    "Galileo",
    df["constelacoes"].str.contains("GAL").sum()
)

c4.metric(
    "BeiDou",
    df["constelacoes"].str.contains("BDS").sum()
)

st.divider()

CARTO_KEY = "cb1_5b4e_1_ec7796dac313c8b382271e46"

m = folium.Map(
    location=[-15.8, -47.9],
    zoom_start=4,
    tiles=None
)

folium.TileLayer(
    tiles=f"https://basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}.png?key={CARTO_KEY}",
    attr="CARTO Voyager",
    name="CARTO Voyager",
    overlay=False,
    control=True
).add_to(m)

for _, r in df.iterrows():

    popup = f"""
    <b>{r['mountpoint']}</b><br>
    Nome: {r['nome']}<br>
    RTCM: {r['formato_rtcm']}<br>
    Rede: {r['rede']}<br>
    Receptor: {r['receptor']}<br>
    Constelações: {r['constelacoes']}
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
