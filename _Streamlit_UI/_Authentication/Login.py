import streamlit as st
from _Authentication.UserData import UserData


class Login:

    def __init__(self, data = UserData()):
        self.data = data.load_user_data()
        self.username = None

    def login(self):
        
        if 'is_logged_in' not in st.session_state:
            st.session_state['is_logged_in'] = False

        username = st.text_input("Enter you username")
        password = st.text_input("Enter your password", type = 'password')

        if st.button("Login"):
            if username not in self.data:
                st.error(f"Username {username} does not exist")
            elif username in self.data:
                if self.data[username]['password'] != password:
                    st.error("Incorrect password, please try again :pensive:")
                else:
                    st.success(f"Welcome {username} :smile:")
                    st.session_state['is_logged_in'] = True
                    st.session_state['username'] = username
                    self.username = username
                    st.rerun()