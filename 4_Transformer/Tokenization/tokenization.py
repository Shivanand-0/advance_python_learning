
# ================================================
# using transformer

from transformers import AutoTokenizer

model="bert-base-uncased"
tokenizer=AutoTokenizer.from_pretrained(model)
text="Hello! I am Shiv...."
tokens=tokenizer.tokenize(text)
print(tokens)