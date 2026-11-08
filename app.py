import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Water Potability Prediction", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #E8F4F8; }
h1 { color: #1A5276 !important; text-align: center; }
.stButton>button { background-color: #87CEEB !important; color: #1A5276 !important; font-size: 22px !important; font-weight: bold !important; border-radius: 12px !important; width: 100%; padding: 12px !important; border: 2px solid #5DADE2 !important; }
.blue-box { background-color: #87CEEB; padding: 15px; border-radius: 15px; border: 2px solid #5DADE2; }
.grey-box { background-color: #D5D8DC; padding: 15px; border-radius: 15px; border: 2px solid #AEB6BF; }
.light-blue-box { background-color: #AED6F1; padding: 15px; border-radius: 15px; border: 2px solid #85C1E9; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Water Potability Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px; color:#5D6D7E;'><b>Check if water is drinkable or not</b></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px; font-weight:bold; color:#1A5276; background-color:#87CEEB; padding:8px; border-radius:10px;'>Made by: Samina</p>", unsafe_allow_html=True)
st.write("---")

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    model_loaded = True
except:
    model_loaded = False

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div class='blue-box'>", unsafe_allow_html=True)
    ph = st.slider("pH Value", 0.0, 14.0, 7.0)
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='grey-box'>", unsafe_allow_html=True)
    hardness = st.slider("Hardness", 0.0, 400.0, 150.0)
    st.markdown("</div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='light-blue-box'>", unsafe_allow_html=True)
    solids = st.slider("Solids (TDS)", 0.0, 60000.0, 20000.0)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

c4, c5, c6 = st.columns(3)
with c4:
    st.markdown("<div class='grey-box'>", unsafe_allow_html=True)
    chloramines = st.slider("Chloramines", 0.0, 15.0, 7.0)
    st.markdown("</div>", unsafe_allow_html=True)
with c5:
    st.markdown("<div class='blue-box'>", unsafe_allow_html=True)
    sulfate = st.slider("Sulfate", 0.0, 500.0, 250.0)
    st.markdown("</div>", unsafe_allow_html=True)
with c6:
    st.markdown("<div class='grey-box'>", unsafe_allow_html=True)
    conductivity = st.slider("Conductivity", 0.0, 800.0, 400.0)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

c7, c8 = st.columns(2)
with c7:
    st.markdown("<div class='light-blue-box'>", unsafe_allow_html=True)
    organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 14.0)
    st.markdown("</div>", unsafe_allow_html=True)
with c8:
    st.markdown("<div class='blue-box'>", unsafe_allow_html=True)
    trihalomethanes = st.slider("Trihalomethanes", 0.0, 130.0, 65.0)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    st.markdown("<div class='grey-box'>", unsafe_allow_html=True)
    turbidity = st.slider("Turbidity", 0.0, 7.0, 3.0)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

if st.button("Predict"):
    if model_loaded:
        features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
        prediction = model.predict(features)[0]
    else:
        prediction = 1 if (6.5 <= ph <= 8.5 and turbidity < 5) else 0

    if prediction == 1:
        st.markdown("<div style='background-color:#87CEEB; padding:25px; border-radius:15px; text-align:center; border:3px solid #1A5276;'><h2 style='color:#1A5276; margin:0;'>Water is Potable - Safe to Drink</h2></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='background-color:#5D6D7E; padding:25px; border-radius:15px; text-align:center; border:3px solid #2C3E50;'><h2 style='color:white; margin:0;'>Water is NOT Potable - Do Not Drink</h2></div>", unsafe_allow_html=True)
