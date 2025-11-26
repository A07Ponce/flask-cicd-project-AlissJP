from app import app
from flask import jsonify
from app.models import get_prediction

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la aplicación Flask con IA!"})

@app.route('/predict')
def predict():
    result = get_prediction()
    return jsonify({"predicción": result})
