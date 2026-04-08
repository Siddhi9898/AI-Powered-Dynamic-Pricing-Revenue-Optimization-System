import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# -----------------------------
# 📊 LOAD DATA
# -----------------------------
data = pd.read_csv("data.csv")

# Features (input)
X = data[["price"]]

# Target (output)
y = data["demand"]

# -----------------------------
# 🤖 TRAIN MODEL
# -----------------------------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# -----------------------------
# 💾 SAVE MODEL
# -----------------------------
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")