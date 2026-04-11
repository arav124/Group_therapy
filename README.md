# Group_therapy
# 🧠 AI-Based Group Therapy Recommendation System

An end-to-end machine learning application that analyzes psychological assessment data and recommends personalized group therapy, therapist guidance, and risk classification.

---

## 🚀 Project Overview

This project is designed to:

* Analyze users' mental health using structured questionnaires
* Identify psychological patterns using Machine Learning
* Classify users into risk categories
* Recommend appropriate therapy plans
* Assign users to suitable therapy groups

---

## 🎯 Key Features

* 📊 Psychological assessment (Emotional Neglect, Anxiety, PsyCap)
* 🤖 ML-based clustering (KMeans)
* 🧠 Risk classification (High / Moderate / Low)
* 💊 Therapy recommendation system
* 👨‍⚕️ Therapist suggestion
* 🧑‍🤝‍🧑 Group therapy allocation
* 🌐 Full-stack implementation (Frontend + Backend)

---

## 🖥️ Frontend

The frontend is built using:

* HTML
* CSS
* JavaScript

### ✨ Features:

* Multi-step assessment UI
* Progress tracking
* Dynamic question rendering
* Real-time validation
* Loading screen
* Result visualization (risk, therapy, therapist, group)

---

## ⚙️ Backend

Built using:

* Flask (Python)
* Scikit-learn
* Pandas, NumPy

### API Endpoint:

POST /predict

### Input:

{
"en": [...],
"ia_an": [...],
"ia_av": [...],
"psy": [...]
}

### Output:

{
"risk": "Moderate",
"therapy": "Weekly Support Group",
"therapist": "Dr. B",
"cluster": 0
}

---

## 🧠 Machine Learning

### Model Used:

* KMeans Clustering

### Features:

* Emotional Neglect Score
* Interpersonal Anxiety Score
* Psychological Capital Score

### Pipeline:

Raw Input → Feature Engineering → Scaling → Clustering → Interpretation → Recommendation

---

## 📁 Project Structure

Group_therapy/

│
├── backend/
│   ├── app.py
│   ├── models/
│   │   ├── kmeans_model.pkl
│   │   └── scaler.pkl
│   ├── utils/
│   └── requirements.txt

│
├── frontend/
│   ├── index.html
│   ├── questionnaire.html
│   ├── result.html
│   ├── script.js
│   └── style.css

│
├── data/
│   ├── dataset.xlsx
│   └── processed_data.csv

│
├── notebook/
│   └── model_training.ipynb

│
├── README.md
└── .gitignore

---

## ▶️ How to Run

### 1️⃣ Clone the repo

git clone <your-repo-url>
cd Group_therapy

---

### 2️⃣ Install dependencies

cd backend
pip install -r requirements.txt

---

### 3️⃣ Run backend

python app.py

Server runs at:
http://127.0.0.1:5000

---

### 4️⃣ Run frontend

cd ../frontend
python -m http.server 5500

Open in browser:
http://localhost:5500/index.html

---

## 🔄 Application Flow

User Input (UI)
↓
Frontend (JS)
↓
Flask API (/predict)
↓
ML Model (KMeans)
↓
Prediction + Recommendation
↓
Frontend Result Display

---

## 💡 Future Enhancements

* Real therapist database integration
* Location-based recommendations
* User authentication
* Deployment (Cloud)
* Advanced ML models

---

## 🏆 Highlights

* End-to-end ML system
* Real-world mental health application
* Full-stack integration
* Clean UI + UX
* Scalable architecture

---

## 📌 Authors

* **Aravind Murugesan** – Machine Learning, Backend Development, System Design
* **Sakthi** – Frontend Development (UI/UX Design)

---

## 🤝 Contributions

* Aravind handled the complete ML pipeline, model building, backend API, and system architecture.
* Sakthi designed and developed the frontend interface, including user experience, questionnaire flow, and result visualization.

---

## ⭐ If you like this project, give it a star!

