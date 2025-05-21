# 🩺 Disease Prediction System using Machine Learning

## 📌 Overview

The **Disease Prediction System** is a smart, web-based application designed to predict the risk of a chronic disease — specifically **diabetes** — using basic medical parameters provided by the user. This project demonstrates the application of **machine learning in healthcare**, offering early insights that can support preventive action.

Built using **Python**, **Streamlit**, and **scikit-learn**, this tool enables users to interact with a trained machine learning model through a clean and responsive web interface.

---

## 🚀 What the System Does

- Takes user input for:
  - ✅ Age
  - ✅ Body Mass Index (BMI)
  - ✅ Blood Pressure
  - ✅ Glucose Level

- Uses a **Random Forest Classifier** to analyze the input.
- Predicts whether the user is at **high risk** or **low risk** of having the disease.
- Displays the result in real-time via the Streamlit interface.

---

## 🎯 Objective

- To utilize machine learning for early disease risk prediction.
- To build a simple and accessible app for non-technical users.
- To promote awareness and assist users in seeking timely medical advice.

---

## 🌍 Why This Matters

Millions of people are affected by chronic illnesses like diabetes, many without knowing it. Early detection plays a crucial role in managing health effectively. This system provides a **first-level, AI-powered screening** tool that is:

- Free
- Accessible
- Easy to use

By giving users a quick and simple way to assess risk, the tool encourages proactive health management.

---

## 🧠 Machine Learning Model

- **Model Used**: Random Forest Classifier
- **Dataset**: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Features Used**: Age, BMI, Blood Pressure, Glucose
- **Target Column**: Outcome (0 = No Disease, 1 = Disease)

---

## 🛠 Built With

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

## 🧪 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/disease-prediction-system.git
cd disease-prediction-system
