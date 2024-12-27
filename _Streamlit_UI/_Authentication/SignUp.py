import streamlit as st
from _Authentication.UserData import UserData


class SignUp:
    
    def __init__(self, data = UserData()):
        
        self.db = data
        self.data = self.db.load_user_data()

    def signup(self):

        username = st.text_input("Enter a unique username")
        password = st.text_input("Enter a password", type = 'password')
        confirmpassword = st.text_input("confirm password", type = 'password')

        if st.button("Create Account"):
            
            if username in self.data:
                st.error(f"Username {username} is taken")
            else:
                if password != confirmpassword:
                    st.error("Passwords do not match, please try again")
                else:
                    self.data[username] = {
                        'username': username,
                        'password': password
                    }
                    self.db.save_user_data(self.data)
                    st.success(f"Account Creation Successful! :party: ")