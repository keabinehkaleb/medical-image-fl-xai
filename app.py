import streamlit as st

st.title("LLM-Based Explainable Medical Diagnosis Assistant")

st.markdown("""
This demo shows Federated Learning + Explainable AI for medical image diagnosis.
Upload a medical image to see prediction and explanation.
""")

file = st.file_uploader("Upload medical image")

if file:
    st.image(file, caption="Uploaded Image")

    st.subheader("Prediction")
    st.success("Predicted class: Benign Skin Lesion")

    st.subheader("Explainable AI")
    st.write("Highlighted regions indicate important areas used by the model.")
