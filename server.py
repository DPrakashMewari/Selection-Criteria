# -*- coding: utf-8 -*-


import numpy as np
import pickle
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if (request.method == 'POST'):

        Python_score = float(request.values["Python_score"])
        R_score = float(request.values["R_score"])
        DS_score = float(request.values["DS_score"])
        UG = request.values["UG"]
        print(UG)
        UG_Year = request.values["UG_Year"]
        print(UG_Year)
        PG = request.values["PG"]

        PG_Year = request.values["PG_Year"]
        otherskills = request.values["otherskills"]
        print(otherskills)
        score = 0
        if (Python_score == 3):
            score = score + 10
        elif (Python_score == 2):
            score = score + 7
        elif (Python_score == 1):
            score = score + 3

        if (R_score == 3):
            score = score + 10
        elif (R_score == 2):
            score = score + 7
        elif (R_score == 1):
            score = score + 3

        if (DS_score == 3):
            score = score + 10
        elif (DS_score == 2):
            score = score + 7
        elif (DS_score == 1):
            score = score + 3

        if (str(UG).lower().find("b.tech") != -1 or str(UG).lower().find("b.e") != -1):
            if (UG_Year == 2020):

                score = score + 10
            elif (UG_Year == 2019):

                score = score + 8

            else:
                score = score + 5

        if (str(PG).lower().find("m.sc") != -1 or str(PG).lower().find("m.tech") != -1):
            if (PG_Year == 2020):
                score = score + 7
            else:
                score = score + 7

        if (str(otherskills).lower().find('machine learning') != -1):
            score = score + 3
        if (str(otherskills).lower().find('deep learning') != -1):
            score = score + 3
        if (str(otherskills).lower().find('nlp') != -1 or str(otherskills).lower().find(
                'natural language processing') != -1):
            score = score + 3
        if (str(otherskills).lower().find('aws') != -1 or str(otherskills).lower().find('amazon web services') != -1):
            score = score + 3
        if (str(otherskills).lower().find('excel') != -1):
            score = score + 3
        if (str(otherskills).lower().find('statistical data analysis') != -1):
            score = score + 3
        print(score)
        vb = np.array(score).reshape(1, -1)
        with open('model.pkl', 'rb') as f:
            dt = pickle.load(f)
        print("loading saved artifacts...done")
        value = dt.predict(vb)
        t = ' '.join(map(str, value))
        if (t == 1):
            print ("Congratulations Your are Selected")
        else:
            print ("Sorry You are Not Selected")

        return render_template('index1.html',t='If 0 You are not Selected and If 1 You are Selected : {}'.format(t))

    else:
        return render_template('index.html', t='If 0 You are not Selected and If 1 You are Selected : {}'.format(t))


if __name__ == '__main__':
    app.run(debug=True)