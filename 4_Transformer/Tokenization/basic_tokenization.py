# basic code

import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

text="Hello! I am Shiv...."

token=word_tokenize(text)

print(token)


