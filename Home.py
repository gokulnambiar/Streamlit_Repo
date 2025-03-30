import streamlit as st
import importlib.util
import os
import sys

st.set_page_config(page_title="Gokul's Portfolio", layout="centered")

# Add project subdirectories to path
sys.path.append(os.path.abspath("projects/ChurnPrediction"))
sys.path.append(os.path.abspath("projects/DynamicPricing"))

# --- Load Churn Demo ---
page_demo_spec = importlib.util.spec_from_file_location(
    "page_demo", "projects/ChurnPrediction/pages/Page_demo.py"
)
page_demo = importlib.util.module_from_spec(page_demo_spec)
page_demo_spec.loader.exec_module(page_demo)

# --- Load Dynamic Pricing - Static Summary ---
price_static_spec = importlib.util.spec_from_file_location(
    "price_static", "projects/DynamicPricing/pages/1_Price_Insights.py"
)
price_static = importlib.util.module_from_spec(price_static_spec)
price_static_spec.loader.exec_module(price_static)

# --- Load Dynamic Pricing - Predict Demo ---
price_predict_spec = importlib.util.spec_from_file_location(
    "price_predict", "projects/DynamicPricing/pages/2_Predict_Price.py"
)
price_predict = importlib.util.module_from_spec(price_predict_spec)
price_predict_spec.loader.exec_module(price_predict)

# --- UI Layout ---
st.title("👨‍💻 Project Portfolio")
st.markdown("Welcome! Here's a showcase of my work:")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/churn.png", width=80)
    st.subheader("Churn Prediction")
    if st.button("🔍 Explore Churn Prediction"):
        st.session_state.project = "Churn"

with col2:
    st.image("assets/pricing.png", width=80)
    st.subheader("Dynamic Pricing – Summary")
    if st.button("📈 View Summary & Train"):
        st.session_state.project = "Dynamic Pricing - Static Summary"

with col3:
    st.image("assets/pricing.png", width=80)
    st.subheader("Dynamic Pricing – Predict")
    if st.button("💡 Try Price Prediction"):
        st.session_state.project = "Dynamic Pricing - Predict"

# --- Route to Selected Project Page ---
if "project" in st.session_state:
    selected = st.session_state.project

    if selected == "Churn":
        page_demo.render()
        st.stop()

    elif selected == "Dynamic Pricing - Static Summary":
        price_static.render()
        st.stop()

    elif selected == "Dynamic Pricing - Predict":
        price_predict.render()
        st.stop()