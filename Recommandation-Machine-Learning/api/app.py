from model_wrapper import VehiculeClassificaionModel
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

model = VehiculeClassificaionModel('config.ini')

feature_names = ['age','sexe','taux','nbEnfantsAcharge','situationFamiliale','2emevoiture']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    X = [request.form[x] for x in feature_names]
    X[0] = int(X[0])
    X[2] = int(X[2])
    X[3] = int(X[3])
    X[5] = bool(X[3])

    data = pd.DataFrame([X],columns=feature_names)

    prediction = model.predict(data)

    prediction_name = model.labels_map[prediction[0]]

    output_data = model.postprocess(prediction)

    return render_template('home.html', 
                           pred_target=f'La catégorie de voiture recommandée est : <b>{prediction_name}</b>',
                           pred_features =output_data.to_html(index=False))

if __name__ == '__main__':
    app.run(debug=True)