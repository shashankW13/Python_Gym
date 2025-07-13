import streamlit as st
import pandas as pd

st.write("Hello World")
name = st.text_input("Enter your name")
st.write(f"Your name {name}")

data = pd.read_csv('netflix_titles.csv')
st.write(data)