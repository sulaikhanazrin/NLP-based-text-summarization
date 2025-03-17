import streamlit as st
import tensorflow as tf
import re
import json

# Load the pre-trained Keras model
model = tf.keras.models.load_model('lstm_model.keras')

with open('regex_patterns.json', 'r') as f:
    patterns = json.load(f)

def extract_info(text, patterns):
    info = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                info[key] = match.group(1).strip()  # Capture the actual data
            except IndexError:
                info[key] = None
        else:
            info[key] = None
    return info

def format_summary(summary):
    formatted_summary = []
    for key, value in summary.items():
        if value:
            formatted_summary.append(f"{key}: {value}")
    return "\n".join(formatted_summary)

# Sample accident data (Example)
example_data = """
**Example Report 1:**
01 Dec 2021 05:30 PM accident occurred Thiruvananthapuram city jurisdiction Vattiyoorkavu police station accident type Minor Injury 0 fatalities 0 grievous injuries 2 minor injuries accident took place Moothakunnam rural weather conditions Sunny/Clear, Good Visibility road type National Highway features Straight Road accident involved Tipper, Motor Cycle spot classification Near Bus Stop traffic control scene Uncontrolled recommendation Improve general road safety awareness, enforcement

**Example Report 2:**
31 Dec 2024 06:30 PM accident occurred Thiruvananthapuram city jurisdiction Vanchiyoor police station accident type Fatal 1 fatalities 0 grievous injuries 0 minor injuries accident took place Kavilnada rural weather conditions Sunny/Clear, Good Visibility road type National Highway features Straight Road accident involved Motor Cycle spot classification Pedestrian Crossing traffic control scene Uncontrolled recommendation Improve pedestrian crossings, install better signage, increase road safety measures, emergency response times

**Example Report 3:**
05 Jan 2024 12:15 PM accident occurred Thiruvananthapuram city jurisdiction Kazhakkuttom police station accident type Grievous Injury 0 fatalities 1 grievous injuries 0 minor injuries accident took place Ezhipram rural weather conditions Hot, Good Visibility road type Road features Straight Road accident involved Motor Cycle, Scooter spot classification Market/Commercial Area traffic control scene Police Controlled recommendation Improve general road safety awareness, enforcement

**Example Report 4:**
03 Nov 2020 12:40 PM accident occurred Thiruvananthapuram city jurisdiction Peroorkada police station accident type Fatal 1 fatalities 0 grievous injuries 1 minor injuries accident took place Mampuzhakary rural weather conditions Sunny/Clear, Good Visibility road type State Highway features Ongoing Road Works/Under Construction accident involved Auto Rickshaw, Car spot classification Near Bus Stop traffic control scene Flashing Signal/Blinker recommendation Increase road safety measures, emergency response times
"""

# Streamlit app
st.title("Accident Data Extractor")

# Display example data in the sidebar
st.sidebar.subheader("Example Accident Data:")
st.sidebar.text(example_data)

# User input
user_input = st.text_area("Enter cleaned text:", "")

# Generate summary using LSTM model
if st.button("Generate Summary"):
    # Preprocess the input text for the LSTM model
    # Assuming you have a tokenizer and preprocessing function ready
    # input_seq = preprocess_text(user_input)
    # summary = model.predict(input_seq)
    # For simplicity, let's assume the summary is generated directly
    summary = "Generated summary from LSTM model"  # Replace with actual LSTM prediction

    # Extract information using regex
    extracted_info = extract_info(user_input, patterns)
    formatted_info = format_summary(extracted_info)

    # Display the results
    st.subheader("Generated Summary:")
    st.text(summary)

    st.subheader("Extracted Information:")
    st.text(formatted_info)
