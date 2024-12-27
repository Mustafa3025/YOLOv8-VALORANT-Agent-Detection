import streamlit as st
from pathlib import Path
from ultralytics import YOLO
import json
import numpy as np
import cv2


def save_image_counter(counter, counter_file_path = Path('counter_file.json')):
    with open(counter_file_path, "w") as f:
        json.dump({"counter": counter}, f)


def load_image_counter(counter_file_path = Path('counter_file.json')):
    if counter_file_path.exists():
        with open(counter_file_path, "r") as f:
            data = json.load(f)
            return data.get("counter", 1)
    return 1 


def app(model_path = Path('models/yolov8.pt'),
        output_directory = Path('Output/images')):
    
    model = YOLO(model_path)
    counter = load_image_counter()
    st.title("Upload Images")

    uploaded_file = st.file_uploader("Choose an image to process", type = ["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()))
        image = cv2.imdecode(file_bytes, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(image_rgb, caption = "Uploaded Image", use_container_width = True)
        st.write("Processing image...............")

        results = model(image, imgsz = 640)
        annotated_frame = results[0].plot()
        
        #annotated_frame = cv2.imdecode(file_bytes, 1)
        #annotated_frame_fixed = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

        st.image(annotated_frame, caption = "Predicted Image", use_container_width = True)

        st.write("Prediction Details")

        if hasattr(results[0], 'boxes'):
                st.json(results[0].boxes.data.tolist())

        output_file_path = output_directory / f"Predicted_image_{counter}.png"
        cv2.imwrite(str(output_file_path), annotated_frame)
        
        counter += 1
        save_image_counter(counter)

        st.write(f"Image saved as {output_file_path}")

