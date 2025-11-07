import React, { useState } from 'react';

function App() {
  const [form, setForm] = useState({ amount: '', transaction_time: '', location_score: '' });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    });
    const data = await response.json();
    setResult(data.fraud_prediction);
  };

  return (
    <div style={{ padding: '40px', fontFamily: 'Arial' }}>
      <h2>Transaction Fraud Detection</h2>
      <form onSubmit={handleSubmit}>
        <label>Amount: </label>
        <input name="amount" value={form.amount} onChange={handleChange} /><br /><br />
        <label>Transaction Time (hour): </label>
        <input name="transaction_time" value={form.transaction_time} onChange={handleChange} /><br /><br />
        <label>Location Score: </label>
        <input name="location_score" value={form.location_score} onChange={handleChange} /><br /><br />
        <button type="submit">Check Fraud</button>
      </form>
      {result !== null && (
        <h3 style={{ marginTop: '20px' }}>Prediction: {result ? '🚨 Fraud Detected' : '✅ Safe Transaction'}</h3>
      )}
    </div>
  );
}

export default App;
