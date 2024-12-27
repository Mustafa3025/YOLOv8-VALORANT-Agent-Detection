import streamlit as st
from PIL import Image
from pathlib import Path

def app(output_directory = Path("Output/images")):

    st.title("View Saved Images :camera:")
    st.write("Select an image to view it")

    saved_images = []
    for f in output_directory.iterdir():
        if f.suffix in {'.png', '.jpg', '.jpeg'}:
            saved_images.append(f.name)

    if saved_images:
        image_name = st.selectbox("Select an Image", saved_images)
        image_path = Path(output_directory)/image_name

        image = Image.open(image_path)
        st.image(image, caption = image_name, use_container_width = True)
    else:
        st.write("No saved images found :sad:")