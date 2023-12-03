import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')
headers = df.columns
print(headers)


st.title('In Search for Happiness')
a = st.selectbox('Select the data for the X-axis', [i for i in headers], key='X')
b = st.selectbox('Select the data for the Y-axis', [i for i in headers], key='Y')
subtitle = st.subheader(f'{a.capitalize()} and {b.capitalize()}')
figure = px.scatter(x=df[a], y=df[b], labels={'x': a.capitalize(), 'y': b.capitalize()})
st.plotly_chart(figure)
