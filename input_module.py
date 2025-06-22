
import streamlit as st

def get_user_input(disease):
    if disease == "Diabetes":
        pregnancies = st.number_input("Pregnancies", 0, 20)
        glucose = st.number_input("Glucose", 0, 300)
        bp = st.number_input("Blood Pressure", 0, 200)
        skin_thickness = st.number_input("Skin Thickness", 0, 100)
        insulin = st.number_input("Insulin", 0, 900)
        bmi = st.number_input("BMI", 0.0, 70.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
        age = st.number_input("Age", 1, 120)
        return [pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]

    elif disease == "Heart Disease":
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex", [0, 1])
        cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
        trestbps = st.number_input("Resting Blood Pressure", 0, 200)
        chol = st.number_input("Serum Cholestoral (mg/dl)", 0, 600)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.selectbox("Resting ECG results", [0, 1, 2])
        thalach = st.number_input("Max Heart Rate", 0, 250)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("ST depression", 0.0, 10.0)
        slope = st.selectbox("Slope", [0, 1, 2])
        ca = st.selectbox("Number of major vessels", [0, 1, 2, 3])
        thal = st.selectbox("Thal", [0, 1, 2, 3])
        return [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    elif disease == "Parkinson's":
        fo = st.number_input("MDVP:Fo(Hz)", 0.0, 300.0)
        fhi = st.number_input("MDVP:Fhi(Hz)", 0.0, 300.0)
        flo = st.number_input("MDVP:Flo(Hz)", 0.0, 300.0)
        jitter_percent = st.number_input("MDVP:Jitter(%)", 0.0, 1.0)
        shimmer = st.number_input("MDVP:Shimmer", 0.0, 1.0)
        rap = st.number_input("MDVP:RAP", 0.0, 1.0)
        ddp = st.number_input("MDVP:DDP", 0.0, 1.0)
        apq = st.number_input("Shimmer:APQ3", 0.0, 1.0)
        spread1 = st.number_input("Spread1", -10.0, 10.0)
        spread2 = st.number_input("Spread2", -10.0, 10.0)
        d2 = st.number_input("D2", 0.0, 4.0)
        return [fo, fhi, flo, jitter_percent, shimmer, rap, ddp, apq, spread1, spread2, d2]
