# 🧠 Accident Report Summarization using Named Entity Recognition (NER)

This project is a lightweight, real-time accident summarization tool built using **spaCy's Named Entity Recognition (NER)** and **custom regular expressions**. It is designed to extract structured summaries from unstructured accident report paragraphs such as date, time, district, deaths, injuries, type of accident, and recommendation.

---

## 🔁 Background

Previously, a similar project was developed using **LSTM + Regex-based summarization**, hosted at:  
🔗 [NLP-based-text-summarization (GitHub)](https://github.com/sulaikhanazrin/NLP-based-text-summarization)

While that model worked well, it was complex, training-heavy, and required more compute. Therefore, this new NER-based version is:

- ✅ Simpler and faster (no training required)
- ✅ Lightweight and easy to deploy
- ✅ Accurate for structured entity extraction
- ✅ Ideal for rule-based government data analytics

---

## 📌 Objective

Extract key accident information from unstructured text using spaCy NER and display it in a clean, structured format.  
The extracted fields are:

- **District**
- **Date**
- **Time**
- **Deaths**
- **Grievous Injuries**
- **Minor Injuries**
- **Accident Type**
- **Recommendation**

---

## 🚀 Features

- Accepts raw accident descriptions (paragraphs)
- Uses `spaCy`'s NER model (`en_core_web_sm`) for entity extraction
- Custom regex rules for numeric fields (injuries, deaths, type)
- Streamlit web interface for real-time usage
- Example texts for easy testing
- Outputs a clear summary instantly

---

## 📂 Folder Structure

NER-NLP/
│
├── streamlit/
│ └── app.py # Main Streamlit app interface
│
├── NER-NLP.ipynb # Jupyter Notebook for processing and NER logic
├── final_accident_data.csv # Raw accident data with unstructured text
├── ner_summarized_data.csv # Final structured data output after NER + regex
├── README.md # This documentation file
└── requirements.txt # Dependencies for deployment


---

## 🧪 Sample Inputs & Outputs

**Example Input:**

On 01 Dec 2021 at 05:30 PM, an accident occurred in THIRUVANANTHAPURAM CITY under the jurisdiction of Vattiyoorkavu police station. The accident type was Minor Injury. There were 0 fatalities, 0 grievous injuries, and 2 minor injuries. The accident took place at MOOTHAKUNNAM in a Rural area... Recommendation: Improve general road safety awareness and enforcement.

**Generated Summary:**

📍 District: THIRUVANANTHAPURAM CITY
📅 Date: 01 Dec 2021
⏰ Time: 05:30 PM
💀 Deaths: 0
🚑 Grievous Injuries: 0
🩹 Minor Injuries: 2
📝 Type: Minor Injury
✅ Recommendation: Improve general road safety awareness and enforcement.

---

## 📊 Technologies Used

- `spaCy` for Named Entity Recognition
- `re` for regex-based pattern matching
- `pandas` for data manipulation
- `Streamlit` for interactive app
- `Python` (3.10+)

---

## 🌍 Live Deployment (via Streamlit Cloud)

The app is deployed on **Streamlit Cloud** and can be accessed at:  
👉 [[https://ner-nlp.streamlit.app](https://ner-nlp-hkduksfhgcnufp7cjbucqp.streamlit.app/)]() 

---
