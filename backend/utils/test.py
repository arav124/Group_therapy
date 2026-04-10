import pickle
import numpy as np


# 🔹 Load saved model and scaler
with open("kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


# 🔹 Prediction function (same as your backend)
def predict_user(en_answers, ia_an_answers, ia_av_answers, psy_answers):

    # Step 1: Calculate scores
    EN_score = np.mean(en_answers)
    Anxiety_score = np.mean(np.array(ia_an_answers) + np.array(ia_av_answers))
    PsyCap_score = np.mean(psy_answers)

    print("\n--- Calculated Scores ---")
    print("EN_score:", EN_score)
    print("Anxiety_score:", Anxiety_score)
    print("PsyCap_score:", PsyCap_score)

    # Step 2: Prepare input
    X = [[EN_score, Anxiety_score, PsyCap_score]]

    # Step 3: Scale
    X_scaled = scaler.transform(X)

    # Step 4: Predict cluster
    cluster = int(kmeans.predict(X_scaled)[0])

    # Step 5: Map risk
    if cluster == 2:
        risk = "High Risk"
        therapy = "Intensive Group Therapy"
        therapist = "Dr. A (Clinical Psychologist)"
    elif cluster == 0:
        risk = "Moderate / Vulnerable"
        therapy = "Weekly Support Group"
        therapist = "Dr. B (Counselor)"
    else:
        risk = "Low Risk"
        therapy = "Well-being Session"
        therapist = "Dr. C (Wellness Coach)"

    # Step 6: Group
    group = f"Group {cluster}"

    # Final result
    result = {
        "risk": risk,
        "therapy": therapy,
        "therapist": therapist,
        "group": group
    }

    return result


# 🔹 TEST INPUT (sample data)
if __name__ == "__main__":

    en = [3,4,5,3,4,3,2,3,4,3,4,5,3,2,3,4,3,2,3,4,3,4]
    ia_an = [1,2,1,0,2,1,2,1,0,1,2,1,0,2,1,2,1,0,1,2,1,0,1,2]
    ia_av = [1,1,2,0,1,2,1,0,1,2,1,0,1,2,1,0,1,2,1,0,1,2,1,0]
    psy = [4,3,5,4,3,4,5,3,4,3,4,5]

    result = predict_user(en, ia_an, ia_av, psy)

    print("\n--- Prediction Result ---")
    print(result)