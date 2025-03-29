from projects.ChurnPrediction.pages import page_demo, page_summary

import streamlit as st

st.set_page_config(page_title="Gokul's Portfolio", layout="centered")

st.title("👨‍💻 Gokul's Data Science Portfolio")
st.markdown("Welcome! Here's a showcase of my work.")

project = st.selectbox("🔍 Choose a Project", [
    "Home",
    "Churn Prediction - Summary",
    "Churn Prediction - Demo"
])

if project == "Churn Prediction - Summary":
    page_summary.render()
elif project == "Churn Prediction - Demo":
    page_demo.render()
else:
    st.subheader("🏠 Home")
    st.write("Select a project from the dropdown above.")