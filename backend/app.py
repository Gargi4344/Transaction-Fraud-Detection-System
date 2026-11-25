from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/fraud_detection"
mongo = PyMongo(app)

// loading the model
model = joblib.load("models/fraud_model.pkl")

@app.route("/")
def index():
    return jsonify({"message": "Fraud Detection API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[data['amount'], data['transaction_time'], data['location_score']]])
    prediction = model.predict(features)[0]

    record = {"amount": data['amount'], "transaction_time": data['transaction_time'],
              "location_score": data['location_score'], "fraud": bool(prediction)}
    mongo.db.transactions.insert_one(record)

    return jsonify({"fraud_prediction": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
