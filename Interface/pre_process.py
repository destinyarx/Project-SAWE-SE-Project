from nltk import word_tokenize
import nltk
#nltk.download('punkt')
import os
import collections
import re
import string
from emoji import UNICODE_EMOJI

# search your emoji
def is_emoji(s):
    return s in UNICODE_EMOJI['en']

#add space to the emoji that has no whitespace
def addSpaceEmoji(input):
    
  sentence = ""
  for x in range(len(input)):
      
    if(is_emoji(input[x])):
      sentence = sentence + ' ' + input[x]
    else:
      sentence = sentence + input[x]

  return sentence

# REMOVE PUNCTUATION
def remove_punct(text):
    text_nopunct = ''
    text_nopunct = re.sub('['+string.punctuation+']', '', text)
    return text_nopunct


# CONVERT TO LOWeER CASE
def lowerStemmer(tokens): 
    return [w.lower() for w in tokens] 

# GET AND SAVE THE STOPWORDS INTO LIST
stoplist = ""

with open('C:/Users/AlphaQuadrant/Downloads/SE System Tool/sentiment-analysis-thesis-FINAL/Interface/static/stopwords/stopwords.txt',encoding="utf-8") as f:
#with open('C:/Users/johnr/Documents/sentiment-analysis-thesis-FINAL/Interface/static/stopwords/stopwords.txt',encoding="utf-8") as f:
  contents = f.read()
  stoplist = stoplist + contents
stoplist = word_tokenize(stoplist)

# FUNCTION TO REMOVE STOPWORDS
def removeStopWords(tokens): 
    return [word for word in tokens if word not in stoplist]
