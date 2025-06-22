
def get_health_tips(disease, result):
    if result == "Positive":
        if disease == "Diabetes":
            return "Maintain a low-sugar diet, exercise daily, monitor blood sugar regularly."
        elif disease == "Heart Disease":
            return "Eat heart-healthy foods, reduce salt, manage stress, and avoid smoking."
        elif disease == "Parkinson's":
            return "Physical therapy, medication adherence, and neurologist consultations are advised."
    else:
        return "No issues detected. Maintain a healthy lifestyle!"
