import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data
data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Air Quality\data\historical_aqi.csv")
data.dropna(inplace=True)

# Features and target
X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'O3', 'CO', 'Temperature', 'Humidity', 'WindSpeed']]
y = data['AQI']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model,r'C:\Users\HP\OneDrive\Desktop\Air Quality\models\aqi_model.pkl')

# Evaluate
y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²:", r2_score(y_test, y_pred))