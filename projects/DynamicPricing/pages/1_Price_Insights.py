import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from projects.DynamicPricing import model_utils

st.title("📊 NYC Airbnb Price Insights & Model Training")

df = model_utils.load_data()

st.subheader("💰 Price Distribution")
fig, ax = plt.subplots()
sns.histplot(df["price"], bins=40, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("🏙️ Price by Neighbourhood Group")
fig, ax = plt.subplots()
sns.boxplot(x="neighbourhood_group", y="price", data=df, ax=ax)
st.pyplot(fig)

if st.button("Train & Save Model"):
    model = model_utils.train_model(df)
    model_utils.save_model(model)
    st.success("✅ Model trained and saved to disk as `model.pkl`")
    
    
st.markdown(
        "[👉 Go to Dynamic Pricing Demo](https://share.streamlit.io/gokulcn/your-repo/pages/2_Predict_Price.py)",
        unsafe_allow_html=True
    )

# https://gokulnambiar.streamlit.app