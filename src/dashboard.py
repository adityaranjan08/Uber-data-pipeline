import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Uber Ride Dashboard", layout="wide")
st.title("Uber Ride Analytics Dashboard")
st.write("Streamlit is working.")  # Test rendering

# Load data
try:
    conn = sqlite3.connect("data/uber_rides.db")
    df = pd.read_sql_query("SELECT * FROM uber_rides", conn)
    conn.close()
    st.success("Data loaded from SQLite")
except Exception as e:
    st.error(f"Failed to load data: {e}")

# If data is loaded, show charts
if 'df' in locals():
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rides", len(df))
    col2.metric("Avg. Fare (₹)", round(df["fare_amount"].mean(), 2))
    col3.metric("Avg. Rating", round(df["rating"].mean(), 2))

    st.markdown("---")
    st.subheader("Ride Count by Pickup Location")
    st.bar_chart(df["pickup_location"].value_counts())

    st.subheader("Fare Trends Over Time")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    fare_by_day = df.groupby(df["timestamp"].dt.date)["fare_amount"].sum()
    st.line_chart(fare_by_day)

    st.subheader("Payment Method Breakdown")
    st.write(df["payment_method"].value_counts())

    st.markdown("Raw Ride Data")
    st.dataframe(df)
