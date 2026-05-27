# run command: python -m streamlit run task.py   

import streamlit as st
from  transformers import pipeline




# 1. Page Configuration
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Sidebar Navigation and Info
with st.sidebar:
    st.title("About the App")
    st.markdown(
        """
    This app uses *Hugging Face** to analyze the emotional tone of text. 
    It computes two primary metrics:
    """
    )
    st.divider()
    st.caption("Built with Python & Streamlit")

# 3. Main Header
st.title("📊 Real-Time Sentiment Analysis Dashboard")
st.markdown("Enter your text below to analyze its underlying sentiment.")

# 4. User Input Area
user_text = st.text_area(
    "Input Text",
    placeholder="Type or paste your text here (e.g., 'I absolutely love this product! The customer service was fantastic.')...",
    height=150,
)

# 5. Core Analysis Logic
# 5. Core Analysis Logic (Using Hugging Face Transformers)
if st.button("Analyze Sentiment", type="primary"):
    if user_text.strip() == "":
        st.warning("Please enter some text to begin the analysis.")
    else:
        # Import pipeline locally to prevent slowdowns on initial app load
        from transformers import pipeline

        # Initialize the pipeline
        classifier = pipeline("sentiment-analysis")

        # Run inference
        result = classifier(user_text)[0]
        hf_label = result["label"].upper()  # Normalize text string casing
        confidence = result["score"]

        # Determine structural classification label based on Model output strings
        if "POS" in hf_label:
            sentiment_label = "Positive"
            sentiment_emoji = "😊"
            status_color = st.success
        elif "NEG" in hf_label:
            sentiment_label = "Negative"
            sentiment_emoji = "😡"
            status_color = st.error
        else:
            sentiment_label = "Neutral"
            sentiment_emoji = "😐"
            status_color = st.info

        st.divider()

        # 6. Display Metrics Blocks
        st.subheader("Analysis Metrics")
        col1, col2 = st.columns(2)

        with col1:
            status_color(f"### **{sentiment_label}** {sentiment_emoji}")
        with col2:
            st.metric(label="Model Confidence Score", value=f"{confidence:.2%}")
