import pre_process as scan
from nltk import word_tokenize
from tensorflow import keras 
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np
import pickle
from emoji import UNICODE_EMOJI



MAX_SEQUENCE_LENGTH = 50
EMBEDDING_DIM = 300
TRAINING_VOCAB = 2455

# search your emoji
def is_emoji(s):
    return s in UNICODE_EMOJI['en']

#LOAD MODEL
taglish_model = keras.models.load_model('C:/Users/AlphaQuadrant/Downloads/SE System Tool/sentiment-analysis-thesis-FINAL/Interface/static/model/tag-lish_cnn.h5')

#taglish_model = keras.models.load_model('C:/Users/johnr/Documents/sentiment-analysis-thesis-FINAL/Interface/static/model/tag-lish_cnn.h5')

#LOAD TOKENIZER
with open('C:/Users/AlphaQuadrant/Downloads/SE System Tool/sentiment-analysis-thesis-FINAL/Interface/static/model/tokenizer.pickle', 'rb') as handle:

#with open('C:/Users/johnr/Documents/sentiment-analysis-thesis-FINAL/Interface/static/model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


# CONVERT LIST TO STRING
def listToString(s): 
    
  # initialize an empty string
  str1 = " " 
    
  # return string  
  return (str1.join(s))


def predict_sentiment(input):
  
  # PREPROCESSING
  
  # Removing Punctuation
  clean = scan.remove_punct(input)
  print("\nRemoving Punctuation: \n",clean)
  # Add space in emoji 
  clean = scan.addSpaceEmoji(clean)
  print("\nAdd space in emoji: \n",clean)
  
  # Tokenize input
  clean = word_tokenize(clean)
  print("\nTokenize input: \n",clean)
  
  # check if emoji is present 
  emoji = 0

  for x in range(len(clean)):
      if(is_emoji(clean[x])):
        emoji = 1
        break
      if(x == ( len(clean) - 1)):
        emoji = 0
  

  clean = scan.lowerStemmer(clean)
  # Remove stopwords
  clean = scan.removeStopWords(clean)
  print("\nRemove stopwords: \n",clean)
  
  # Convert to strin again so that we can convert it int padding sequences
  input = listToString(clean)

  test = [[]]
  test[0] = clean

  #CONVERT INPUT INTO PADDING
  clean_sequences  = tokenizer.texts_to_sequences(test)
  
  if(len(clean_sequences[0]) == 0):
    return 3,emoji
  
  else:        
    clean_input = pad_sequences(clean_sequences, maxlen=MAX_SEQUENCE_LENGTH)
    print("\nPadding sequences: \n",clean_input)
        
    #model prediction
    input_predictions = taglish_model.predict(clean_input, batch_size=1024, verbose=1)

    #Tensor data computed by model
    print("\nTensor data computed by model: \n",input_predictions)

    labels = [2,0,1]

    # Convert tensor into its highest probability in labels
    input_prediction_labels = labels[np.argmax(input_predictions)]
    
    total = input_predictions[0][0] + input_predictions[0][1]

    positive_percentage = "{:.2f}".format((input_predictions[0][0] / total) * 100)
    negative_percentage = "{:.2f}".format((input_predictions[0][1] / total) * 100)

    print("\nConvert tensor into sentiments: \n",input_prediction_labels)

  return input_prediction_labels,emoji,positive_percentage,negative_percentage
  

def predict_single_sentiment(input):
      
  #PREPROCESSING
  
  # Removing Punctuation
  clean = scan.remove_punct(input)
  print("\nRemoving Punctuation: \n",clean)
  # Add space in emoji 
  clean = scan.addSpaceEmoji(clean)
  print("\nAdd space in emoji: \n",clean)
  
  # Tokenize input
  clean = word_tokenize(clean)
  print("\nTokenize input: \n",clean)
  
  clean = scan.lowerStemmer(clean)
  # Remove stopwords
  clean = scan.removeStopWords(clean)
  print("\nRemove stopwords: \n",clean)
  
  # Convert to strin again so that we can convert it int padding sequences
  input = listToString(clean)


  test = [[]]
  test[0] = clean

  #CONVERT INPUT INTO PADDING
  clean_sequences  = tokenizer.texts_to_sequences(test)
  print("\nSequences value : \n",clean_sequences)
  
  if(len(clean_sequences[0]) == 0):
    print("empty")  
    return 3,2,1
  
  
  clean_input = pad_sequences(clean_sequences, maxlen=MAX_SEQUENCE_LENGTH)
  print("\nPadding sequences: \n",clean_input)
  #model prediction

  # Model predict
  input_predictions = taglish_model.predict(clean_input, batch_size=1024, verbose=1)

  #Tensor data computed by model
  print("\nTensor data computed by model: \n",input_predictions)
  
  labels = [2,0,1]
  
  # Convert tensor into its highest probability in labels
  input_prediction_labels = labels[np.argmax(input_predictions)]

  print("\nConvert tensor into sentiments: \n",input_prediction_labels)
  
  total = input_predictions[0][0] + input_predictions[0][1]

  positive_percentage = "{:.2f}".format((input_predictions[0][0] / total) * 100)
  negative_percentage = "{:.2f}".format((input_predictions[0][1] / total) * 100)
  
  positive_percentage = "Positive Percentage: " + str(positive_percentage) 
  negative_percentage = "Negative Percentage: " + str(negative_percentage) 

  return input_prediction_labels,positive_percentage,negative_percentage