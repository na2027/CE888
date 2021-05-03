#importing the libraries

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Grab all template entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict the features
    prediction = model.predict(array_features)
    
    pred_output = prediction
    
    # Check the pred_output values and retrive the result with html tag based on the value
    if pred_output == 1:
        return render_template('index.html', 
                               result = 'The patient has not heart disease!')
    else:
        return render_template('index.html', 
                               result = 'The patient has heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()
    
    