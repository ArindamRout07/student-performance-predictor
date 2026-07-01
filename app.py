import streamlit as st
import pandas as pd
import joblib


model = joblib.load("model/student_performance_model.pkl")
st.title(" Student Performance Predictor")
st.write(
    "Predict a student's Math Score using demographic information and academic performance.")

st.header(" Enter Student Details")
gender = st.selectbox(
    "Gender",
    ["female", "male"]
)
race = st.selectbox(
    "Race/Ethnicity",
    [
        "group A",
        "group B",
        "group C",
        "group D",
        "group E"
    ]
)
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
lunch = st.selectbox(
    "Lunch Type",
    [
        "standard",
        "free/reduced"
    ]
)
test_prep = st.selectbox(
    "Test Preparation Course",
    [
        "none",
        "completed"
    ]
)
reading_score = st.slider(
    "Reading Score",
    0,
    100,
    70
)
writing_score = st.slider(
    "Writing Score",
    0,
    100,
    70
)
predict = st.button("Predict Math Score")