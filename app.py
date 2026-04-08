import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 🎨 PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Smart Pricing System", layout="wide")

# -----------------------------
# 🎨 CUSTOM UI
# -----------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #E6E6E6;
    }
    .card {
        background-color: #1A1F2B;
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 📥 LOAD MODEL
# -----------------------------
model = joblib.load("model.pkl")

# -----------------------------
# 🧾 TITLE
# -----------------------------
st.title("🚀 AI-Powered Dynamic Pricing & Revenue Optimization System")
st.markdown("Optimize pricing using AI-driven demand prediction, simulation, and strategy recommendations.")

st.markdown("---")

# -----------------------------
# 🎛️ INPUT SECTION
# -----------------------------
st.header("📥 Input Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    price = st.slider("Select Price (₹)", 100, 1000, 500)

with col2:
    cost = st.number_input("Enter Cost (₹)", value=200)

with col3:
    competitor_price = st.number_input("Competitor Price (₹)", value=550)

# -----------------------------
# 🔮 PREDICTION
# -----------------------------
demand = model.predict([[price]])[0]
revenue = price * demand
profit = (price - cost) * demand

# -----------------------------
# 🔄 SIMULATION
# -----------------------------
price_range = np.linspace(100, 1000, 50)

revenues = []
profits = []

for p in price_range:
    d = model.predict([[p]])[0]
    revenues.append(p * d)
    profits.append((p - cost) * d)

# -----------------------------
# 🧠 OPTIMIZATION
# -----------------------------
best_index = np.argmax(profits)
best_price = price_range[best_index]
best_profit = profits[best_index]

# -----------------------------
# 💡 STRATEGY ENGINE
# -----------------------------
if price < competitor_price and demand > 500:
    strategy = "📈 Increase price slightly due to strong demand"
elif demand < 300:
    strategy = "📉 Offer discount to boost demand"
elif price > competitor_price:
    strategy = "⚠️ Price higher than competitor, consider reducing"
else:
    strategy = "⚖️ Maintain current pricing"

# -----------------------------
# 📊 OUTPUT CARDS
# -----------------------------
st.header("📊 Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <h4>📦 Demand</h4>
        <h2>{int(demand)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h4>💰 Revenue</h4>
        <h2>₹{int(revenue)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <h4>📈 Profit</h4>
        <h2 style="color:#00FF88;">₹{int(profit)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <h4>🎯 Best Price</h4>
        <h2 style="color:#00F5D4;">₹{int(best_price)}</h2>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# 📈 GRAPHS
# -----------------------------
st.markdown("---")
st.header("📈 Price Simulation")

fig1 = plt.figure()
plt.plot(price_range, revenues)
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.title("Price vs Revenue")
st.pyplot(fig1)

fig2 = plt.figure()
plt.plot(price_range, profits)
plt.xlabel("Price")
plt.ylabel("Profit")
plt.title("Price vs Profit")
st.pyplot(fig2)

# -----------------------------
# 💬 STRATEGY OUTPUT
# -----------------------------
st.markdown("---")
st.header("🧠 Strategy Recommendation")

st.markdown(f"""
<div class="card">
    <h3>{strategy}</h3>
</div>
""", unsafe_allow_html=True)