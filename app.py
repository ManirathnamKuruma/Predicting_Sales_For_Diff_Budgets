from flask import Flask, render_template, request
import jsonify
import requests
import sklearn
import pickle
app = Flask(__name__)
model = pickle.load(open('lr_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        tv_ad = float(request.form['tv'])
        radio_ad= float(request.form['radio'])
        newspaper_ad= float(request.form['newspaper'])
        prediction=model.predict([[tv_ad,radio_ad,newspaper_ad]])
        output=prediction[0]
        return render_template('index.html',prediction_text='Sales Outcome in Dollars: {}'.format(output))

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

