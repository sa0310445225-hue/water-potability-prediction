import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.set_page_config(page_title="Water Prediction", layout="wide")

# CREAM + GREY + WHITE BUTTON + BROWN RESULT
st.markdown("""
<style>
.stApp { background-color: #FFF8E7; }
h1 { color: #4A4A4A !important; text-align: center; }
p { color: #6E6E6E !important; text-align: center; }
div[data-testid="stColumn"] {
    background-color: #EDEDED;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #D9D9D9;
}
.stButton > button {
    background-color: white !important;
    color: #4A4A4A !important;
    border: 2px solid #4A4A4A !important;
    border-radius: 12px !important;
    height: 55px !important;
    font-size: 20px !important;
    font-weight: bold !important;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💧 Water Potability Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p>Check if water is drinkable or not</p>", unsafe_allow_html=True)
st.write("")

# ROW 1 - 4 in one row
c1, c2, c3, c4 = st.columns(4)
with c1: ph = st.slider("pH", 0.0, 14.0, 7.0)
with c2: hardness = st.slider("Hardness", 0.0, 400.0, 150.0)
with c3: solids = st.slider("Solids", 0.0, 50000.0, 20000.0)
with c4: chloramines = st.slider("Chloramines", 0.0, 15.0, 7.0)
st.write("")

# ROW 2 - 4 in one row
c5, c6, c7, c8 = st.columns(4)
with c5: sulfate = st.slider("Sulfate", 0.0, 500.0, 300.0)
with c6: conductivity = st.slider("Conductivity", 0.0, 800.0, 400.0)
with c7: organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 14.0)
with c8: trihalomethanes = st.slider("Trihalomethanes", 0.0, 130.0, 60.0)
st.write("")

# ROW 3 - ONLY 2 boxes now, NO blank boxes
c9, c10 = st.columns(2)
with c9: turbidity = st.slider("Turbidity", 0.0, 7.0, 3.0)
with c10:
    st.write("")
    predict = st.button("Predict")

# RESULT - BROWN + WHITE
if predict:
    data = [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]
    prediction = model.predict(data)
    st.write("")
    if prediction[0] == 1:
        st.markdown("<div style='background-color:#8B5E3C; color:white; text-align:center; padding:18px; border-radius:15px; font-size:22px; font-weight:bold;'>✅ This Water is DRINKABLE</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='background-color:#8B5E3C; color:white; text-align:center; padding:18px; border-radius:15px; font-size:22px; font-weight:bold;'>❌ This Water is NOT DRINKABLE</div>", unsafe_allow_html=True)