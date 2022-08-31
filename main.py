# importar librerias
from streamlit_embedcode import github_gist
from streamlit_observable import observable
from streamlit_echarts import Map
from streamlit_agraph import TripleStore, agraph
from streamlit_d3_demo import d3_line
import random
import streamlit as st
import streamlit.components.v1 as components
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import pydeck 

from st_aggrid import AgGrid
from streamlit_agraph import agraph
from annotated_text import annotated_text

from wordcloud import WordCloud, ImageColorGenerator
import plotly.express as px

#extra
from PIL import Image


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
    st.title('Vacaciones en londres')
    st.header('Londres AirBnB')
    
    londres = Image.open('londres.jpg')
    logo = Image.open('Airbnb_logo.jpg')
    st.image(londres, caption='Sunrise by the mountains')

    st.text('SCIENCE es sinonimo de confianza.')
# video
    video_file = open('istockphoto-1258113642-640_adpp_is.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

# cuerpo de la pagina
with Body:
    st.markdown(
        'Precios de alquiler en la ciudad de londres')

    # visualiza imagenes
    #a1, a2, a3 = st.columns(3)
    #a1.image(Image.open('Airbnb red.png'))
    #a2.image(Image.open('casa.jpg'))
    #a3.image(Image.open('Airbnb_logo.jpg'))




# DataFrame
token = "pk.eyJ1Ijoid2VubGxhIiwiYSI6ImNsNnhmcjFmcjBzbjQzZHFsNXB3YXc0cHAifQ.Yhi8lAIuVUiXA8TltkAMIw"
path_to_data = ('london_airbnb.csv')


@st.cache(persist=True)
def load_data():
    df = pd.read_csv(path_to_data)

    # Comienzo la Ingenieria de caracteristicas
    df.drop(["neighbourhood_group","id", "name","host_id","host_name"], axis=1, inplace=True)
    df.dropna(how='any')
    
    #reemplazar datos Na
    promedio = df["reviews_per_month"].mean()
    df["reviews_per_month"].fillna(promedio, inplace=True)
    mode_review = df["last_review"].mode()[0]
    df["last_review"].fillna(mode_review, inplace=True)

    #eNcontrar valores en cero y reemplazarlo
    modaprice = df["price"].mode()[0]
    df['price'] = df['price'].replace([0], modaprice)

    return df

st.title('SCIENCE STARTUD')

st.markdown(
    
    """
    Si estas pensando en viajar a londres y necesitas encontrar el alojamiento perfecto para ti, 
    has llegado al lugar indicado.
    En nuestra startup damos solucion a esto, podras buscar tu lugar ideal, al precio que mejor se adapte a ti.
    
          """  )


# guardamos los datos para usar
leer_data = load_data()

    
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


####################################################################################
nosotros()


# nosotros()

# fn del programa
if __name__ == '__main__':
    main()
