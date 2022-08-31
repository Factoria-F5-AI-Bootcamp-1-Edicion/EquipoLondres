import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Leemos los datos de arrendador
df = pd.read_csv('london_airbnb.csv')

# Se preparan los datos
df['host_name'].fillna("0", inplace=True)
df['last_review'].fillna('2018-01-01', inplace=True)
df['last_review'] = pd.to_datetime(df['last_review'], format='%Y-%m-%d')
df['reviews_per_month'].fillna(0, inplace=True)
df = df.drop(columns='neighbourhood_group')

# Filtramos los datos
filtro = df[['host_name', 'name']].groupby(
    'host_name').count().sort_values(by='name', ascending=False)

#titulo
st.title("Concentrarion de arrendadores.")
st.markdown("### Por barrios. ")

#pinta grafica 1
st.line_chart(filtro)

# Sacamos las localizaciones
map_data = pd.DataFrame(df, columns=['latitude', 'longitude'])
#titulo
st.markdown("### Mapa por concentración. ")
# pinta mapa
st.map(map_data)

# datos a usar
values = df.neighbourhood.value_counts()
names = df.neighbourhood.unique().tolist()

# tipos de figura a usar
fig = px.pie(df, values=values, names=names)
fig.update_traces(textposition='inside', textinfo='percent+label')
st.markdown("### Barrios con más hospedaje. ")
# Se pinta la grafica
st.plotly_chart(fig)
