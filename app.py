# app.py
import streamlit as st
import numpy as np
import pandas as pd
from MlflowProject.pipeline.prediction import PredictionPipeline

st.set_page_config(page_title="Salary Prediction App")

st.title("Salary Prediction App")
st.write("Enter the years of experience to predict the salary.")

# User input
experience = st.number_input("Years of Experience", min_value=0.0, max_value=30.0, value=1.0, step=0.1)

# When button is clicked
if st.button("Predict Salary"):
    # Ensure the feature name matches what was used during training
    input_data = pd.DataFrame({"YearsExperience": [experience]})
    
    pipeline = PredictionPipeline()
    result = pipeline.predict(input_data)

    st.success(f"Predicted Salary: ₹{result[0]:,.2f}")

