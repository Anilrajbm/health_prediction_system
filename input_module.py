import streamlit as st

def get_user_input(disease):
    if disease == "Diabetes":
        pregnancies = st.number_input("Pregnancies", 0, 20)
        glucose = st.number_input("Glucose", 0, 200)
        bp = st.number_input("Blood Pressure", 0, 150)
        skin_thickness = st.number_input("Skin Thickness", 0, 100)
        insulin = st.number_input("Insulin", 0, 1000)
        bmi = st.number_input("BMI", 0.0, 70.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5)
        age = st.number_input("Age", 1, 120)
        return [pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]

    elif disease == "Heart Disease":
        age = st.number_input("Age", 1, 120)
        sex = st.number_input("Sex (0 = female, 1 = male)", 0, 1)
        cp = st.number_input("Chest Pain Type (0-3)", 0, 3)
        trestbps = st.number_input("Resting Blood Pressure", 80, 200)
        chol = st.number_input("Cholesterol", 100, 600)
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)", 0, 1)
        restecg = st.number_input("Resting ECG (0-2)", 0, 2)
        thalach = st.number_input("Max Heart Rate Achieved", 50, 250)
        exang = st.number_input("Exercise Induced Angina (1 = yes, 0 = no)", 0, 1)
        oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
        slope = st.number_input("Slope (0-2)", 0, 2)
        ca = st.number_input("Number of Major Vessels (0-3)", 0, 3)
        thal = st.number_input("Thalassemia (1-3)", 1, 3)
        return [age, sex, cp, trestbps, chol, fbs, restecg,
                thalach, exang, oldpeak, slope, ca, thal]

    elif disease == "Parkinson's":
        fo = st.number_input("MDVP:Fo(Hz)", 0.0, 300.0)
        fhi = st.number_input("MDVP:Fhi(Hz)", 0.0, 300.0)
        flo = st.number_input("MDVP:Flo(Hz)", 0.0, 300.0)
        jitter_percent = st.number_input("MDVP:Jitter(%)", 0.0, 1.0)
        jitter_abs = st.number_input("MDVP:Jitter(Abs)", 0.0, 1.0)
        rap = st.number_input("MDVP:RAP", 0.0, 1.0)
        ppq = st.number_input("MDVP:PPQ", 0.0, 1.0)
        ddp = st.number_input("Jitter:DDP", 0.0, 1.0)
        shimmer = st.number_input("MDVP:Shimmer", 0.0, 1.0)
        shimmer_db = st.number_input("MDVP:Shimmer(dB)", 0.0, 3.0)
        apq3 = st.number_input("Shimmer:APQ3", 0.0, 1.0)
        apq5 = st.number_input("Shimmer:APQ5", 0.0, 1.0)
        mdvp_apq = st.number_input("MDVP:APQ", 0.0, 1.0)
        dda = st.number_input("Shimmer:DDA", 0.0, 1.0)
        nhr = st.number_input("NHR", 0.0, 1.0)
        hnr = st.number_input("HNR", 0.0, 50.0)
        rpde = st.number_input("RPDE", 0.0, 1.0)
        dfa = st.number_input("DFA", 0.0, 1.0)
        spread1 = st.number_input("Spread1", -10.0, 10.0)
        spread2 = st.number_input("Spread2", -10.0, 10.0)
        d2 = st.number_input("D2", 0.0, 4.0)
        ppe = st.number_input("PPE", 0.0, 1.0)

        return [
            fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
            shimmer, shimmer_db, apq3, apq5, mdvp_apq, dda,
            nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe
        ]
    else:
        st.warning("Disease not implemented yet.")
        return None
