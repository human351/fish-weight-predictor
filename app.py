from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('fish_weight_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        features = [float(data['length1']), float(data['length2']), float(data['length3']), float(data['height']), float(data['width'])]
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter numeric values only.'}), 400
    
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
