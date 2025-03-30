import streamlit as st
import importlib.util
import os
import sys

st.set_page_config(page_title="Gokul's Portfolio", layout="centered")

# Add module paths
sys.path.append(os.path.abspath("projects/ChurnPrediction"))
sys.path.append(os.path.abspath("projects/DynamicPricing"))

# --- Load Churn Demo Page ---
page_demo_spec = importlib.util.spec_from_file_location(
    "page_demo", "projects/ChurnPrediction/pages/Page_demo.py"
)
page_demo = importlib.util.module_from_spec(page_demo_spec)
page_demo_spec.loader.exec_module(page_demo)

# --- Load Dynamic Pricing Insights Page ---
price_static_spec = importlib.util.spec_from_file_location(
    "price_static", "projects/DynamicPricing/pages/1_Price_Insights.py"
)
price_static = importlib.util.module_from_spec(price_static_spec)
price_static_spec.loader.exec_module(price_static)

# --- UI Layout ---
st.title("👨‍💻 Project Portfolio")
st.markdown("Welcome! Here's a showcase of my work.")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/churn.png", width=80)
    st.subheader("Churn Prediction")
    if st.button("🔍 Explore Churn Prediction"):
        st.session_state.project = "Churn"

with col2:
    st.image("assets/pricing.png", width=80)
    st.subheader("Dynamic Pricing")
    if st.button("📈 Explore Dynamic Pricing Summary"):
        st.session_state.project = "Dynamic Pricing - Static Summary"

# --- Route Based on Selection ---
if "project" in st.session_state:
    selected = st.session_state.project

    if selected == "Churn":
        page_demo.render()
        st.stop()

    elif selected == "Dynamic Pricing - Static Summary":
        price_static.render()
        st.stop()