# File: app/air_quality_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load(r"C:\Users\HP\OneDrive\Desktop\Air Quality\models\aqi_model.pkl")
data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Air Quality\data\historical_aqi.csv")
data['Date'] = pd.to_datetime(data['Date'])

st.set_page_config(page_title="Air Quality Prediction & Monitoring", layout="wide")
st.title("🌫️ Air Quality Prediction & Monitoring Dashboard")

# Tabs
tab1, tab2 = st.tabs(["📊 Monitoring", "🔮 AQI Prediction"])

# --- Monitoring Tab ---
with tab1:
    st.subheader("📡 Live Monitoring Dashboard")

    # Simulated values
    aqi = int(data['AQI'].iloc[-1])
    pm25 = int(data['PM2.5'].iloc[-1])
    pm10 = int(data['PM10'].iloc[-1])
    no2 = int(data['NO2'].iloc[-1])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("AQI", aqi)
    col2.metric("PM2.5", f"{pm25} µg/m³")
    col3.metric("PM10", f"{pm10} µg/m³")
    col4.metric("NO2", f"{no2} ppb")

    st.markdown("### AQI Over Time")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(data['Date'], data['AQI'], color='green')
    ax.set_xlabel("Date")
    ax.set_ylabel("AQI")
    st.pyplot(fig)

# --- Prediction Tab ---
with tab2:
    st.subheader("🔮 Predict AQI")

    pm25 = st.slider("PM2.5", 0.0, 500.0)
    pm10 = st.slider("PM10", 0.0, 500.0)
    no2 = st.slider("NO2", 0.0, 200.0)
    so2 = st.slider("SO2", 0.0, 150.0)
    o3 = st.slider("O3", 0.0, 200.0)
    co = st.slider("CO", 0.0, 10.0)
    temp = st.slider("Temperature (°C)", -10.0, 50.0)
    humidity = st.slider("Humidity (%)", 0.0, 100.0)
    wind = st.slider("Wind Speed (km/h)", 0.0, 50.0)

    input_data = np.array([[pm25, pm10, no2, so2, o3, co, temp, humidity, wind]])

    if st.button("Predict AQI"):
        predicted_aqi = model.predict(input_data)[0]
        st.success(f"Predicted AQI: {round(predicted_aqi, 2)}")
