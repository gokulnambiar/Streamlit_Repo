import pandas as pd
import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline

FEATURES = [
    "room_type", "neighbourhood_group",
    "minimum_nights", "number_of_reviews",
    "reviews_per_month", "availability_365"
]
TARGET = "price"
CATEGORICAL = ["room_type", "neighbourhood_group"]
NUMERIC = ["minimum_nights", "number_of_reviews", "reviews_per_month", "availability_365"]

def load_data(path="projects/DynamicPricing/dataset/AB_NYC_2019.csv"):
    df = pd.read_csv(path)
    df = df[(df["price"] > 30) & (df["price"] < 500)]
    df = df[df["reviews_per_month"].notnull()]
    return df

def save_model(model, path="projects/DynamicPricing/model.pkl"):
    joblib.dump(model, path)

def load_model(path="projects/DynamicPricing/model.pkl"):
    return joblib.load(path)



def train_model(df):
    X = df[FEATURES]
    y = df[TARGET]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL)
    ], remainder="passthrough")

    model = make_pipeline(
        preprocessor,
        XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    )

    model.fit(X, y)
    # save_model(model, "model.pkl")
    return model


# df = load_data("dataset/AB_NYC_2019.csv")
# train_model(df)