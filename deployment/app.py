import streamlit as st
import eda
import prediction
import about_me


nav = st.sidebar.selectbox('Pilih halaman:', ('EDA', 'About Me', 'Forecast Model'))

if nav == 'EDA':
    eda.run()
elif nav == 'About Me':
    about_me.run()
else:
    prediction.run()


