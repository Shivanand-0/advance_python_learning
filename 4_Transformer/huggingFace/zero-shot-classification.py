# classifing text in calegory without trining model with related context.
# when we don't have labeled data, category changes frequently then we use zero shot classification.



from transformers import pipeline

classifier=pipeline('zero-shot-classification')
text='This food is very tasty. how can i buy more?'
label=['nutral','negetive','positive']
result=classifier(text,label)

print(result)