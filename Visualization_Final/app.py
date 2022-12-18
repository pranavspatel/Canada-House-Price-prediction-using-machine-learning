from flask import Flask, render_template,request
import numpy as np
import joblib
import datetime 
import time
import pandas as pd

model=joblib.load('regression-model-houseprice.sav')

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')
    
@app.route('/predict', methods=['POST'])
def predict():

    return render_template('home.html')

@app.route('/getresults',methods=['POST'])
def getresults():
    
    
    form_data=request.form

    d1 = pd.to_datetime(form_data['Date'])
    date = d1.toordinal()
    rate=float(form_data['Mortgage_rate'])
    immigrants=float(form_data['Immigrants'])

    test_data=np.array([[rate,date,immigrants]]).reshape(1,3)

    prediction = int(model.predict(test_data)[0])

    results_dict= {"prediction":(prediction)}


    return render_template('results.html',results=results_dict)


if __name__ == "__main__":
   app.run(debug=True)