import streamlit as st
import numpy as np
import pandas as pd
#from collections import Counter

st.write("# Welcome to Spam Detection 👋")
df_origin = pd.read_csv('df_20.csv')
df_origin.drop("Unnamed: 0",axis=1,inplace=True)
st.markdown(
    """
    ### Original Dataset :

    """)
st.dataframe(df_origin.style.background_gradient(cmap='Blues'))

result = " ".join(df_origin['text'][df_origin['spam'] == 1].to_list())
result = result.split(" ")
s = pd.Series(result)
cnt = s.value_counts()
k = 20  # Top 20 most frequent words
top_k = cnt.head(k)

st.markdown(
    """
    ### Description of columns:
    - text: subject and body of email
    - spam: 1 for spam email and 0 for ham email
    ### Comment on dataset:
    
    - Contains punctuation 
    - It needs cleaning and word stemming
    
    ### most 20 common words in spam email :
    

    """)
st.write(top_k)

st.markdown(
    """
    ### most 20 common words in ham email :

    """)
result = " ".join(df_origin['text'][df_origin['spam'] == 0].to_list())
result = result.split(" ")
s = pd.Series(result)
cnt = s.value_counts()
k = 20  # Top 20 most frequent words
top_k = cnt.head(k)
st.write(top_k)