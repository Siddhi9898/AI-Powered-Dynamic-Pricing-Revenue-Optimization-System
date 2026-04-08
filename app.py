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
# 📥 LOAD MODEL (SAFE LOAD)
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")  # make sure filename matches repo

model = load_model()

# -----------------------------
# 🧾 TITLE
# -----------------------------
st.title("🚀 AI-Powered Dynamic Pricing & Revenue Optimization System")
st.success("✅ Live AI Pricing Engine Running")
st.caption("Built with Machine Learning for real-time pricing optimization")

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
# Adjust input shape depending on your model training
try:
    demand = model.predict([[price]])[0]
except:
    demand = model.predict([[price, competitor_price]])[0]

revenue = price * demand
profit = (price - cost) * demand

# -----------------------------
# 🔄 SIMULATION (OPTIMIZED)
# -----------------------------
price_range = np.linspace(100, 1000, 50)

try:
    predictions = model.predict(price_range.reshape(-1, 1))
except:
    predictions = model.predict(np.column_stack((price_range, [competitor_price]*50)))

revenues = price_range * predictions
profits = (price_range - cost) * predictions

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

# Revenue graph
fig1, ax1 = plt.subplots()
ax1.plot(price_range, revenues)
ax1.axvline(best_price, linestyle='--')
ax1.set_xlabel("Price")
ax1.set_ylabel("Revenue")
ax1.set_title("Price vs Revenue")
st.pyplot(fig1)

# Profit graph
fig2, ax2 = plt.subplots()
ax2.plot(price_range, profits)
ax2.axvline(best_price, linestyle='--')
ax2.set_xlabel("Price")
ax2.set_ylabel("Profit")
ax2.set_title("Price vs Profit")
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