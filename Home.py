import streamlit as st
import importlib.util
import os
import sys

st.set_page_config(page_title="Gokul's Portfolio", layout="centered")

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("projects/ChurnPrediction"))
sys.path.append(os.path.abspath("projects/DynamicPricing"))

# --- Churn ---
page_demo_spec = importlib.util.spec_from_file_location(
    "page_demo", "projects/ChurnPrediction/pages/Page_demo.py"
)
page_demo = importlib.util.module_from_spec(page_demo_spec)
page_demo_spec.loader.exec_module(page_demo)

# --- Dynamic Pricing - Static Summary ---
price_static_spec = importlib.util.spec_from_file_location(
    "price_static", "projects/DynamicPricing/pages/1_Price_Insights.py"
)
price_static = importlib.util.module_from_spec(price_static_spec)
price_static_spec.loader.exec_module(price_static)

# --- UI ---
st.title("👨‍💻 Gokul's Data Science Portfolio")
st.markdown("Welcome! Here's a showcase of my work.")

project = st.selectbox("🔍 Choose a Project", [
    "Home",
    "Churn",
    "Dynamic Pricing - Static Summary"
])

if project == "Churn":
    page_demo.render()
    st.stop()


elif project == "Dynamic Pricing - Static Summary":
    price_static.render()
    st.stop()


else:
    st.subheader("🏠 Home")
    st.write("Select a project from the dropdown above.")