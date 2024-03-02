
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask,render_template,request
import numpy as np
import pandas as pd

with open('./SavedMateria/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the Deep Learning Sentiment Model
sentiment_model = load_model('./SavedMateria/Sentiment-BiLSTM.h5')

# Load the Deep Learning Geninuness Model
genuineness_model = load_model('./SavedMateria/Geniuneness Model.h5')

app = Flask(__name__)
app.secret_key = 'YourSecrtekey'

def modelsPredictions(text,attributes):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=100)  # Assuming you have a max_sequence_length defined

    sentiment_prediction = sentiment_model.predict(padded_sequences)
    # genuineness_prediction = genuineness_model.predict([attributes, padded_sequences])

    # Print the predictions
    print("Sentiment Prediction:", sentiment_prediction)
    # print("Genuineness Prediction:",genuineness_prediction )
    
# , int(np.around(genuineness_prediction))
    return int(np.around(sentiment_prediction))

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return value  # Return the original value if it cannot be converted to float
 

@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Access form data submitted by the user
        tweet_text = request.form.get('tweet_text')
        protected = request.form.get('protected')
        retweet = request.form.get('retweet')
        reply_count = request.form.get('reply_count')
        like_count = request.form.get('like_count')
        quote_count = request.form.get('quote_count')
        followers_count = request.form.get('followers_count')
        listed_count = request.form.get('listed_count')
        friends_count = request.form.get('friends_count')
        attrbut = [protected,1,retweet,reply_count,like_count,quote_count,followers_count,listed_count,friends_count]
        # Use the map function to apply the conversion to each element of the list
        attrbut_float = list(map(convert_to_float, attrbut))
        df = pd.DataFrame(attrbut_float, columns=['ColumnName'])
        print(f'Attributes : {attrbut_float}')
        a,b = modelsPredictions(tweet_text,attrbut_float),1        
        
        return render_template('index.html',sent=a,gen=b) 
    
        
    return render_template('index.html',sent=2,gen=2)
