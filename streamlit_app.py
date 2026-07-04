import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Dashboard")
st.write("Predict whether a telecom customer is likely to churn.")

# ---------------- Sidebar ---------------- #

st.sidebar.title("Project Information")

st.sidebar.success("Model : Random Forest")
st.sidebar.info("Threshold : 0.60")
st.sidebar.write("Accuracy : 76.7%")
st.sidebar.write("Recall : 72.6%")
st.sidebar.write("Precision : 62.0%")

# ---------------- Form ---------------- #

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👤 Customer Information")

        SeniorCitizen = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        Dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0
        )

        Contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        PaymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    with col2:

        st.subheader("🌐 Internet & Billing")

        InternetService = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        MultipleLines = st.selectbox(
            "MultipleLines", 
            ["No", 
            "Yes",
            "No phone service"
            ]
        )

        OnlineSecurity = st.selectbox(
            "Online Security",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        TechSupport = st.selectbox(
            "Tech Support",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        StreamingMovies = st.selectbox(
            "Streaming Movies",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        PaperlessBilling = st.selectbox(
            "Paperless Billing",
            [
                "Yes",
                "No"
            ]
        )

        MonthlyCharges = st.number_input(
            "Monthly Charges",
            min_value=0.0
        )

        TotalCharges = st.number_input(
            "Total Charges",
            min_value=0.0
        )

    submitted = st.form_submit_button("🔍 Predict")

# ---------------- Prediction ---------------- #

if submitted:

    customer = {
        "SeniorCitizen": SeniorCitizen,
        "Dependents": Dependents,
        "tenure": tenure,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "TechSupport": TechSupport,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    response = requests.post(
        "https://khushilorish-customer-churn-prediction-fastapi.hf.space/predict",
        json=customer
    )

    result = response.json()

    probability = result["probability"]

    st.divider()
    st.header("📈 Prediction Result")

    if result["prediction"] == 1:
        st.error("❌ Customer is likely to churn")
    else:
        st.success("✅ Customer is NOT likely to churn")

    st.metric(
        label="Churn Probability",
        value=f"{probability*100:.2f}%"
    )

    st.progress(probability)

    if probability < 0.40:
        st.success("🟢 Risk Level : Low")
    elif probability < 0.60:
        st.warning("🟡 Risk Level : Medium")
    else:
        st.error("🔴 Risk Level : High")