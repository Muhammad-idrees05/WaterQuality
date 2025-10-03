# -*- coding: utf-8 -*-
"""
Water Quality Prediction App
Author: Master
"""

import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import base64

# =======================
# Load Model and Scaler
# =======================
load_model = pickle.load(open('D:/All Tasks/XGBoost/waterQuality.sav', 'rb'))

# Try loading scaler if available
try:
    scaler = pickle.load(open("D:/All Tasks/XGBoost/scaler.sav", "rb"))
    use_scaler = True
except:
    scaler = None
    use_scaler = False

# =======================
# Set Background Image
# =======================
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("D:/All Tasks/XGBoost/IMG-20250207-WA0194.jpg")

# =======================
# Custom CSS Styling (Black Text)
# =======================
st.markdown("""
    <style>
        h1 {
            color: #000000;   /* Black */
            text-align: center;
            font-family: 'Arial', sans-serif;
            text-shadow: none;
        }
        h2, h3, h4, h5, h6, p, label, div {
            color: #000000 !important;  /* Force black text everywhere */
        }
        .stButton>button {
            background-color: #0077b6;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #0096c7;
            color: white;
        }
        .result-box {
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #000000;  /* Black text in result box */
        }
    </style>
""", unsafe_allow_html=True)

# =======================
# Title
# =======================
st.title("💧 Water Quality Prediction App")

def main():
    st.markdown("### 📝 Enter the water test values below")

    # Use columns for cleaner layout
    col1, col2, col3 = st.columns(3)

    with col1:
        Ph_value = st.number_input("pH value", step=0.01)
        Hardness_value = st.number_input("Hardness", step=0.01)
        Solids_value = st.number_input("Solids", step=0.01)
    with col2:
        Chloramines_value = st.number_input("Chloramines", step=0.01)
        Sulfate_value = st.number_input("Sulfate", step=0.01)
        Conductivity_value = st.number_input("Conductivity", step=0.01)
    with col3:
        Organic_carbon_value = st.number_input("Organic Carbon", step=0.01)
        Trihalomethanes_value = st.number_input("Trihalomethanes", step=0.01)
        Turbidity_value = st.number_input("Turbidity", step=0.01)

    # =======================
    # Prediction Button
    # =======================
    if st.button("🔍 Predict Water Quality"):
        try:
            # Create DataFrame
            data = pd.DataFrame([[
                Ph_value,
                Hardness_value,
                Solids_value,
                Chloramines_value,
                Sulfate_value,
                Conductivity_value,
                Organic_carbon_value,
                Trihalomethanes_value,
                Turbidity_value
            ]], columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate',
                         'Conductivity', 'Organic_carbon',
                         'Trihalomethanes', 'Turbidity'])

            # Apply scaler if available
            if use_scaler:
                data_scaled = scaler.transform(data)
                prediction = load_model.predict(data_scaled)
            else:
                prediction = load_model.predict(data)

            # Show styled result
            if prediction[0] == 1:
                st.success("✅ Water is safe to drink")
                st.markdown(
                    "<div class='result-box' style='background-color:#d8f3dc; color:#2d6a4f;'>"
                    "✅ Prediction: Water is Safe to Drink"
                    "</div>", unsafe_allow_html=True
                )
            else:
                st.error("❌ Water is not safe to drink")
                st.markdown(
                    "<div class='result-box' style='background-color:#ffe5ec; color:#9d0208;'>"
                    "❌ Prediction: Water is Not Safe to Drink"
                    "</div>", unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"⚠️ Error occurred: {e}")

# =======================
# Run Main
# =======================
if __name__ == '__main__':
    main()
