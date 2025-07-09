import pickle

def load_model(disease):
    if disease == "Diabetes":
        with open("diabetes_model.sav", "rb") as f:
            return pickle.load(f)
    elif disease == "Heart Disease":
        with open("heart_model.sav", "rb") as f:
            return pickle.load(f)
    elif disease == "Parkinson's":
        with open("parkinsons_model.sav", "rb") as f:
            return pickle.load(f)
