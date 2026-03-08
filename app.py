
import streamlit as st
import json

st.set_page_config(
    page_title="MedSafe AI",
    page_icon="💊",
    layout="wide"
)

st.markdown("""
<style>
.main {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

h1 {
color: white;
text-align:center;
}

.stButton>button {
background-color:#00c6ff;
color:white;
border-radius:10px;
padding:10px 20px;
font-size:16px;
}

.stTextInput>div>div>input {
border-radius:10px;
}
</style>
""", unsafe_allow_html=True)
from modules.fuzzy_matcher import match_medicine
from modules.interaction_checker import check_interactions
from modules.ocr_reader import extract_text
from modules.symptom_solver import symptom_advice
from modules.side_effect_monitor import analyze_side_effect
from modules.risk_predictor import risk_score


st.title("MedSafe AI")
st.subheader("AI-powered medicine safety assistant")


menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "Medicine Interaction Checker",
        "Prescription OCR",
        "Symptom Solver",
        "Side Effect Monitor",
        "Emergency Risk Predictor"
    ]
)

if menu == "Medicine Interaction Checker":

    st.header("Check Medicine Interactions")

    medicines = st.text_input("Enter medicines separated by comma")

    if st.button("Check"):

        meds = [m.strip() for m in medicines.split(",")]

        salts = []

        for m in meds:
            match, salt = match_medicine(m)

            if match:
                salts.append(salt)

        interactions = check_interactions(salts)

        if interactions:
            for i in interactions:
                st.warning(f"{i[0]} : {i[1]}")
        else:
            st.success("No major interactions found")


elif menu == "Prescription OCR":

    st.header("Upload Prescription")

    file = st.file_uploader("Upload image")

    if file:

        text = extract_text(file)

        st.text_area("Extracted Text", text)


elif menu == "Symptom Solver":

    st.header("Symptom Guidance")

    symptom = st.text_input("Describe your symptom")

    if st.button("Get Advice"):

        advice = symptom_advice(symptom)

        st.info(advice)


elif menu == "Side Effect Monitor":

    st.header("Log Medicine Experience")

    medicine = st.text_input("Medicine name")
    symptom = st.text_input("What did you experience?")

    if st.button("Analyze"):

        result = analyze_side_effect(medicine, symptom)

        st.write(result)


elif menu == "Emergency Risk Predictor":

    st.header("Emergency Risk Check")

    symptoms = st.text_area("Describe symptoms")

    if st.button("Check Risk"):

        result = risk_score(symptoms)

        st.warning(result)