import streamlit as st
from graph import graph

st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="centered"
)

st.title(" AI Study Planner")
st.write("Generate a personalized study plan using LangGraph + Gemini AI.")

# User Inputs
name = st.text_input("Enter your name")

subjects = st.text_input(
    "Enter subjects (comma separated)",
    placeholder="Python, DBMS, Operating Systems"
)

hours = st.number_input(
    "Study Hours Per Day",
    min_value=1,
    max_value=24,
    value=4
)

exam_days = st.number_input(
    "Days Left for Exam",
    min_value=1,
    value=10
)

if st.button("Generate Study Plan"):

    if not name or not subjects:
        st.warning("Please fill in all the fields.")
    else:

        state = {
            "name": name,
            "subjects": [subject.strip() for subject in subjects.split(",")],
            "hours": hours,
            "exam_days": exam_days,
            "plan": ""
        }

        with st.spinner("Generating your study plan..."):
            result = graph.invoke(state)

        st.success("Study Plan Generated Successfully!")

        st.subheader("Your Personalized Study Plan")
        st.write(result["plan"])
