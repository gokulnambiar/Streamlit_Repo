import streamlit as st
from projects.ChurnPrediction import churn_demo

def render():
    churn_demo.run_demo()  # Make sure churn_demo.py wraps Streamlit logic in a function