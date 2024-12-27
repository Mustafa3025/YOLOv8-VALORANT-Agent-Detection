import streamlit as st
from PIL import Image
from pathlib import Path


def app(output_directory = Path("Output/videos")):

    st.title("View Saved Videos 📹")
    st.write("Select an image to view it")

    saved_videos = []
    for f in output_directory.iterdir():
        if f.suffix in {'.mp4', '.webm', '.ogv', '.ogg'}:
            saved_videos.append(f.name)


    if saved_videos:
        video_name = st.selectbox("Select a Video", saved_videos)
        video_path = Path(output_directory)/video_name

        st.video(video_path)
    else:
        st.write("No saved videos found :sad: ")