from transformers import pipeline


ner=pipeline('ner', grouped_entities=True)

text="Shivanand Gupta will be the next world leader."
res=ner(text)

print(res)