import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Project FORESIGHT",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("reports/risk_scoring.csv")

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("📈 Project FORESIGHT")
st.subheader("Retail Demand Forecasting & Inventory Risk Dashboard")

st.success("Dataset Loaded Successfully")

# -----------------------------
# KPI Cards
# -----------------------------
st.header("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Total SKU",
        df["sku_id"].nunique()
    )

with col3:
    st.metric(
        "Average Predicted Sales",
        round(df["Predicted_Units_Sold"].mean(),2)
    )

with col4:
    st.metric(
        "Average Inventory",
        round(df["on_hand_units"].fillna(0).mean(),2)
    )

# -----------------------------
# Dataset Preview
# -----------------------------
st.header("📄 Dataset Preview")

st.dataframe(df.head(20))