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

from st_aggrid import AgGrid
from streamlit_agraph import agraph, Node, Edge, Config
from annotated_text import annotated_text

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


    fig = plt.figure(figsize=(10, 4))
    sns.color_palette("hls", 5)
    sns.scatterplot(data=leer_data, x="latitude", y="longitude", hue="price")
    st.pyplot(fig)

AgGrid(leer_data)

#mapa?
nodes = []
edges = []
nodes.append( Node(id="Spiderman", 
                   label="Peter Parker", 
                   size=400, 
                   svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                   size=400, 
                   svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   type="CURVE_SMOOTH") 
            ) # includes **kwargs

config = Config(width=500, 
                height=500, 
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)

# text colores
annotated_text(
    "This ",
    ("is", "verb", "#8ef"),
    " some ",
    ("annotated", "adj", "#faa"),
    ("text", "noun", "#afa"),
    " for those of ",
    ("you", "pronoun", "#fea"),
    " who ",
    ("like", "verb", "#8ef"),
    " this sort of ",
    ("thing", "noun", "#afa"),
    "."
)


#grafos 3d
import random
from streamlit_d3_demo import d3_line

def generate_random_data(x_r, y_r):
    return list(zip(range(x_r), [random.randint(0, y_r) for _ in range(x_r)]))

d3_line(generate_random_data(20, 500), circle_radius=15, circle_color="#6495ed")

# otro
from rdflib import Graph
from streamlit_agraph import TripleStore, agraph

graph = Graph()
graph.parse("http://www.w3.org/People/Berners-Lee/card")
store = TripleStore()

for subj, pred, obj in graph:
    store.add_triple(subj, pred, obj, "")
    
agraph(list(store.getNodes()), list(store.getEdges()), config)

#


algos = GraphAlgos(store)
algos.shortest_path("Spiderman", "Captain_Marvel")
algos.density()

#
from streamlit_echarts import Map
with open("USA.json", "r") as f:
    map = Map(
        "USA",
        json.loads(f.read()),
        {
            "Alaska": {"left": -131, "top": 25, "width": 15},
            "Hawaii": {"left": -110, "top": 28, "width": 5},
            "Puerto Rico": {"left": -76, "top": 26, "width": 2},
        },
    )
options = {...}
st_echarts(options, map=map)



#

from streamlit_observable import observable

@st.cache
def get_trader_joes():
    # a lot of code...
    return df

df = get_trader_joes()

observable("Trader Joes Voronoi Map", 
    notebook="@mbostock/u-s-voronoi-map-o-matic", 
    targets=["map"],
    redefine={
        "data": df[["longitude", "latitude", "name"]].to_dict(orient="records")
    }
)


from streamlit_embedcode import github_gist

github_gist("https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087/")

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
