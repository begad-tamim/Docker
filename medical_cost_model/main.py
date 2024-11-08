from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from flask_sqlalchemy import SQLAlchemy

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/flask_db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Welcome to the Insurance Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)