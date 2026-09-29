import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model = joblib.load("housing_model.joblib")

st.set_page_config(page_title="California Housing Price Predictor", page_icon="🏠")
st.title("🏠 California Uy Narxini Bashorat Qilish")
st.write("Quyidagi ma'lumotlarni kiriting va uyning taxminiy narxini bilib oling.")

col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("Longitude", value=-119.5, format="%.4f")
    latitude = st.number_input("Latitude", value=35.6, format="%.4f")
    housing_median_age = st.number_input("Housing Median Age", value=25.0)
    total_rooms = st.number_input("Total Rooms", value=2000.0)
    total_bedrooms = st.number_input("Total Bedrooms", value=400.0)

with col2:
    population = st.number_input("Population", value=1000.0)
    households = st.number_input("Households", value=400.0)
    median_income = st.number_input("Median Income (10 minglab $)", value=3.5)
    ocean_proximity = st.selectbox(
        "Ocean Proximity",
        ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
    )

if st.button("Narxni bashorat qil"):
    input_df = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Taxminiy uy narxi: **${prediction:,.2f}**")