import streamlit as st
import numpy as np
import pandas as pd
import joblib


st.write("#  Spam prediction")
# load model


my_model = joblib.load("gpt1_pipeline.joblib")


if 'my_text_input' not in st.session_state:
    st.session_state.my_text_input = ""
def clear_text_input():
    st.session_state.my_text_input = ""
col1, col2 = st.columns([3,1])
with col1:
    st.write("Enter email:")
    mail_text = st.text_input("Enter email :", key="my_text_input", label_visibility="collapsed")

with col2:
    st.write("press to clear:")
    st.button("Clear Text", on_click=clear_text_input)

predict = st.button("Predict")
if predict:
    pred = my_model.predict([mail_text])[0]
    if pred==1:
        st.text(f"prediction is : spam email ")
    if pred==0:
        st.text(f"prediction is : not spam email ")





