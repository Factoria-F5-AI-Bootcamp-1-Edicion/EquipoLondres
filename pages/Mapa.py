import streamlit as st
import folium
import pandas as pd
from PIL import Image
from streamlit_folium import st_folium
# extra
#import graficas


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


# cuerpo de la pagina
with Body:
    st.markdown(
        'La espectativas de precios en el mercado inmobiliario de londres..')
path_to_data = ('london_airbnb.csv')


@st.cache(persist=True)
def load_data():
    df = pd.read_csv(path_to_data)

    # Comienzo la Ingenieria de caracteristicas
    df.drop(["neighbourhood_group","id", "name","host_id","host_name"], axis=1, inplace=True)
    df.dropna(how='any')
    modaprice = df["price"].mode()[0]
    df['price'] = df['price'].replace([0], modaprice)
    return df



# guardamos los datos para usar
leer_data = load_data()


# Localización del mapa
mapa = folium.Map(location=[51.509865, -0.118092], zoom_start=12)
i = 0

# Busca por precio
precios_londres = st.slider("Precio locales:", 10, 1000)


# print(len(leer_data['price']))

for i in range(len(leer_data['price'])):
    
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



# pie de pagina
with Footer:
    st.header('Mapa de resultados')
    st.text('Grafica resultante.')



# Configuración del Menu
page = st.sidebar.selectbox("Seleciona grafica B",
                            [
                                "Elige", "Barrio1", "barrio2"
                            ]
)

if page == 'Barrio1':
    barrio()
else:
    barrio()
