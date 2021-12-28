from flask import Flask, request
import tensorflow
import numpy as np
from pickle import load

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route('/score', methods=['POST'])
def score():
    
    n_inputs = 30
    oversample_model = tensorflow.keras.models.load_model('saved_model/my_model')
    rob_scaler = load(open('scaler.pkl', 'rb'))

    # X is array of 28 elems, [V1..V28]
    features = request.json['X']
    #amount_time is [amount,time]
    amount_time=request.json['amount_time']
    features=amount_time.extend(features)
    predictions=oversample_model.predict(features)
    result = np.argmax(predictions,axis=1)
    return 'fraud' if result==0 else 'not fraud'
