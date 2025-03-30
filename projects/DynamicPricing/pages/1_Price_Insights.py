import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from projects.DynamicPricing import model_utils


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from projects.DynamicPricing import model_utils

def render():
    st.header("📊 NYC Airbnb Price Insights")

    df = model_utils.load_data()

    st.subheader("💰 Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["price"], bins=40, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("🏙️ Price by Neighbourhood Group")
    fig, ax = plt.subplots()
    sns.boxplot(x="neighbourhood_group", y="price", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("🎯 Try It Yourself")
    st.markdown("Click below to launch the interactive pricing demo:")

    st.markdown(
        "[👉 Go to Dynamic Pricing Demo](https://gokulnambiar.streamlit.app/projects/DynamicPricing/pages/2_Predict_Price.py)",
        unsafe_allow_html=True
    )


# https://gokulnambiar.streamlit.app

# gokulnambiar/streamlit_repo/main/projects/DynamicPricing/pages/2_Predict_Price.py


# https://share.streamlit.io/gokulcn/your-repo/pages/2_Predict_Price.py