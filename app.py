import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(
    open("models/crop_model.pkl", "rb")
)

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾"
)

st.title("🌾 Crop Recommendation System")

st.write(
    "Enter soil and environmental parameters to get the best crop recommendation."
)

N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)

temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
ph = st.number_input("pH Value", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("Recommend Crop"):

    input_data = pd.DataFrame(
        [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(input_data)

    st.success(
        f"🌱 Recommended Crop: {prediction[0].upper()}"
    )