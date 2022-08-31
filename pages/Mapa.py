import streamlit as st
import folium
import pandas as pd
from PIL import Image
from streamlit_folium import st_folium


# Comienza el programa
def main():

    # Configuracion de css
    st.markdown('<style>' + open('./styles.css').read() +
                '</style>', unsafe_allow_html=True)


# Contenedores
Head = st.container()
Body = st.container()
Footer = st.container()



# Cabecera
with Head:
    st.title('Buscador por precios')
    st.markdown('## Ciency tu consultora de confianza.')


# cuerpo de la pagina
with Body:
    #lectura de datos
    path_to_data = ('london_airbnb.csv')

# Carga de datos y filtrado
@st.cache(persist=True)
def load_data():
    df = pd.read_csv(path_to_data)

    # Comienzo la Ingenieria de caracteristicas
    df.drop(["neighbourhood_group", "id", "name",
            "host_id", "host_name"], axis=1, inplace=True)
    df.dropna(how='any')
    modaprice = df["price"].mode()[0]
    df['price'] = df['price'].replace([0], modaprice)
    return df


# guardamos los datos para usar
leer_data = load_data()


# Localización del mapa
mapa = folium.Map(location=[51.509865, -0.118092], zoom_start=12)
i = 0

# Busca por precio de 10 hasta  500
precios_londres = st.slider("Precio locales:", 10, 500)

# Ciclo de pintura jajajaja
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

# Renderizacion del mapa.
st_data = st_folium(mapa, width=625)


# pie de pagina
with Footer:
    
    st.text('Mapa de resultados.')
