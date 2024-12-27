import streamlit as st

def app():

    st.title("Valorant Agent Detection using :violet[YOLOv8] 🎮🕹️👾")
    video_path = "AboutUsVideo.mp4"  
    st.video(video_path)
    st.write("---")
    st.subheader("**Intro to Training with ModelV8 Small for Valorant Agent Detection**")
    st.subheader(":red[DISCLAIMER] our model's accuracy is not that great when there are multiple agents clustered together :pensive:")

    text = """

    In this project, we utilize the **ModelV8 Small** architecture to train a custom model for detecting agents in the popular game *Valorant*. The model has been specifically trained on custom data, focusing on two agents **Cypher** and **Brimstone** with plans to expand to other agents in the future. By using ModelV8 Small, a lightweight version of the YOLO (You Only Look Once) model, we can efficiently detect agents in real-time gameplay while maintaining a balance between performance and accuracy. The training involves annotating in-game images and finetuning the model to recognize each agent's unique characteristics and poses, making it highly effective for Valorant agent detection tasks.
    
    """

    st.markdown(text)
    
    st.write("---")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/smmustafa/)")
