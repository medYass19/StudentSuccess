import streamlit as st
import pandas as pd
import numpy as np
import pickle
data=pickle.load(open(r"/Users/medyas/Desktop/dataMining.sav","rb"))
df=data["df"]
st.title("Predict your final grade ")
with st.form("student_form"):
    st.subheader("Student Information")

    student_id = st.number_input("Student ID", min_value=1, step=1)
    age = st.number_input("Age", min_value=5, max_value=30, step=1)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    school_type = st.selectbox(
        "School Type",
        ["Public", "Private"]
    )

    parent_education = st.selectbox(
        "Parent Education",
        ["Primary", "Secondary", "High School", "Bachelor", "Master", "PhD"]
    )

    study_hours = st.number_input(
        "Study Hours per Day",
        min_value=0.0, max_value=24.0, step=0.5
    )

    attendance_percentage = st.slider(
        "Attendance Percentage",
        min_value=0.0, max_value=100.0, value=75.0
    )

    internet_access = st.selectbox(
        "Internet Access",
        ["Yes", "No"]
    )

    travel_time = st.selectbox(
        "Travel Time to School",
        ["<15 min", "15–30 min", "30–60 min", ">60 min"]
    )

    extra_activities = st.selectbox(
        "Extra Activities",
        ["Yes", "No"]
    )

    study_method = st.selectbox(
        "Study Method",
        ["Self-study", "Group study", "Online courses", "Tutoring"]
    )

    math_score = st.number_input(
        "Math Score", min_value=0.0, max_value=100.0
    )

    science_score = st.number_input(
        "Science Score", min_value=0.0, max_value=100.0
    )

    english_score = st.number_input(
        "English Score", min_value=0.0, max_value=100.0
    )

    overall_score = st.number_input(
        "Overall Score", min_value=0.0, max_value=100.0
    )

    submit = st.form_submit_button("Predict Final Grade")
