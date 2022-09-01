
import altair as alt
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib as plt
from streamlit_vega_lite import vega_lite_component, altair_component


#ESTRUCTURA DE PÁGINA

# Título principal
st.title(":bar_chart: Mi buscador")
st.markdown("##")

#Texto introductorio
st.text('Visualizaremos los datos de nuestro interés usando los filtros.')
st.text(' Datos basados en la data de Londres_airbnb.')

# Título secundario
st.write("### DataFrame")

#READ DATAFRAME
#df = pd.read_csv ('london_airbnb.csv',
#)

#st.dataframe(df)

# DATAFRAME FILTRADO
@st.cache(persist=True)
def load_data():
    df = pd.read_csv('london_airbnb.csv')

# Comienzo la Ingenieria de caracteristicas
    df.drop(["neighbourhood_group","id", "name","host_id","host_name"], axis=1, inplace=True)
    df.dropna(how='any')
    modaprice = df["price"].mode()[0]
    df['price'] = df['price'].replace([0], modaprice)
    return df

df = load_data()

print(df)

#Filtrar DataFrame

#Por vecindarios
st.sidebar.header("Filtrar:")
neighbourhood = st.sidebar.multiselect(
    "Seleccione el barrio de su interés:",
    options=df["neighbourhood"].unique(),
    default=df["neighbourhood"].unique()
)

#Por tipo de habitación
room_type = st.sidebar.multiselect(
    "Seleccione el tipo de alojamiento de su interés:",
    options=df["room_type"].unique(),
    default=df["room_type"].unique()
)

#Nueva variable para dar funcionalidad al filtrado
#query
df_selection = df.query (
    "neighbourhood == @neighbourhood & room_type == @room_type"
)

st.dataframe(df_selection)







