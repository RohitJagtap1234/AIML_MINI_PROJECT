import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Replace with the path to your trained model or integrate your model's training code here
from sklearn.ensemble import RandomForestClassifier

# Sample model (replace with your actual trained model)
# rf = RandomForestClassifier().fit(X_train, y_train)
# Save and load your model using pickle (example)
# pickle.dump(rf, open("model.pkl", "wb"))
# rf = pickle.load(open("model.pkl", "rb"))

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
    input_data = np.array([[open_price, high_price, low_price, volume]])
    # Replace `rf` with your actual loaded model
    # prediction = rf.predict(input_data)
    prediction = [1]  # Example output (1 = Up, 0 = Down)

    st.subheader("Prediction")
    st.write("📈 The closing price will go **UP**" if prediction[0] == 1 else "📉 The closing price will go **DOWN**")

