import pandas as pd
import streamlit as st
import plotly.express as px 
import folium

# [selectbox, image] -> display an image
st.header("Images")
pics = {
"Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
"Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
"Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg"
}
pic = st.selectbox("Picture choices", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True, caption=pics[pic])

# [button, balloons] -> built-in animation
st.markdown("## London time!")
st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
	st.balloons() 


# muestra el precio en euros las zonas mas caras
# [subheader, map] -> display data on map

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

leer_data = load_data()

st.header("Where are the most expensive properties located?")
st.subheader("Airbnb más caros")
st.markdown("El siguiente mapa muestra el 1% de los Airbnb más caros con un precio de xxxx euros o más..")
st.map(leer_data).query("price>=800")[["latitude", "longitude"]].dropna(how="any")


