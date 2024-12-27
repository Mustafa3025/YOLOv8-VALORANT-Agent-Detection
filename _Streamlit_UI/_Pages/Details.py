import streamlit as st
from pathlib import Path
from ultralytics import YOLO


def app(model_path = Path("models/yolov8.pt")):

    model = YOLO(model_path)
    st.title("Model Saved Details 📋🗃️")
    st.json(model.overrides)


    st.subheader("Model Architecture 🏗️")

    # Convert model to a string format for clean output
    model_summary = str(model.model)

    # Display the model summary as clean formatted code block
    st.code(model_summary, language="python")