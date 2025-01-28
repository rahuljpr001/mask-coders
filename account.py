import streamlit as st
def app():
    st.title("welcome to :blue[MASK CODERS]")
    choice=st.selectbox("LOGIN/SING-UP",["LOGIN","SING-UP"])
    email=st.text_input("EMAIL")
    password=st.text_input("PASSWORD",type="password")
    login=st.button("LOGIN")
    
    
    
