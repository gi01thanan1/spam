import streamlit as st
import numpy as np
import pandas as pd


st.markdown("<h3 style='color: #FF5733;'>Email before cleaning and preprecessing</h3>", unsafe_allow_html=True)
df_origin = pd.read_csv('df_20.csv')
df_origin.drop("Unnamed: 0",axis=1,inplace=True)
# st.dataframe(df_origin.style.background_gradient(cmap='Blues'))
text_0=df_origin['text'].iloc[0]
st.write(text_0)


st.markdown("<h3 style='color: #2AF527;'>Email after cleaning,remove punctuation,remove stopwords and stemming</h3>", unsafe_allow_html=True)

df_corpus = pd.read_csv('corpus_df_20.csv')
df_corpus.drop("Unnamed: 0",axis=1,inplace=True)
# st.dataframe(df_corpus.style.background_gradient(cmap='Blues'))
text_0=df_corpus['0'].iloc[0]
st.write(text_0)