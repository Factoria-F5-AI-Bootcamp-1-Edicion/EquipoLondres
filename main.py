#importar librerias
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

def main():
    #titulo
    st.title('Análisis de precios')
    st.markdown('El panel visualiza la situacion de ...')
    st.markdown('La espectativas de precios en el mercado inmobiliario de londres..')
    #titulo de sidebar
    st.sidebar.header('User Input Parameters')
    st.text('Esto es una prueba')
    st.write()
    st.dataframe()
    st.map()

fichero=('london_airbnb.csv')
@st.cache(persist=True)

def load_data():
    data=pd.read_csv(fichero)
    return data

leer_data = load_data()

st.markdown(leer_data)

#Visualizacion de datos






'''st.sidebar.checkbox('Muestra el Analisis por barrio', True, Key=1)
select = st.sidebar.selectbox('Selecciona barrio', df['barrio'])

barrio_data = df[df['barrio'] == select]
select_status = st.sidebar.radio('precio',('Confirmar','barato', '',''))
'''
#trazar graficos
def get_total_dataframe(dataset):
    get_total_dataframe = pd.DataFrame({
    })

if __name__ == '__main__':
    main()
    