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
st.title("👨‍💻 Project Portfolio")
st.markdown("Welcome! Here's a showcase of my work.")

# project = st.selectbox("🔍 Choose a Project", [
#     "Home",
#     "Churn",
#     "Dynamic Pricing - Static Summary"
# ])

col1, col2 = st.columns(2)

with col1:
    st.image("https://img.icons8.com/external-flatart-icons-outline-flatarticons/64/000000/external-customer-retention-digital-marketing-flatart-icons-outline-flatarticons.png", width=50)
    st.subheader("Churn Prediction")
    if st.button("🔍 Explore Churn Prediction"):
        st.session_state.project = "Churn"

with col2:
    st.image("https://img.icons8.com/external-flatart-icons-outline-flatarticons/64/000000/external-price-tag-e-commerce-flatart-icons-outline-flatarticons.png", width=50)
    st.subheader("Dynamic Pricing")
    if st.button("📈 Explore Dynamic Pricing Summary"):
        st.session_state.project = "Dynamic Pricing - Static Summary"

if "project" in st.session_state:
    selected = st.session_state.project

    if selected == "Churn":
        from projects.ChurnPrediction.pages import Page_demo
        Page_demo.render()
        st.stop()

    elif selected == "Dynamic Pricing - Static Summary":
        # from projects.DynamicPricing.pages import 1_Price_Insights
        price_static.render()
        st.stop()


# if project == "Churn":
#     page_demo.render()
#     st.stop()


# elif project == "Dynamic Pricing - Static Summary":
#     price_static.render()
#     st.stop()


# else:
#     st.subheader("🏠 Home")
#     st.write("Select a project from the dropdown above.")