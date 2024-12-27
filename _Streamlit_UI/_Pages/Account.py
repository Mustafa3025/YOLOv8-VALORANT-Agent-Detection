import streamlit as st

def app():
    st.title("Account Details 👨‍💼")
    username = st.session_state["username"]
    st.write(f"## Name: {username}") 
    #st.write(st.session_state)


    
  
