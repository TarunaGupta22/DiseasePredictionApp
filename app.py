import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Title of the web app
st.title("Disease Prediction System")
st.write("Enter your health data to predict disease risk:")

# User input sliders
age = st.slider("Age", 1, 100, 30)
bmi = st.slider("BMI", 10.0, 50.0, 22.0)
bp = st.slider("Blood Pressure", 50, 180, 80)
glucose = st.slider("Glucose Level", 50, 200, 100)

# Load dataset
data = pd.read_csv("diabetes.csv")

# Use only the same features as in input
X = data[['Age', 'BMI', 'BloodPressure', 'Glucose']]
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction
input_data = np.array([[age, bmi, bp, glucose]])
prediction = model.predict(input_data)

# Show prediction result
if st.button("Predict"):
    st.write("Prediction:", "⚠️ Disease Risk" if prediction[0] == 1 else "✅ No Disease Risk")
