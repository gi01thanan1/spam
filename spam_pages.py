import streamlit as st
#from PIL import Image
import numpy as np
import pandas as pd
import string
from nltk.stem import PorterStemmer

hide_streamlit_style = """

    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
    
    
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.image("email.jpeg")
stemmer = PorterStemmer()
def custom_tokenizer(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    #tokens = word_tokenize(text)
    # Stem
    #stemmed = [stemmer.stem(word) for word in tokens]
    stemmed = [stemmer.stem(word) for word in text]
    return stemmed

pg = st.navigation([st.Page("Home.py",title="Welcome", icon="👋"), st.Page("preprocessing.py"),st.Page("spam Prediction.py")])#":material/target:")])

pg.run()