import streamlit as st
import pandas as pd

st.title("🎶website Deverloping using Python🎶")
st.header("website Deverloping using Python")

st.image('./image/IMG_7218.jpg')
st.subheader("Percc🦦")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))