import streamlit as st
import folium
import pandas as pd
from st_on_hover_tabs import on_hover_tabs
# extra
#import graficas


# Comienza el programa
def main():

    # Configuracion de css
    st.markdown('<style>' + open('./styles.css').read() +
                '</style>', unsafe_allow_html=True)

#from st_on_hover_tabs import on_hover_tabs
#import streamlit as st
st.set_page_config(layout="wide")

st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Money', 'Economy'], 
                         iconName=['dashboard', 'money', 'economy'], default_choice=0)

if tabs =='Dashboard':
    st.title("Navigation Barq")
    st.write(f'Name of option is {tabs}')

elif tabs == 'Money':
    st.title("Paper")
    st.write(f'Name of option is {tabs}')

elif tabs == 'Economy':
    st.title("Tom")
    st.write(f'Name of option is {tabs}')
    
    