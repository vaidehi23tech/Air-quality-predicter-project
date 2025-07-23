import pandas as pd
import numpy as np

# Generate a sample dataset with synthetic air quality and weather data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=200)

data = pd.DataFrame({
    'Date': dates,
    'PM2.5': np.random.uniform(10, 200, size=200),
    'PM10': np.random.uniform(20, 300, size=200),
    'NO2': np.random.uniform(5, 100, size=200),
    'SO2': np.random.uniform(2, 80, size=200),
    'O3': np.random.uniform(10, 150, size=200),
    'CO': np.random.uniform(0.5, 5.0, size=200),
    'Temperature': np.random.uniform(10, 40, size=200),
    'Humidity': np.random.uniform(30, 90, size=200),
    'WindSpeed': np.random.uniform(0.5, 15, size=200),
})

# Simulate AQI based on weighted sum of pollutants
data['AQI'] = (
    0.3 * data['PM2.5'] +
    0.2 * data['PM10'] +
    0.1 * data['NO2'] +
    0.1 * data['SO2'] +
    0.1 * data['O3'] +
    0.1 * data['CO'] * 20 +
    0.05 * (40 - data['Temperature']) +
    0.05 * (100 - data['Humidity'])
).round(2)

# Save to CSV
file_path = r"C:\Users\HP\OneDrive\Desktop\Air Quality\data\historical_aqi.csv"
data.to_csv(file_path, index=False)
file_path