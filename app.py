import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AI Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# -------------------------
# Load Model & Data
# -------------------------
model = joblib.load(
    "models/student_dropout_pipeline.pkl"
)

df = pd.read_csv(
    "data/cleaned_student_dropout.csv"
)

# -------------------------
# Title
# -------------------------
st.title("🎓 AI Student Dropout Prediction System")
st.markdown(
    "### Intelligent Student Retention Analytics Dashboard"
)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("Student Selection")

student_index = st.sidebar.selectbox(
    "Select Student",
    df.index
)

student_data = df.iloc[[student_index]]

# -------------------------
# Prediction
# -------------------------
X_input = student_data.drop(
    "Dropped_Out",
    axis=1
)

prediction = model.predict(X_input)[0]

probability = model.predict_proba(
    X_input
)[0][1]

# -------------------------
# Risk Level
# -------------------------
if probability < 0.20:
    risk = "🟢 Low Risk"
    risk_color = "green"

elif probability < 0.50:
    risk = "🟡 Medium Risk"
    risk_color = "orange"

else:
    risk = "🔴 High Risk"
    risk_color = "red"

# -------------------------
# Layout Columns
# -------------------------
col1, col2 = st.columns([1.2, 1])

# ==================================================
# LEFT SIDE → Student Info
# ==================================================
with col1:

    st.subheader("👨‍🎓 Student Overview")

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "GPA",
            round(
                student_data["GPA"].values[0],
                2
            )
        )

    with metric2:

        attendance_col = (
            "Attendance_Pct"
            if "Attendance_Pct"
            in student_data.columns
            else None
        )

        attendance_value = (
            student_data[
                attendance_col
            ].values[0]
            if attendance_col
            else 0
        )

        st.metric(
            "Attendance %",
            attendance_value
        )

    with metric3:

        backlog_col = (
            "Backlogs"
            if "Backlogs"
            in student_data.columns
            else None
        )

        backlog_value = (
            student_data[
                backlog_col
            ].values[0]
            if backlog_col
            else 0
        )

        st.metric(
            "Backlogs",
            backlog_value
        )

    with metric4:

        fee_col = (
            "Tuition_Fee_Status"
            if "Tuition_Fee_Status"
            in student_data.columns
            else None
        )

        fee_value = (
            student_data[
                fee_col
            ].values[0]
            if fee_col
            else "Unknown"
        )

        st.metric(
            "Fee Status",
            fee_value
        )

    st.markdown("---")

    st.subheader("📋 Student Details")

    st.dataframe(
        student_data.T,
        use_container_width=True
    )

# ==================================================
# RIGHT SIDE → Prediction
# ==================================================
with col2:

    st.subheader("🤖 Prediction Result")

    st.metric(
        "Dropout Probability",
        f"{probability:.2%}"
    )

    st.markdown(
        f"## {risk}"
    )

    st.progress(
        float(probability)
    )

    st.markdown("---")

    st.subheader("💡 AI Insights")

    insights = []

    if student_data["GPA"].values[0] < 5:
        insights.append(
            "⚠ Low GPA is strongly increasing dropout risk."
        )

    if (
        "Attendance_Pct"
        in student_data.columns
    ):

        if (
            student_data[
                "Attendance_Pct"
            ].values[0] < 75
        ):
            insights.append(
                "⚠ Attendance below 75%."
            )

    if (
        "Backlogs"
        in student_data.columns
    ):

        if (
            student_data[
                "Backlogs"
            ].values[0] >= 2
        ):
            insights.append(
                "⚠ Multiple backlogs detected."
            )

    if len(insights) == 0:
        insights.append(
            "✅ No major academic warning signs detected."
        )

    for insight in insights:
        st.write(insight)

    st.markdown("---")

    st.subheader("🎯 Recommendations")

    recommendations = []

    if student_data["GPA"].values[0] < 5:
        recommendations.append(
            "📘 Schedule academic counselling."
        )

    if (
        "Attendance_Pct"
        in student_data.columns
    ):

        if (
            student_data[
                "Attendance_Pct"
            ].values[0] < 75
        ):
            recommendations.append(
                "👨‍🏫 Assign attendance mentor."
            )

    if (
        "Backlogs"
        in student_data.columns
    ):

        if (
            student_data[
                "Backlogs"
            ].values[0] >= 2
        ):
            recommendations.append(
                "📝 Arrange tutoring support."
            )

    if len(recommendations) == 0:
        recommendations.append(
            "✅ Student performing well."
        )

    for rec in recommendations:
        st.write(rec)

# ==================================================
# GPA Trend Chart
# ==================================================
st.markdown("---")
st.subheader("📈 Academic Performance Trend")

semester_columns = [
    col for col in student_data.columns
    if "GPA_Sem" in col
]

if len(semester_columns) > 0:

    gpa_values = [
        student_data[col].values[0]
        for col in semester_columns
    ]

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.plot(
        range(
            1,
            len(gpa_values)+1
        ),
        gpa_values,
        marker="o"
    )

    ax.set_title(
        "Semester-wise GPA Trend"
    )

    ax.set_xlabel(
        "Semester"
    )

    ax.set_ylabel(
        "GPA"
    )

    st.pyplot(fig)

else:
    st.info(
        "Semester GPA data not available."
    )
