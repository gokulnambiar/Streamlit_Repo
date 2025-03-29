import streamlit as st
from PIL import Image

st.title("👨‍💻 Gokul's Data Science Project Showcase")
st.write("Explore my portfolio of data-driven projects below:")

# Project 1: EV Prediction
st.subheader("🔋 Electric Vehicle Usage Prediction")
ev_img = Image.open("images/ev_placeholder.png")
st.image(ev_img, caption="Time-series forecasting with LSTM", use_column_width=True)
st.markdown("**Overview**: A time-series model using LSTM to forecast electric vehicle usage.")
st.markdown("[View Code](https://github.com/gokulnambiar/ev-forecasting)")

# Project 2: Fraud Detection
st.subheader("💳 Financial Fraud Detection")
fraud_img = Image.open("images/fraud_placeholder.png")
st.image(fraud_img, caption="Random Forest with SHAP explainability", use_column_width=True)
st.markdown("**Overview**: A model to detect suspicious transactions and interpret results using SHAP.")
st.markdown("[View Code](https://github.com/gokulnambiar/fraud-detection)")

# Project 3: Image Generation using GANs
st.subheader("🧠 Image Generation with GANs")
st.markdown("**Overview**: A DCGAN that generates synthetic handwritten digits.")
st.markdown("[View Code](https://github.com/gokulnambiar/image-gen-gan)")
