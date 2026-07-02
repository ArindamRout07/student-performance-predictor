import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model/student_performance_model.pkl")

# -----------------------------
# Main Title
# -----------------------------
st.title("🎓 Student Performance Predictor")

st.markdown("""
Predict a student's **Math Score** using demographic information
and academic performance with a Machine Learning model built using
**Scikit-Learn**.
""")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📚 About This Project")

st.sidebar.markdown("""
### Student Performance Predictor

This application predicts a student's **Math Score**
using a trained **Linear Regression** model.

---

### 🛠 Tech Stack

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib

---

### 📈 Model Performance

- **R² Score:** 0.8875
- **MAE:** 4.07
- **RMSE:** 4.98

---

Developed by **Arindam Rout**
""")

# -----------------------------
# Student Details
# -----------------------------
st.header("📋 Enter Student Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["female", "male"]
    )

    race = st.selectbox(
        "Race / Ethnicity",
        [
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ]
    )

    lunch = st.selectbox(
        "Lunch Type",
        [
            "standard",
            "free/reduced"
        ]
    )

with col2:

    parent_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )

    test_prep = st.selectbox(
        "Test Preparation Course",
        [
            "none",
            "completed"
        ]
    )

st.markdown("---")

reading_score = st.slider(
    "📖 Reading Score",
    0,
    100,
    70
)

writing_score = st.slider(
    "✍ Writing Score",
    0,
    100,
    70
)

st.markdown("")

predict = st.button(
    "🎯 Predict Math Score",
    use_container_width=True
)

# -----------------------------
# Prediction
# -----------------------------
if predict:

    input_data = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race],
        "parental level of education": [parent_education],
        "lunch": [lunch],
        "test preparation course": [test_prep],
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    with st.spinner("Analyzing student performance..."):

     prediction = model.predict(input_data)
     

    score = prediction[0]

    st.markdown("---")

    st.subheader("Prediction Result")

    st.metric(
        label="Predicted Math Score",
        value=f"{score:.2f}"
    )

    st.progress(min(int(score), 100))

    if score >= 90:
        st.balloons()
        st.success("🌟 Outstanding Performance!")

    elif score >= 75:
        st.info("📘 Good Performance! Keep practicing.")

    elif score >= 50:
        st.warning("📈 Average Performance. More practice can improve your score.")

    else:
        st.error("📚 Needs Improvement. Focus on strengthening your fundamentals.")