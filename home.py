import streamlit as st
import pandas as pd

st.title("🎶website Deverloping using Python🎶")
st.header("website Deverloping using Python")

st.image('./img/IMG_7218.webp')
st.subheader("Nattawat MTV🧸🎧🎸")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.warning(dt.head(10))