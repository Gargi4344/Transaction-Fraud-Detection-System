import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Dummy dataset
data = pd.DataFrame({
    'amount': [200, 500, 1000, 400, 1500, 2300, 300],
    'transaction_time': [2, 4, 9, 12, 18, 23, 5],
    'location_score': [0.9, 0.8, 0.2, 0.4, 0.3, 0.1, 0.7],
    'fraud': [0, 0, 1, 0, 1, 1, 0]
})

X = data[['amount', 'transaction_time', 'location_score']]
y = data['fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"Model trained with accuracy: {acc:.2f}")

joblib.dump(model, 'models/fraud_model.pkl')
print("Model saved successfully!")
