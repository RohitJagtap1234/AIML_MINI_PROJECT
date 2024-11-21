import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your trained model (ensure this path is correct)
# Replace 'model.pkl' with the actual file you saved the model in
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app
st.title("Stock Price Movement Predictor")
st.write("Enter the stock details to predict whether the closing price will go up or down.")

# Inputs
open_price = st.number_input("Open Price", min_value=0.0, step=0.01)
high_price = st.number_input("High Price", min_value=0.0, step=0.01)
low_price = st.number_input("Low Price", min_value=0.0, step=0.01)
volume = st.number_input("Volume", min_value=0.0, step=1.0)

# Prediction logic
if st.button("Predict"):
    try:
        # Prepare the input data for prediction
        input_data = np.array([[open_price, high_price, low_price, volume]])
        prediction = model.predict(input_data)

        # Display the result
        st.subheader("Prediction")
        if prediction[0] == 1:
            st.write("📈 The closing price will go **UP**.")
        else:
            st.write("📉 The closing price will go **DOWN**.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
