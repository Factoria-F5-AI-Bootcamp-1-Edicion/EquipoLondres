# importar librerias
from streamlit_folium import st_folium
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import pydeck as pdk
import folium
import streamlit_folium
import streamlit.components.v1 as components
import graficas 
# Comienza el programa


def main():
    #st.set_page_config(page_title="Information", page_icon="🧾")
    # Configuracion de la web

    st.title('Análisis de precios')
    st.markdown('<style>' + open('./styles.css').read() + '</style>', unsafe_allow_html=True)
    
    st.markdown('El panel visualiza la situacion de ...')
    st.markdown(
        'La espectativas de precios en el mercado inmobiliario de londres..')
    st.sidebar.header('User Input Parameters')
    st.text('Esto es una prueba')
    st.write()


# DataFrame
token = "pk.eyJ1Ijoid2VubGxhIiwiYSI6ImNsNnhmcjFmcjBzbjQzZHFsNXB3YXc0cHAifQ.Yhi8lAIuVUiXA8TltkAMIw"
fichero = ('london_airbnb.csv')


@st.cache(persist=True)
def load_data():
    df = pd.read_csv(fichero)
    return df


# guardamos los datos para usar
leer_data = load_data()

# pruebas mapa

m = folium.Map(location=[51.509865, -0.118092], zoom_start=12)
i = 0
# cuantos buscar
# precio
precios_londres = st.slider("Precio locales:", 10, 1000)

print(len(leer_data['price']))

for i in range(len(leer_data['id'])):
    print(f'iterando: {i}')
    if precios_londres > leer_data['price'][i]:
        latitud = leer_data['latitude'][i]
        longitud = leer_data['longitude'][i]
        precio = leer_data['price'][i]
        noches = leer_data['minimum_nights'][i]
        visitas = leer_data['number_of_reviews'][i]
        items = folium.Marker(
            [latitud, longitud],
            popup=f' valoración: {visitas}, noches {noches}',
            tooltip=f'{precio} libras'
        ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=625)


# visualiza imagenes
a1, a2, a3 = st.columns(3)
a1.image(Image.open('Airbnb red.png'))
a2.image(Image.open('London.jpg'))
a3.image(Image.open('Airbnb_logo.jpg'))


# pintamos dataframe
# st.dataframe(leer_data)  Descomentar en la presentacion, gasta muchos recursos.


# Mapa general
#precio = st.slider('Precio', 0, 130, 25)
#st.write("Precio: ", precio, 'Libras')
#st.map(leer_data[{'latitude', 'longitude'}],zoom=None, use_container_width=True)

#precios_londres = st.slider("Precio locales:", 0, 10000)


viviendas_por_precio = 0

for i in leer_data['price']:
    if i <= precios_londres:
        viviendas_por_precio += 1

st.markdown(f"Numero total de viviendas: {viviendas_por_precio} ")

# st.write((precios_londres > leer_data['price'].all(
# )) and leer_data[{"latitude", "longitude", "price"}])
# .bool(), a.item(), a.any() or a.all().
#df = leer_data[{"latitude", "longitude"}]

# mapa simple
#st.map(leer_data[{"latitude", "longitude"}].dropna(how='any'))


# Funcones del menu
def scatterplot():

    fig = plt.figure(figsize=(10, 4))
    sns.color_palette("hls", 5)
    sns.scatterplot(data=leer_data, x="latitude", y="longitude", hue="price")
    st.pyplot(fig)


def nosotros():
    st.markdown(
        """
        19/08/2022
        
        Autores:
        
        * [Víctor Arbiol](https://www.linkedin.com/in/victor-arbiol/)
        * [Yuan Chen](www.linkedin.com/in/)
        * [Alexandra](https://www.linkedin.com/in/)
        * [Christian](https://www.linkedin.com/in/)

        ---
        
        * **Artículo Medium** [Medium](https://medium.com/)
        * **Código fuente:** [GitHub](https://github.com/)

        
        """
    )
# iframe
#import streamlit.components.v1 as components
components.iframe("https://trade.mql5.com/trade?servers=SomeBroker1-Demo,SomeBroker1-Live,SomeBroker2-Demo,SomeBroker2-Live&amp;trade_server=SomeBroker-Demo&amp;startup_mode=open_demo&amp;lang=en&amp;save_password=off")

# Configuración del Menu
page = st.sidebar.selectbox(
    "Select a Page",
    [
        "Elige", "scatterplot", "nosotros"
    ]
)
# Llamadas al menu
#scatterplot()
#nosotros()

#print(graficas.yuan("Chen"))
graficas.yuan(load_data(), token)

# fn del programa
if __name__ == '__main__':
    main()
