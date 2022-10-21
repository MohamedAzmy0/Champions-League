import streamlit as st
import pandas as pd
import plotly_express as px
import webbrowser

st.set_page_config (page_title='Uefa Champions League', page_icon='⚽', layout='wide')
st.title('Uefa Champions League :soccer:')
st.markdown(''' 
This is a simple web app to show the stats of the Champions League 2021/2022 season ''' )
col1 , col2 = st.columns(2)
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.subheader('“Football is played with your head. Your feet are just the tools.”')
    st.subheader('\t \t \t \t \t \t  ― Andrea Pirlo')
with col2:
    st.image('wp10129848.jpg', width=600)

url = 'https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league'

if st.button('Click Here for Data Reference'):
    webbrowser.open_new_tab(url)

