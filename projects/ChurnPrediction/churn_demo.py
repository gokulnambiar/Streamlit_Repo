import pandas as pd
import shap
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

@st.cache_resource
def load_data_and_model():
    df = pd.read_csv("projects/ChurnPrediction/dataset/telco_churn.csv")

    # Clean up and fix TotalCharges to float
    df = df[df["TotalCharges"] != " "]
    df["TotalCharges"] = df["TotalCharges"].astype(float)
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    df = df.drop(columns=["customerID"])

    le_dict = {}
    for col in df.select_dtypes("object").columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        le_dict[col] = le

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model, X.columns.tolist(), le_dict

model, feature_names, encoders = load_data_and_model()

# --- Streamlit UI ---
def run_demo():
    
    st.title("📊 Real-Time Customer Churn Prediction")
    
    st.markdown("""
    Use this tool to simulate different customer profiles and predict whether they are likely to churn based on historical patterns.

    ---

    ### 🗃️ Dataset Used
    This demo uses the **Telco Customer Churn dataset**, which includes information about 7043 customers:
    - Demographics like `gender`, `SeniorCitizen`, `Partner`, `Dependents`
    - Service details: `InternetService`, `PhoneService`, `TechSupport`, etc.
    - Financials: `MonthlyCharges`, `TotalCharges`
    - Contractual information: `Contract`, `PaymentMethod`, `tenure`
    - Target column: **`Churn`** (Yes/No)

    ---

    ### 🤖 Model Info
    - Model Type: **Random Forest Classifier**
    - Categorical columns encoded using **LabelEncoder**
    - Trained with:
        - `MonthlyCharges`, `tenure`
        - `Contract`, `PaymentMethod`, `TechSupport`, `InternetService`
    - Decision threshold customizable via the slider

    ---

    ### 🔍 What You Can Do
    - Simulate a customer's profile using the form below
    - Adjust decision threshold (0–100%)
    - Get prediction + churn probability
    - View feature contribution (SHAP waterfall + full breakdown)
    """)

    monthly_charges = st.slider("Monthly Charges", 0, 200, 70)
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    threshold_percent = st.slider("Decision Threshold (%)", 0, 100, 50, 5)
    threshold = threshold_percent / 100  # convert to float between 0.0 and 1.0 

    def transform_input():
        row = {
            "MonthlyCharges": monthly_charges,
            "tenure": tenure,
            "Contract": encoders["Contract"].transform([contract])[0],
            "PaymentMethod": encoders["PaymentMethod"].transform([payment_method])[0],
            "TechSupport": encoders["TechSupport"].transform([tech_support])[0],
            "InternetService": encoders["InternetService"].transform([internet_service])[0],
        }

        # for feat in feature_names:
        #     if feat not in row:
        #         row[feat] = 0

        # return pd.DataFrame([row])
        input_df = pd.DataFrame([row])
        input_df = input_df.reindex(columns=feature_names, fill_value=0)
        return input_df

    if st.button("Predict Churn"):
        input_df = transform_input()
        # Get probability of churn
        prob = model.predict_proba(input_df)[0][1]
        

        # Make decision based on user-defined threshold
        if prob >= threshold:
            st.error(f"❌ Prediction: Will Churn")
        else:
            st.success(f"✅ Prediction: Will Not Churn")

        st.info(f"🔢 Churn Probability: {round(prob * 100, 2)}%")

        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(input_df)

        st.write("📉 Feature Contribution (SHAP Waterfall)")
        shap_values = explainer.shap_values(input_df)

        # Handle binary classification safely
        if isinstance(shap_values, list) and len(shap_values) > 1:
            class_idx = 1  # class "churn"
        else:
            class_idx = 0  # fallback for single-class result

        fig, ax = plt.subplots()
        shap.plots._waterfall.waterfall_legacy(
            explainer.expected_value[class_idx],
            shap_values[class_idx][0],
            feature_names=input_df.columns,
            max_display=10,
            show=False
        )
        st.pyplot(fig)
        
        # Extract SHAP values for this instance
        shap_vals = shap_values[class_idx][0]

        # Align SHAP values with features
        if len(shap_vals) == len(input_df.columns):
            shap_df = pd.DataFrame({
                "Feature": input_df.columns,
                "SHAP Value": shap_vals
            }).sort_values(by="SHAP Value", key=abs, ascending=False)

            st.write("🔬 Full SHAP Breakdown:")
            st.dataframe(shap_df, use_container_width=True)
        else:
            st.warning("⚠️ Could not align SHAP values with input features.")