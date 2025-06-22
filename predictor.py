
import numpy as np

def predict_disease(model, input_data, disease):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return "Positive" if prediction[0] == 1 else "Negative"
