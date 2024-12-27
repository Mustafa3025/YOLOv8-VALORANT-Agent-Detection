import streamlit as st

from _Authentication.Login import Login
from _Authentication.SignUp import SignUp


def app():
    
    st.title(" :wave: :orange[Welcome] 🔐")

    choice = st.selectbox("Login or Signup", ["Login", "Register"])

    if choice == "Login":
        login_obj = Login()
        if login_obj.login():
            st.session_state['is_logged_in'] = True
            st.session_state['username'] = login_obj.username

    else:
        signup_obj = SignUp()
        signup_obj.signup()