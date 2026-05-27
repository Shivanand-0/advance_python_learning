from transformers import pipeline

generator=pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

res=generator('Machine Learning is ', max_length=50)

print(res)