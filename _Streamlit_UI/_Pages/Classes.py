import streamlit as st
from pathlib import Path
from ultralytics import YOLO
from PIL import Image

def display_icons(path):
    
    icons = []

    for f in path.iterdir():
        if f.suffix in {'.png'}:
            icons.append(f)
      
    number_of_columns = 4

    columns = st.columns(number_of_columns)
    
    for index, icon_path in enumerate(icons):
        icon = Image.open(icon_path)

        column = columns[index % number_of_columns]
        column.image(icon, caption = icon_path.stem, use_container_width= True)  


def app(model_path = Path("models/yolov8.pt"), 
        icons_path_done = Path('_Pages/icons_agents_done'),
        icons_path_in_progress = Path('_Pages/icons_agents_in_progress'),
        icons_path_pending = Path('_Pages/icons_agents_pending')
        ):

    model = YOLO(model_path)
    st.title("Model Class Names 📑")
    st.write("The model is trained to detect the following classes")
    st.json(model.names)

    st.write("# Agent Done")   
    display_icons(icons_path_done)

    
    st.write("# Agent In Progress")   
    display_icons(icons_path_in_progress)

    
    st.write("# Agent Pending")   
    display_icons(icons_path_pending)