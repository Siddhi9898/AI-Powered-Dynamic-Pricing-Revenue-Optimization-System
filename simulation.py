import joblib
import numpy as np

model = joblib.load("model.pkl")

price_range = np.linspace(100, 1000, 50)

results = []

for price in price_range:
    demand = model.predict([[price]])[0]
    revenue = price * demand
    profit = (price - 200) * demand

    results.append((price, demand, revenue, profit))

# Check if results filled
print("Total results:", len(results))

best = max(results, key=lambda x: x[3])

print("Best Price:", int(best[0]))
print("Max Profit:", int(best[3]))