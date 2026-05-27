# text-summerization has two type:
#1) Extractive Summerization: it just extract words from original text to give summery.
#2) Abstractive Summerization: it generate words to give summery.
from transformers import pipeline


ts=pipeline('summarisation',model="facebook/bart-large-cnn")

text="The huggingface_hub library allows you to interact with the Hugging Face Hub, a machine learning platform for creators and collaborators. Discover pre-trained models and datasets for your projects or play with the hundreds of machine learning apps hosted on the Hub. You can also create and share your own models and datasets with the community. The huggingface_hub library provides a simple way to do all these things with Python. Read the quick start guide to get up and running with the huggingface_hub library. You will learn how to download files from the Hub, create a repository, and upload files to the Hub. Keep reading to learn more about how to manage your repositories on the 🤗 Hub, how to interact in discussions or even how to run inference."
res=ts(text)

print(res)