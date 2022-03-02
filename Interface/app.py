from nltk import word_tokenize, WordNetLemmatizer
import nltk
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import taglish_sentiment_analysis_cnn as model
from werkzeug.utils import secure_filename
import os
import pandas as pd
import csv
from io import StringIO
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


app = Flask(__name__)

import os
from os.path import join, dirname, realpath

#global variable 
input_with_polarity = []


# enable debugging mode
app.config["DEBUG"] = True

# Upload folder for files
#UPLOAD_FOLDER = 'C:/Users/johnr/Documents/sentiment-analysis-thesis-FINAL/Interface/static/files/'
UPLOAD_FOLDER = 'C:/Users/AlphaQuadrant/Downloads/SE System Tool/sentiment-analysis-thesis-FINAL/Interface/static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER



#homepage
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/about',methods=['POST','GET'])
def about():
    return render_template("about_us.html")

# Go to analyze page
@app.route('/sentiment',methods=['POST','GET'])
def sentiment():
    return render_template("analyze.html")
    
#predict single input
@app.route('/predict',methods=['POST','GET'])

def predict():
    
    input = request.form.get("sentimentArea")

    if request.method == "POST" and input != '':
        # getting input with name = fname in HTML form
        sentiment = model.predict_single_sentiment(input)
        print(sentiment)
    else:
        return render_template("analyze.html",sentiment='Input is Empty',input_text=input)
    
    if(sentiment[0]==3):
        return render_template("analyze.html",sentiment='Input is invalid')
    
    if(sentiment[0]==2):
        return render_template("analyze.html",sentiment='Predicted Sentiment:  Positive',input_text=input,
                               input = 'Input text: ' + input, positive_percentage = sentiment[1],  negative_percentage = sentiment[2])

    if(sentiment[0]==1):
        return render_template("analyze.html",sentiment='Predicted Sentiment:  Neutral',input_text=input, input =  'Input text: ' 
                               + input, positive_percentage = sentiment[1],  negative_percentage = sentiment[2])

    if(sentiment[0]==0):
        return render_template("analyze.html",sentiment='Predicted Sentiment:  Negative',input_text=input, input =  'Input text: ' 
                               + input, positive_percentage = sentiment[1],  negative_percentage = sentiment[2])


#predict multiple input   
@app.route('/predict_multiple',methods=['POST','GET'])

def uploadFiles():
    #count sentiments with or without emoji
    isEmoji = []

    positive_with_emoji = 0
    positive_no_emoji = 0

    negative_with_emoji = 0
    negative_no_emoji = 0

    neutral_with_emoji = 0
    neutral_no_emoji = 0

    #global variable list for predicted polarity with emoji(True or False)
    global input_with_polarity
    input_with_polarity = []

    # get the uploaded file
    uploaded_file = request.files['file']    
    
    # check if the file is not empty 
    if uploaded_file.filename != '':
        
        if uploaded_file.filename.rsplit('.', 1)[1].lower() != 'csv':
            print("Una")
            return render_template("analyze.html", show = "False")

        

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file
        

        #read the uploaded file
        data = pd.read_csv(file_path,header = None)

        data.columns = ['text']

        sentiment_prediction = []
        emoji = 0
        no_emoji = 0
        
        pos_percent = []
        neg_percent = []

        for text in data['text']:
            polarity = model.predict_sentiment(text)
            
            print("ETOOOOO : ",polarity)
            
            if(polarity[0]==3):
                sentiment_prediction.append("invalid")
            else:
                sentiment_prediction.append(polarity[0])
              
            try:
                pos_percent.append(polarity[2])
            except:
                pos_percent.append('N/A')
                
            try:
                neg_percent.append(polarity[3])
            except:
                neg_percent.append('N/A')            

            isEmoji.append(polarity[1])

            #count inputs with emoji and w/o emoji
            if(polarity[1]):
                emoji += 1
            else:
                no_emoji += 1

        #write to csv
        


        #save the text and its respective polarity into list of list
        for n in range(len(data['text'])):
            input_with_polarity.append([data['text'][n],sentiment_prediction[n],isEmoji[n],pos_percent[n],neg_percent[n]])

            if(sentiment_prediction[n] == 0 ):
                if(isEmoji[n] == 1):
                    negative_with_emoji +=1
                else:
                    negative_no_emoji +=1

            elif(sentiment_prediction[n] == 1 ):
                if(isEmoji[n] == 1):
                    neutral_with_emoji +=1
                else:
                    neutral_no_emoji +=1

            elif(sentiment_prediction[n] == 2 ):
                if(isEmoji[n] == 1):
                    positive_with_emoji +=1
                else:
                    positive_no_emoji +=1
        
        pos = 0
        neg = 0
        neu = 0

        for sentiment in sentiment_prediction:
            if(sentiment==0):
                neg+=1
            if(sentiment==2):
                pos+=1
            if(sentiment==1):
                neu+=1
        
        invalid_qty = len(data['text'])-(pos + neg)
        print('positive: ',pos,'  negative: ',neg,'  neutral: ',neu)
        print('with emoji: ',emoji,'   without emoji: ',no_emoji)
        print('Positive with emoji:',positive_with_emoji,'  Positive w/o emoji: ',positive_no_emoji)
        print('Negative with emoji:',negative_with_emoji,'  Negative w/o emoji: ',negative_no_emoji)
        print('Neutral with emoji:',neutral_with_emoji,'  Neutral w/o emoji: ',neutral_no_emoji)

        empty_file = 1
    else:
        empty_file = 0
    
    #start ako dito 
    header = ['Text', 'Polarity','Emoji present','Positive Percentage','Negative Percentage']

    si = StringIO()
        
    #with open('summarize.csv', 'w',newline='', encoding='UTF8') as f:
    writer = csv.writer(si)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(input_with_polarity)):
        print(i,' ',input_with_polarity[i])
        writer.writerow(input_with_polarity[i])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
        
    if(empty_file == 1):
        print("Okay pasok")
        return render_template("analyze.html", positive = 'Positive: ', positive_qty = pos, 
                               
        negative= 'Negative:', negative_qty = neg, neutral= 'Neutral:', neutral_qty = neu,
        
        with_emoji_label = 'With Emoji: ',with_emoji=emoji,
        
        wo_emoji_label = 'Without Emoji: ', wo_emoji=no_emoji,
        
        positive_emoji_label = 'Positive with Emoji: ',positive_with_emoji = positive_with_emoji,
        
        negative_emoji_label = 'Negative with Emoji',negative_with_emoji = negative_with_emoji,
        
        neutral_emoji_label = 'Neutral with Emoji: ',neutral_with_emoji = neutral_with_emoji,
        
        positive_no_emoji_label = 'Positive w/o Emoji',positive_no_emoji = positive_no_emoji,
        
        neutral_no_emoji_label = 'Neutral w/o Emoji: ',neutral_no_emoji = neutral_no_emoji,
        
        negative_no_emoji_label = 'Negative w/o Emoji: ',negative_no_emoji = negative_no_emoji,
        
        show = "True",invalid = "invalid: ", invalid_qty = len(data['text'])-(pos + neg))
        
    else:
        print("Pangalawa")
        return render_template("analyze.html", show = "Empty")
    


#download csv copy   
@app.route('/download',methods=['POST','GET'])

def download():

    header = ['Text', 'Polarity','Emoji present','Positive Percentage','Negative Percentage']

    si = StringIO()
        
    #with open('summarize.csv', 'w',newline='', encoding='UTF8') as f:
    writer = csv.writer(si)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(input_with_polarity)):
        print(i,' ',input_with_polarity[i])
        writer.writerow(input_with_polarity[i])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
        
    return output

if __name__ == '__main__':
    app.run(debug=True)