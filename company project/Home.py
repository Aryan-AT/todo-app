import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

data = pandas.read_csv("004 data.csv")
topics = pandas.read_csv("004 topics.csv")

with col1:
    for index, row in data[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("004 images/" + row["image"])

with col2:
    for index, row in data[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("004 images/" + row["image"])

with col3:
    for index, row in data[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("004 images/" + row["image"])
