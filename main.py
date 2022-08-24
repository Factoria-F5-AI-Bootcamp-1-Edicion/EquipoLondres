# importar librerias

import streamlit as st
import folium
from folium.plugins import MarkerCluster
from folium import plugins
import streamlit_folium
import streamlit.components.v1 as components
from streamlit_folium import st_folium
import pickle
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import pydeck as pdk
from streamlit_card import card
from wordcloud import WordCloud, ImageColorGenerator
import plotly.express as px
# extra
import graficas


# Comienza el programa
def main():

    # Configuracion de css
    st.markdown('<style>' + open('./styles.css').read() +
                '</style>', unsafe_allow_html=True)
    

# Contenedores
Head = st.container()
Body = st.container()
Footer = st.container()
st.sidebar.title("Filtros")
# Cabecera
with Head:
    st.title('Análisis de precios')
    st.header('Londres AirBnB')
    st.text('Ciency tu consultora de confianza.')
#video
    video_file = open('istockphoto-1258113642-640_adpp_is.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    # visualiza imagenes
    a1, a2, a3 = st.columns(3)
    a1.image(Image.open('Airbnb red.png'))
    a2.image(Image.open('London.jpg'))
    a3.image(Image.open('Airbnb_logo.jpg'))

# cuerpo de la pagina
with Body:
    st.markdown(
        'La espectativas de precios en el mercado inmobiliario de londres..')


# pie de pagina
with Footer:
    st.header('Mapa de resultados')
    st.text('Grafica resultante.')



# DataFrame
token = "pk.eyJ1Ijoid2VubGxhIiwiYSI6ImNsNnhmcjFmcjBzbjQzZHFsNXB3YXc0cHAifQ.Yhi8lAIuVUiXA8TltkAMIw"
path_to_data = ('london_airbnb.csv')


@st.cache(persist=True)
def load_data():
    df = pd.read_csv(path_to_data)
    
    # Comienzo la limpieza de datos no definitiva
    df.drop(["host_id", "name", "host_name", ], axis=1, inplace=True)
    df.dropna(how='any')
    return df


# guardamos los datos para usar
leer_data = load_data()


# Localización del mapa
mapa = folium.Map(location=[51.509865, -0.118092], zoom_start=12)
i = 0

# Busca por precio
precios_londres = st.slider("Precio locales:", 10, 1000)

# print(len(leer_data['price']))

for i in range(len(leer_data['id'])):
    print(f'iterando: {i}')
    if precios_londres >= leer_data['price'][i]:
        latitud = leer_data['latitude'][i]
        longitud = leer_data['longitude'][i]
        precio = leer_data['price'][i]
        alquiler = leer_data['room_type'][i]
        noches = leer_data['minimum_nights'][i]
        visitas = leer_data['number_of_reviews'][i]
        items = folium.Marker(
            [latitud, longitud],
            popup=f' valoración: {visitas}, noches {noches}, alquiler{alquiler}',
            tooltip=f'{precio} libras'
        ).add_to(mapa)

# call to render Folium map in Streamlit
st_data = st_folium(mapa, width=625)


# pintamos dataframe
# st.dataframe(leer_data)  Descomentar en la presentacion, gasta muchos recursos.


viviendas_por_precio = 0

for i in leer_data['price']:
    if i <= precios_londres:
        viviendas_por_precio += 1

st.markdown(f"Numero total de viviendas: {viviendas_por_precio} ")


# Funcones del menu
def scatterplot():
    print('123')

scatterplot() #borrar prueba

def nosotros():
    # Render the h1 block, contained in a frame of size 200x200.
    st.title('THE TEAM')
    components.html(
'''
<div class="row">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Ciency</h5>
         <img src="https://thispersondoesnotexist.com/image" width="200" height="200"> 
         <img src="https://thispersondoesnotexist.com/image" width="200" height="200"> 
         <img src="https://thispersondoesnotexist.com/image" width="200" height="200"> 
         <img src="https://thispersondoesnotexist.com/image" width="200" height="200"> 
        <p class="card-text">Alexandra CEO.    Alexandra CEO.    Alexandra CEO.    Alexandra CEO.</p>
      </div>
    </div>
  </div>
</div>
''', width=1200, height=200)

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


#res = card(
#    title = "Chen",
#    text="CEO ",
#    image="https://placekitten.com/100/100",        
#)

#print(res)

# iframe
#import streamlit.components.v1 as components
# components.iframe("https://trade.mql5.com/trade?servers=SomeBroker1-Demo,SomeBroker1-Live,SomeBroker2-Demo,SomeBroker2-Live&amp;trade_server=SomeBroker-Demo&amp;startup_mode=open_demo&amp;lang=en&amp;save_password=off")

#################################################################################### 
st.sidebar.title("Configuración")
# Mostrar por barrio
# Obtengo los elementos unicos de la columna room_type
list = np.unique(leer_data["room_type"])

if st.sidebar.checkbox("Mostrar grafica de Barrio", False, key=1):
    fig, ax = plt.subplots(ncols=1, figsize=(18, 7))
    sns.boxplot(y='price', x='neighbourhood', data=leer_data, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)


##################################################################################

# Configuración del Menu
page = st.sidebar.selectbox( "Seleciona grafica B",
    [
        "Elige", "scatterplot", "nosotros"
    ]
)
if page == 'scatterplot':
    scatterplot()
if page == 'nosotros':
    nosotros()





# print(graficas.yuan("Chen"))
graficas.yuan(leer_data, token)


#nosotros()

# fn del programa
if __name__ == '__main__':
    main()
