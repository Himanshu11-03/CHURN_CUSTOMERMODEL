import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure (Months)", 0, 100)
monthlycharges = st.number_input("Monthly Charges", 0.0, 500.0)
totalcharges = st.number_input("Total Charges", 0.0, 10000.0)

if st.button("Predict Churn"):

    data = pd.DataFrame({
        "tenure":[tenure],
        "MonthlyCharges":[monthlycharges],
        "TotalCharges":[totalcharges]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")
