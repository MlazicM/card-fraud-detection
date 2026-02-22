# Credit Card Fraud Detection 💳🛡️

![Status](https://img.shields.io/badge/Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Deploy](https://img.shields.io/badge/API-Live-brightgreen)

An end-to-end machine learning pipeline to detect fraudulent credit card transactions, deployed as a REST API.

## 🌐 Live API
**Base URL:** `https://card-fraud-detection-zhgs.onrender.com`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/predict` | POST | Predict fraud |
| `/docs` | GET | Interactive API docs |

**Example request:**
```json
POST /predict
{
  "features": [-1.35, -0.07, 2.54, ...]
}
```

**Example response:**
```json
{
  "fraud": false,
  "probability": 0.0001
}
```

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Precision | 0.9367 |
| Recall | 0.7789 |
| F1 Score | 0.8506 |
| F2 Score | 0.8061 |
| AUPRC | 0.8290 |

## 📌 Project Pipeline

- [x] Exploratory Data Analysis
- [x] Feature Engineering (time_delta, velocity, hour_of_day)
- [x] Preprocessing & SMOTE for class imbalance
- [x] Model Training (Logistic Regression, Random Forest, XGBoost)
- [x] Hyperparameter Tuning (RandomizedSearchCV)
- [x] Evaluation (Confusion Matrix, PR Curve, Feature Importance)
- [x] REST API (FastAPI)
- [x] Deployment (Render)

## 🛠️ Tech Stack
Python, XGBoost, Scikit-Learn, FastAPI, Uvicorn, Pandas, NumPy, Imbalanced-Learn

## 🚀 Run Locally
```bash
git clone https://github.com/MlazicM/card-fraud-detection.git
pip install -r requirements.txt
uvicorn app:app --reload
```

## 📁 Dataset
European cardholders dataset. Features V1-V28 are PCA-transformed. Target: `Class` (1 = Fraud, 0 = Legit).

---
*Last Updated: February 2026*
