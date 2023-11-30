from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)

# Load the sentiment analysis model
with open('LinearSVC.pkl', 'rb') as model_file:
    sentiment_model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def predict():
    # Get the text from the form
    text = request.form['user_input']
    #convert text to list if it is not
    if type(text) == str:
        text = [text]
    count_vector = CountVectorizer(stop_words= 'english', lowercase = True,vocabulary=pickle.load(open("vector_vocabulary.pkl", "rb"))) 
    data= count_vector.fit_transform(text)
    sentiment_model.predict(data)
    if(sentiment_model.predict(data)==1):
        #print bullying on the html page
        return render_template('index.html', user_input='text', sentiment='Offensive')
    else:
        #print non-bullying on the html page
        return render_template('index.html',user_input='text',  sentiment='Non-Offensive')

if __name__ == '__main__':
    app.run(debug=True)
