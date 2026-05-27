from transformers import AutoTokenizer, AutoModel

import torch 


tokenizer=AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model=AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')


text="AI is Ammaging"

input= tokenizer(text,return_tensor='pt')

outputs=model(**input)

print(outputs)
# print(outputs.last_hidden_state.shape)