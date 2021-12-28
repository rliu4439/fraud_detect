from flask import Flask, request
import tensorflow
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python11!"

@app.route('/score', methods=['POST'])
def score():
    
    n_inputs = 30
    oversample_model = tensorflow.keras.models.load_model('saved_model/my_model')

    features = request.json['X']
    predictions=oversample_model.predict(features)
    result = np.argmax(oversample_predictions,axis=1)
    return 'fraud' if result==0 else 'not fraud'
