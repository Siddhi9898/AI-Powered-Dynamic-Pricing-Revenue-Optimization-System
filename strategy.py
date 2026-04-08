import joblib

# -----------------------------
# 📥 LOAD MODEL
# -----------------------------
model = joblib.load("model.pkl")

# -----------------------------
# 🎯 INPUT VALUES
# -----------------------------
price = 500
cost = 200
competitor_price = 550

# -----------------------------
# 🔮 PREDICT DEMAND
# -----------------------------
demand = model.predict([[price]])[0]

# -----------------------------
# 💰 CALCULATE METRICS
# -----------------------------
revenue = price * demand
profit = (price - cost) * demand

# -----------------------------
# 🧠 STRATEGY LOGIC
# -----------------------------
if price < competitor_price and demand > 500:
    strategy = "Increase price slightly (high demand)"
elif demand < 300:
    strategy = "Offer discount (low demand)"
elif price > competitor_price:
    strategy = "Consider lowering price (competition high)"
else:
    strategy = "Maintain current pricing"

# -----------------------------
# 📊 OUTPUT
# -----------------------------
print("Price:", price)
print("Demand:", int(demand))
print("Revenue:", int(revenue))
print("Profit:", int(profit))
print("Strategy:", strategy)