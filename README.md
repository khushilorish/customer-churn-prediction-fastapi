# 📊 Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn using a Random Forest Classifier. The project includes data preprocessing, feature engineering, model training, FastAPI backend, Streamlit frontend, and deployment on Hugging Face Spaces.

---

## 🚀 Live Demo

### 🌐 Streamlit Frontend
https://khushilorish-customer-churn-prediction-streamlit.hf.space

### ⚡ FastAPI Backend
https://khushilorish-customer-churn-prediction-fastapi.hf.space/docs

---

## 📌 Problem Statement

Customer churn is one of the biggest challenges for telecom companies. Losing customers directly affects revenue.

This project predicts whether a customer is likely to leave the company based on demographic information, contract details, internet services, billing information, and account history.

---

## 📂 Dataset

Dataset: Telecom Customer Churn Dataset

Target Variable:
- Churn
    - Yes
    - No

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib
- Uvicorn
- Hugging Face Spaces

---

## 📊 Machine Learning Workflow

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Categorical Encoding
- Model Training
- Hyperparameter Tuning
- Threshold Optimization
- Model Evaluation
- API Development
- Streamlit UI
- Cloud Deployment

---

## 🤖 Model Used

Random Forest Classifier

Threshold used:
```
0.60
```

---

## 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 80.9% |
| Precision | 62.0% |
| Recall | 72.6% |

---

## 📥 Input Features

The model predicts churn using features such as:

- Senior Citizen
- Dependents
- Tenure
- Internet Service
- Multiple Lines
- Online Security
- Tech Support
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

## 📤 Prediction Output

The application returns:

- Customer Churn Prediction
- Churn Probability
- Risk Level

Example:

```
Prediction:
Customer is NOT likely to churn

Probability:
55.99%

Risk Level:
Medium
```

---

## 📸 Screenshots

### Dashboard

![Dashboard](Screenshots/Dashboard%20img.png)

### Prediction Result

![Prediction](Screenshots/Prediction%20img.png)

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── app.py
├── streamlit_app.py
├── schema.py
├── feature_engineering.py
├── churn_pipeline.pkl
├── threshold.pkl
├── requirements.txt
├── Dockerfile
├── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/khushilorish/customer-churn-prediction-fastapi.git
```

Move into project

```bash
cd customer-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Run Streamlit in new terminal

```bash
streamlit run streamlit_app.py
```

---

## 📌 API Documentation

After running FastAPI:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Future Improvements

- XGBoost Implementation
- LightGBM Model
- SHAP Explainability
- Customer Segmentation
- Feature Importance Visualization
- Model Monitoring
- Docker Compose Deployment

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
