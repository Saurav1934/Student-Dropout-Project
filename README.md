# 🎓 AI-Powered Student Dropout Prediction & Retention Analytics System

## 🌐 Live Demo

**Try the deployed application here:**

**Live App:**
https://student-dropout-project-035.streamlit.app/

**GitHub Repository:**
https://github.com/Saurav1934/Student-Dropout-Project 

---

## 📌 Project Overview

The **AI-Powered Student Dropout Prediction & Retention Analytics System** is a machine learning and analytics solution developed to identify university students who are at risk of dropping out.

The system analyzes:

* Academic performance
* Attendance behavior
* Family background
* Financial indicators
* Semester-wise progress

to predict **dropout probability**, classify students into **risk levels**, and recommend suitable interventions.

The project combines:

* **Machine Learning**
* **Predictive Analytics**
* **Explainable Insights**
* **Risk Categorization**
* **Interactive Dashboarding**

to help educational institutions improve student retention and academic success.

---

## 🚨 Problem Statement

Student dropout is a major challenge faced by educational institutions. Traditional monitoring systems often fail to identify struggling students early enough.

This project uses **Artificial Intelligence and Data Analytics** to detect early warning signs and support proactive intervention.

---

## 🎯 Objectives

The main objectives are:

✅ Predict students likely to drop out
✅ Analyze academic and behavioral patterns
✅ Compare multiple ML models
✅ Categorize students into risk groups
✅ Generate personalized recommendations
✅ Build an interactive analytics dashboard

---

## ✨ Key Features

### 🎯 Student Dropout Prediction

Predicts whether a student is likely to:

* Continue / Graduate
* Drop Out

using machine learning algorithms.

---

### 📊 Multi-Model Comparison

The project compares:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* KNN
* XGBoost

to identify the best-performing model.

---

### 🧠 Explainable Insights

The system explains **why a student is at risk**.

Example risk indicators:

* Low GPA
* Poor attendance
* Academic backlogs
* Financial difficulties

---

### 🚦 Risk Categorization

Students are classified into:

🟢 **Low Risk**
🟡 **Medium Risk**
🔴 **High Risk**

to prioritize institutional intervention.

---

### 💡 Recommendation System

The dashboard generates personalized interventions such as:

* 📘 Academic Counseling
* 👨‍🏫 Mentorship Support
* 📝 Tutoring Assistance
* 📈 Attendance Monitoring

---

### 📈 Academic Performance Tracking

The system includes:

* Semester-wise GPA trend analysis
* Performance visualization
* Student academic insights

---

### 🖥 Interactive Streamlit Dashboard

The dashboard includes:

* Student selection system
* Risk prediction
* Dropout probability
* AI insights
* Student metrics
* GPA trend chart
* Recommendations engine

---

## 🛠 Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Core Programming      |
| Pandas       | Data Processing       |
| NumPy        | Numerical Analysis    |
| Scikit-learn | Machine Learning      |
| XGBoost      | Advanced Prediction   |
| SHAP         | Explainable AI        |
| Streamlit    | Dashboard Development |
| Matplotlib   | Visualization         |
| Sweetviz     | Data Profiling        |
| Joblib       | Model Serialization   |

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Multi-Model Comparison
7. Model Evaluation
8. Risk Categorization
9. Dashboard Deployment

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

## 📂 Project Structure

```text
Student-Dropout-Project/

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
│── runtime.txt
│── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Saurav1934/Student-Dropout-Project.git
```

### Navigate to Project Folder

```bash
cd Student-Dropout-Project
```

### Create Environment

```bash
conda create -n student_dropout python=3.11
conda activate student_dropout
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

Start Streamlit:

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## 🔮 Future Improvements

* Real-time student monitoring
* Deep learning integration
* University ERP integration
* Automated alerts for at-risk students
* Cloud deployment enhancements

---

## 👨‍💻 Author

**Saurav Ray**
B.Tech Computer Science Engineering
Lovely Professional University

**LinkedIn:**
https://linkedin.com/in/sauravray05
