
import streamlit as st
from input_module import get_user_input
from model_loader import load_model
from predictor import predict_disease
from chatbot_module import get_health_tips

st.set_page_config(page_title="Health Prediction System", layout="centered")
st.title("🩺 Health Prediction System")

disease = st.selectbox("Choose Disease to Predict", ["Diabetes", "Heart Disease", "Parkinson's"])

if disease:
    input_data = get_user_input(disease)

    if st.button("Predict"):
        model = load_model(disease)
        result = predict_disease(model, input_data, disease)
        st.success(f"Prediction Result: {result}")
        st.info(get_health_tips(disease, result))
