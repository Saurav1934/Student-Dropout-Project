# 🎓 AI-Powered Student Dropout Prediction & Retention Analytics System

## 📌 Project Overview

The **AI-Powered Student Dropout Prediction & Retention Analytics System** is a machine learning and analytics solution designed to identify university students who are at risk of dropping out.

The system analyzes:

* Academic performance
* Attendance behavior
* Financial and family background
* Student demographics
* Semester-wise progress

to predict **dropout probability**, classify students into **risk levels**, and generate **actionable recommendations** for early intervention.

The project combines **Machine Learning**, **Explainable AI (XAI)**, **Risk Categorization**, and an **Interactive Streamlit Dashboard** to help educational institutions improve student retention.

---

## 🚨 Problem Statement

Student dropout is a major challenge faced by universities and colleges. Traditional monitoring systems often fail to identify struggling students early enough.

This project aims to solve this problem using:

* Artificial Intelligence
* Predictive Analytics
* Explainable Machine Learning
* Educational Data Mining

to proactively identify students at risk and support academic intervention.

---

## 🎯 Objectives

The key objectives of this project are:

✅ Predict student dropout risk using machine learning
✅ Analyze academic and behavioral factors affecting retention
✅ Compare multiple ML models for performance evaluation
✅ Categorize students into **Low**, **Medium**, and **High Risk** groups
✅ Provide personalized intervention recommendations
✅ Build an interactive dashboard for monitoring and prediction

---

## ✨ Key Features

### 1. Student Dropout Prediction

Predicts whether a student is likely to:

* Continue / Graduate
* Drop Out

using machine learning algorithms.

---

### 2. Multi-Model Comparison

The project evaluates and compares multiple machine learning models:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* K-Nearest Neighbors (KNN)
* XGBoost

to identify the best-performing model.

---

### 3. Explainable AI (XAI)

The system explains **why a student is predicted to be at risk**.

Example:

**High Dropout Risk due to:**

* Low GPA
* Poor Attendance
* Academic Backlogs
* Financial Issues

---

### 4. Risk Categorization

Students are categorized into:

🟢 **Low Risk**
🟡 **Medium Risk**
🔴 **High Risk**

This enables universities to prioritize interventions.

---

### 5. Recommendation System

The dashboard generates personalized recommendations such as:

* 📘 Academic Counseling
* 👨‍🏫 Mentorship Support
* 📈 Attendance Monitoring
* 💰 Financial Aid Guidance
* 📝 Tutoring Assistance

---

### 6. Interactive Dashboard

Built using **Streamlit**, the dashboard provides:

* Student selection system
* Dropout probability prediction
* Risk level analysis
* AI insights
* GPA trend visualization
* Recommendation engine
* Student performance overview

---

## 🛠 Technologies Used

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| Python       | Programming Language     |
| Pandas       | Data Processing          |
| NumPy        | Numerical Analysis       |
| Scikit-learn | Machine Learning         |
| XGBoost      | Advanced ML Model        |
| SHAP         | Explainable AI           |
| Streamlit    | Dashboard Development    |
| Matplotlib   | Data Visualization       |
| Sweetviz     | Automated Data Profiling |
| Joblib       | Model Serialization      |

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Encoding
6. Model Training
7. Multi-Model Comparison
8. Risk Categorization
9. Explainable AI Analysis
10. Dashboard Deployment

---

## 📈 Model Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Cross Validation

The final model was selected based on balanced performance for identifying at-risk students.

---

## 🖥 Dashboard Preview

The Streamlit dashboard includes:

### Student Overview

* GPA
* Attendance %
* Backlogs
* Fee Status

### Prediction Result

* Dropout Probability
* Risk Level
* AI-Based Insights

### Recommendations

* Personalized intervention strategies

### Academic Trend

* Semester-wise GPA visualization

---

## 📂 Project Structure

```text id="rr2s95"
student_dropout_prediction/

│── data/
│   ├── student_dropout.csv
│   └── cleaned_student_dropout.csv

│── models/
│   └── student_dropout_pipeline.pkl

│── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_training.ipynb

│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash id="2r6pbv"
git clone <repository-url>
```

### 2. Navigate to Project Folder

```bash id="j9v0d1"
cd student_dropout_prediction
```

### 3. Create Conda Environment

```bash id="9s1hzt"
conda create -n student_dropout python=3.11
conda activate student_dropout
```

### 4. Install Dependencies

```bash id="1k2r7f"
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Launch the Streamlit dashboard:

```bash id="1g7ptf"
streamlit run app.py
```

Open browser:

```text id="7d1xnm"
http://localhost:8501
```

---

## 🔮 Future Scope

Possible future enhancements:

* Real-time student monitoring
* Deep learning integration
* University ERP integration
* Automated intervention alerts
* Multi-university deployment
* Cloud deployment

---

## 👨‍💻 Author

**Saurav**

AI-Powered Student Dropout Prediction & Retention Analytics System
