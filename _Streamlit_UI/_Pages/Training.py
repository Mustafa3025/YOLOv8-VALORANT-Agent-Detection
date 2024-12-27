import streamlit as st
from pathlib import Path
from PIL import Image
import json

def app(notebooks_directory=Path("_jupyter_notebooks_collab/"),
        images_directory=Path("_jupyter_notebooks_collab/Attemp03_images")):



    # Select and display an image regarding the model training
    #images = [f.name for f in images_directory.iterdir() if f.suffix in {'.png', '.jpg', '.jpeg'}]
    
    images = []

    for f in images_directory.iterdir():
        if f.suffix in {'.png', '.jpg', '.jpeg'}:
            images.append(f.name)

    if images:
        selected_image = st.selectbox("Select an Image Regarding the Model Training", images)
        image_path = images_directory/selected_image
        image = Image.open(image_path)
        st.image(image, caption=selected_image, use_container_width=True)
    else:
        st.warning("No images found in the specified directory!")

    st.write("---")
    # Select an .ipynb file
    #notebooks = [f.name for f in notebooks_directory.iterdir() if f.suffix == '.ipynb']
    
    notebooks = []

    for f in notebooks_directory.iterdir():
        if f.suffix == '.ipynb':
            notebooks.append(f.name)
    
    if not notebooks:
        st.error("No Jupyter Notebook files found!")
        return

    selected_notebook = st.selectbox("Select a Notebook File", notebooks)
    notebook_path = notebooks_directory/selected_notebook

    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    # Extract code cells
    #code_cells = [cell['source'] for cell in notebook_data['cells'] if cell['cell_type'] == 'code']
    
    code_cells = []

    for cell in notebook_data['cells']:
        if cell['cell_type'] == 'code':
            code_cells.append(cell['source'])


    st.title(f"Notebook: {selected_notebook}")
    for cell in code_cells:
        st.code('\n'.join(cell), language="python")

    st.write("---")
    