import streamlit as st
from streamlit_option_menu import option_menu
from _Pages.Login_SignUp import app as loginsignup_app
from _Pages.Classes import app as classes_app
from _Pages.Details import app as details_app
from _Pages.ViewImages import app as viewimages_app
from _Pages.ViewVideos import app as viewvideos_app
from _Pages.Account import app as accounts_app  
from _Pages.AboutUs import app as aboutus_app
from _Pages.Training import app as training_app
from _Pages.UploadImages import app as uploadimages_app

if "is_logged_in" not in st.session_state:
    st.session_state['is_logged_in'] = False


def logout():
    if st.sidebar.button("Log out, Click Me Twice :pensive:"):
        st.session_state['is_logged_in'] = False
    
       
if st.session_state['is_logged_in']:
    with st.sidebar:
        page = option_menu(
            "Main Menu", 
            ["About Us", "YOLOv8 Features", "Account"], 
            icons=["question-circle", "gear", "person"], 
            menu_icon="cast", 
            default_index=0
        )

    if page == "YOLOv8 Features":
        sub_page = option_menu(
            "Features", 
            ["Model Training Notebook", "Class Names", "Model Details","View Saved Images", "View Saved Videos", "Upload Image"], 
            icons=["book", "file-earmark-text", "tools","image", "film", "upload"],
            default_index=0
        )

        if sub_page == "Model Training Notebook":
            training_app()
        elif sub_page == "Class Names":
            classes_app()
        elif sub_page == "Model Details":
            details_app()
        elif sub_page == "View Saved Images":
            viewimages_app()
        elif sub_page == "View Saved Videos":
            viewvideos_app()
        elif sub_page == "Upload Image":
            uploadimages_app()
    
    elif page == "About Us":
        aboutus_app()
        

    elif page == "Account":
        accounts_app()  

    logout()

else:
    loginsignup_app()
