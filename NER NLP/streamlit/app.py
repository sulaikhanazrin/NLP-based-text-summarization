import streamlit as st
import spacy
import re
import subprocess
import importlib.util

# ✅ Ensure spaCy model is downloaded and loaded
@st.cache_resource
def load_spacy_model():
    model_name = "en_core_web_sm"
    try:
        return spacy.load(model_name)
    except OSError:
        # If model is not installed, download it
        subprocess.run(["python", "-m", "spacy", "download", model_name])
        return spacy.load(model_name)

nlp = load_spacy_model()

# -----------------------------
# 🔍 NER + Regex Extractor
# -----------------------------
def extract_summary(text):
    doc = nlp(text)

    summary = {
        "district": "unknown",
        "date": "unknown",
        "time": "unknown",
        "deaths": "0",
        "grievous": "0",
        "minor": "0",
        "type": "unknown",
        "recommendation": "N/A"
    }

    for ent in doc.ents:
        if ent.label_ == "GPE" and summary["district"] == "unknown":
            summary["district"] = ent.text
        elif ent.label_ == "DATE" and summary["date"] == "unknown":
            summary["date"] = ent.text
        elif ent.label_ == "TIME" and summary["time"] == "unknown":
            summary["time"] = ent.text

    # Regex extraction
    if match := re.search(r"(?:death|fatalit(?:y|ies))\D*(\d+)", text, re.IGNORECASE):
        summary["deaths"] = match.group(1)

    if match := re.search(r"grievous injuries?\D*(\d+)", text, re.IGNORECASE):
        summary["grievous"] = match.group(1)

    if match := re.search(r"minor injuries?\D*(\d+)", text, re.IGNORECASE):
        summary["minor"] = match.group(1)

    if match := re.search(r"accident type was\s*([a-zA-Z\s]+)", text, re.IGNORECASE):
        summary["type"] = match.group(1).strip()

    if match := re.search(r"recommendation:\s*(.*)", text, re.IGNORECASE):
        summary["recommendation"] = match.group(1).strip()

    return summary

# -----------------------------
# 🌐 Streamlit UI
# -----------------------------
st.set_page_config(page_title="NER Accident Extractor", layout="wide")
st.title("🚨 Accident Report Summary Extractor")
st.markdown("Paste any accident paragraph below to extract key details using spaCy NER and regex.")

# Example text collapsible
with st.expander("📋 Example Paragraphs (Click to View)", expanded=False):
    st.markdown("""
**Example 1:**  
`On 01 Dec 2021 at 05:30 PM, an accident occurred in THIRUVANANTHAPURAM CITY under the jurisdiction of Vattiyoorkavu police station. The accident type was Minor Injury. There were 0 fatalities, 0 grievous injuries, and 2 minor injuries. The accident took place at MOOTHAKUNNAM in a Rural. Weather conditions were Sunny/Clear, with Good visibility. The road type was National Highway with features such as Straight Road. The accident involved a Tipper and a Motor Cycle. Spot classification: Near bus stop. Traffic control at the scene was Uncontrolled. Recommendation: Improve general road safety awareness and enforcement.`

**Example 2:**  
`On 31 Dec 2024 at 06:30 AM, an accident occurred in THIRUVANANTHAPURAM CITY under the jurisdiction of Vanchiyoor police station. The accident type was Fatal. There were 1 fatalities, 0 grievous injuries, and 0 minor injuries. The accident took place at KAVILNADA in a Rural. Weather conditions were Sunny/Clear, with Good visibility. The road type was National Highway with features such as Straight Road. The accident involved a Motor Cycle and a Motor Cycle. Spot classification: At pedestrian crossing. Traffic control at the scene was Uncontrolled. Recommendation: Improve pedestrian crossings and install better signage. Increase road safety measures and emergency response times.`

**Example 3:**  
`On 15 Jan 2024 at 07:00 PM, an accident occurred in ALAPPUZHA under the jurisdiction of Mannachery police station. The accident type was Grevious Injury. There were 0 fatalities, 1 grievous injuries, and 0 minor injuries. The accident took place at KERALAPURAM in a Rural. Weather conditions were Sunny/Clear, with Good visibility. The road type was National Highway with features such as Others. The accident involved a Scooter and a Car. Spot classification: In Open area. Traffic control at the scene was Uncontrolled. Recommendation: Improve general road safety awareness and enforcement.`

**Example 4:**  
`On 14 Jan 2021 at 08:00 AM, an accident occurred in ERNAKULAM RURAL under the jurisdiction of Aluva West police station. The accident type was Grevious Injury. There were 0 fatalities, 1 grievous injuries, and 0 minor injuries. The accident took place at CHETTIVILA JN in a Rural. Weather conditions were Sunny/Clear, with Good visibility. The road type was Other Road with features such as Curved Road. The accident involved a Scooter and a Motor Cycle. Spot classification: Near bus stop. Traffic control at the scene was Uncontrolled. Recommendation: Improve general road safety awareness and enforcement.`

**Example 5:**  
`On 03 Jan 2024 at 10:00 AM, an accident occurred in PALAKKAD under the jurisdiction of Kuzhalmannam police station. The accident type was Minor Injury. There were 0 fatalities, 0 grievous injuries, and 1 minor injuries. The accident took place at KAKKAYANGAD in a Rural. Weather conditions were Sunny/Clear, with Good visibility. The road type was Other Road with features such as Others. The accident involved a Lorry and a Motor Cycle. Spot classification: In Residential area. Traffic control at the scene was Uncontrolled. Recommendation: Improve pedestrian crossings and install better signage.`
""")

# Text Input
input_text = st.text_area("📝 Paste Unstructured Accident Text Here:", height=250)

if st.button("🔍 Generate Summary"):
    if not input_text.strip():
        st.warning("Please paste some text first.")
    else:
        result = extract_summary(input_text)

        st.markdown("### ✅ Extracted Information:")
        st.markdown(f"""
        ---
        **📍 District:** {result['district']}  
        **📅 Date:** {result['date']}  
        **⏰ Time:** {result['time']}  
        **💀 Deaths:** {result['deaths']}  
        **🚑 Grievous Injuries:** {result['grievous']}  
        **🩹 Minor Injuries:** {result['minor']}  
        **📝 Type:** {result['type']}  
        **✅ Recommendation:** {result['recommendation']}
        """)
