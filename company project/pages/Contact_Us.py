import streamlit as st
from Home import topics

with st.form(key="Email_form"):
    user_email = st.text_input("Your Email Address")

    select_box = st.selectbox('What topics do you want to discuss?', (topics['topic']))

    raw_message = st.text_area("Your message ")

    message = f"""/
Subject: New email from {user_email}

From:{user_email}
Topic {select_box}
{raw_message}
"""

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your email was sent")