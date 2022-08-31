import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

#df y limpieza
df = pd.read_csv('london_airbnb.csv')

df['host_name'].fillna("0",inplace = True)
df['last_review'].fillna('2018-01-01',inplace = True)
df['last_review'] = pd.to_datetime(df['last_review'],format='%Y-%m-%d')
df['reviews_per_month'].fillna(0,inplace = True)
df = df.drop(columns='neighbourhood_group')

arr = df[['host_name','name']].groupby('host_name').count().sort_values(by='name', ascending=False)
st.line_chart(arr)


map_data = pd.DataFrame(df,columns=['latitude', 'longitude'])
st.map(map_data)


values = df.neighbourhood.value_counts()
names = df.neighbourhood.unique().tolist()
fig = px.pie(df, values=values, names=names)
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig)
