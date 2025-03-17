import streamlit as st
import tensorflow as tf
import re
import json

# Load the pre-trained Keras model
model = tf.keras.models.load_model('lstm_model.keras')

# Load regex patterns from JSON file
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

# Streamlit app
st.title("Accident Data Extractor")

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