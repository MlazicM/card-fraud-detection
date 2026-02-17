# Credit Card Fraud Detection 💳🛡️

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Focus-Anomaly%20Detection-red)

An end-to-end machine learning pipeline to detect fraudulent credit card transactions using highly imbalanced data.

## 🚧 Project Status: Work in Progress
I am currently developing this model. The goal is to build a robust classifier that can handle the extreme class imbalance (approx. 0.17% fraud) typical in financial datasets.

### 📅 Development Roadmap
- [x] Initial Repository Setup
- [x] Exploratory Data Analysis (EDA) & Visualization
- [ ] Feature Scaling (Time & Amount)
- [ ] Handling Imbalance (SMOTE / Random Under-sampling)
- [ ] Model Selection (Logistic Regression, Random Forest, etc.)
- [ ] Hyperparameter Tuning
- [ ] Final Performance Report (AUPRC & Confusion Matrix)

---

## 📌 Project Overview
The challenge in fraud detection is the "needle in a haystack" problem. This project explores various techniques to ensure the model doesn't just guess "not fraud" every time to achieve high accuracy. 



## 📊 Dataset
The dataset contains transactions made by European cardholders. Due to confidentiality, features V1 to V28 are PCA-transformed versions of the original data.
- Target Variable: Class (1 for Fraud, 0 for Legitimate)
- Key Challenge: Extreme class imbalance requiring specialized evaluation metrics like Precision-Recall curves instead of simple Accuracy.

## 🛠️ Current Tech Stack
- Language: Python
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

## 🚀 How to Run (Local)
1. Clone the repo:
   git clone https://github.com/MlazicM/card-fraud-detection.git

2. Install requirements:
   pip install pandas numpy matplotlib seaborn scikit-learn

3. Run the notebook:
   jupyter notebook

---
*Last Updated: February 2026*
