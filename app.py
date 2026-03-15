import streamlit as st

st.title("LLM-Based Explainable Medical Diagnosis Assistant")

st.write("Upload an image for AI explanation")

file = st.file_uploader("Upload image")

if file:
    st.image(file)
    st.write("Prediction: Example skin condition")
    st.write("Explanation: This is a demo AI explanation.")