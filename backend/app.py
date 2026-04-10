from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# load model
kmeans = pickle.load(open("models/kmeans_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def home():
    return "Backend is running!"
    
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    en = data["en"]
    ia_an = data["ia_an"]
    ia_av = data["ia_av"]
    psy = data["psy"]

    # scores
    EN_score = np.mean(en)
    Anxiety_score = np.mean(np.array(ia_an) + np.array(ia_av))
    PsyCap_score = np.mean(psy)

    # dataframe (fix warning)
    X = pd.DataFrame([{
        "EN_score": EN_score,
        "Anxiety_score": Anxiety_score,
        "PsyCap_score": PsyCap_score
    }])

    X_scaled = scaler.transform(X)

    cluster = int(kmeans.predict(X_scaled)[0])

    # mapping
    if cluster == 2:
        risk = "High Risk"
        therapy = "Intensive Therapy"
        therapist = "Dr. A"
    elif cluster == 0:
        risk = "Moderate"
        therapy = "Weekly Support"
        therapist = "Dr. B"
    else:
        risk = "Low Risk"
        therapy = "Awareness Session"
        therapist = "Dr. C"

    return jsonify({
        "risk": risk,
        "therapy": therapy,
        "therapist": therapist,
        "cluster": cluster
    })


if __name__ == "__main__":
    app.run(debug=True)