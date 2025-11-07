# 💳 Transaction Fraud Detection System

**Tech Stack:** Python • React • MongoDB • Scikit-learn • Power BI

## 📋 Overview
An ML-powered fraud detection system that monitors transactions in real time, detects anomalies, and visualizes insights using Power BI dashboards.

## 🚀 Features
- Machine learning model for detecting fraudulent transactions  
- REST API built with Flask for real-time monitoring  
- React frontend to simulate and test predictions  
- MongoDB for transaction storage  
- Power BI for analytical visualization  

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model
```bash
python models/train_model.py
```

### 3️⃣ Run the API
```bash
python backend/app.py
```

### 4️⃣ Start React Frontend
```bash
cd frontend
npm install
npm start
```

### 5️⃣ Test
Go to `http://localhost:3000` and try submitting a transaction.

### 6️⃣ Docker Run
```bash
docker build -t fraud-detection .
docker run -p 5000:5000 fraud-detection
```

## 📊 Power BI Integration
Use Power BI to connect to the MongoDB dataset for advanced analytics and fraud trend visualizations.

## 🧠 Future Enhancements
- Implement anomaly detection with neural networks  
- Add user authentication and alert notifications  
- Deploy via AWS EC2 or Azure Web Apps  

## 🧑‍💻 Author
**Pruthvirajsinh Rathod**  
Transaction Fraud Detection System | © 2025
