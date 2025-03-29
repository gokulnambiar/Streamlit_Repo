import importlib.util
import streamlit as st
import os
import sys

# Ensure current directory and subfolders are on sys.path
sys.path.append(os.path.abspath("."))  # adds root
sys.path.append(os.path.abspath("projects/ChurnPrediction"))  # adds the churn module

# Dynamically import page modules
page_demo_spec = importlib.util.spec_from_file_location(
    "page_demo", "projects/ChurnPrediction/pages/Page_demo.py"
)
page_demo = importlib.util.module_from_spec(page_demo_spec)
page_demo_spec.loader.exec_module(page_demo)

# page_summary_spec = importlib.util.spec_from_file_location(
#     "page_summary", "projects/ChurnPrediction/pages/page_summary.py"
# )
# page_summary = importlib.util.module_from_spec(page_summary_spec)
# page_summary_spec.loader.exec_module(page_summary)

st.set_page_config(page_title="Gokul's Portfolio", layout="centered")

st.title("👨‍💻 Gokul's Data Science Portfolio")
st.markdown("Welcome! Here's a showcase of my work.")

project = st.selectbox("🔍 Choose a Project", [
    "Home",
    # "Churn Prediction - Summary",
    "Churn Prediction - Demo"
])

# if project == "Churn Prediction - Summary":
#     page_summary.render()
if project == "Churn Prediction - Demo":
    page_demo.render()
else:
    st.subheader("🏠 Home")
    st.write("Select a project from the dropdown above.")