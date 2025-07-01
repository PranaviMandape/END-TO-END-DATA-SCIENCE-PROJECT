from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

labels = ["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function", "Age"]

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('form.html', labels=labels, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.getlist('values')]
    scaled_data = scaler.transform([input_data])
    prediction = model.predict(scaled_data)
    result = 'Diabetic (1)' if prediction[0] == 1 else 'Not Diabetic (0)'
    return render_template('form.html', labels=labels, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)