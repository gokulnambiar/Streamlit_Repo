import streamlit as st
import pandas as pd
from projects.DynamicPricing import model_utils

def render():
    st.title("🏡 Predict Airbnb Price")

    model = model_utils.load_model()
    df = model_utils.load_data()

    # Sample values from dataset
    room_type = st.selectbox("Room Type", df["room_type"].unique())
    neighbourhood = st.selectbox("Neighbourhood Group", df["neighbourhood_group"].unique())
    min_nights = st.slider("Minimum Nights", 1, 30, 3)
    num_reviews = st.slider("Number of Reviews", 0, 300, 10)
    reviews_per_month = st.slider("Reviews per Month", 0.0, 10.0, 1.2)
    availability = st.slider("Availability (days/year)", 0, 365, 180)

    input_df = pd.DataFrame([{
        "room_type": room_type,
        "neighbourhood_group": neighbourhood,
        "minimum_nights": min_nights,
        "number_of_reviews": num_reviews,
        "reviews_per_month": reviews_per_month,
        "availability_365": availability
    }])

    if st.button("Predict Price"):
        price = model.predict(input_df)[0]
        st.success(f"💰 Estimated Price: ${round(price, 2)}")