import gradio as gr
from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Prediction function
def analyze_sentiment(text):

    result = classifier(text)

    label = result[0]["label"]
    score = round(result[0]["score"] * 100, 2)

    return f"Sentiment: {label}\nConfidence Score: {score}%"


# Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as ui:

    gr.Markdown("# AI Sentiment Analyzer")
    gr.Markdown("Enter text and detect sentiment using Hugging Face Transformers.")

    with gr.Row():

        with gr.Column():

            input_text = gr.Textbox(
                label="Enter Text",
                placeholder="Type or paste text here...",
                lines=8
            )

            analyze_btn = gr.Button(
                "Analyze Sentiment",
                variant="primary"
            )

        with gr.Column():

            output = gr.Textbox(
                label="Result",
                lines=4
            )

    analyze_btn.click(
        fn=analyze_sentiment,
        inputs=input_text,
        outputs=output
    )

ui.launch()