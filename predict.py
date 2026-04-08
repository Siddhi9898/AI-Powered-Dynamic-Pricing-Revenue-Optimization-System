import joblib

# -----------------------------
# 📥 LOAD MODEL
# -----------------------------
model = joblib.load("model.pkl")

# -----------------------------
# 🎯 TEST INPUT
# -----------------------------
price = 500

# -----------------------------
# 🔮 PREDICTION
# -----------------------------
predicted_demand = model.predict([[price]])

# -----------------------------
# 📊 OUTPUT
# -----------------------------
print(f"Price: ₹{price}")
print(f"Predicted Demand: {int(predicted_demand[0])}")