import streamlit as st
import pandas #use to read CSV data

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("006 images/photo.png")

with col2:
    st.title("Aryan Thakkar")
    content = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    st.info(content)

content2 = """
Below you can find some of the apps. I have built in python. Feel free to conatact me!"
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("006 data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])