from transformers import pipeline


model_name = "distilbert-base-uncased"
classifier= pipeline("text-classification",model="./fine_tuned_model")


result=classifier("This is funtastic")

print(result)