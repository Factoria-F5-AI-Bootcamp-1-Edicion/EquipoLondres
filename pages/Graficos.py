
import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
from streamlit_vega_lite import vega_lite_component, altair_component
path_to_data = ('london_airbnb.csv')
df = pd.read_csv(path_to_data)


@st.cache



# nuevo codigo
def scatterplot():

    fig = plt.figure(figsize=(10, 4))
    sns.color_palette("hls", 5)
    sns.scatterplot(data=df, x="latitude", y="longitude", hue="price")
    st.pyplot(fig)
scatterplot()