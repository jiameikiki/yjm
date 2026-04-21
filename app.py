import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Stock Analysis Tool",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Data Analysis Dashboard")
st.markdown("### Track 4: Interactive Data Analysis Tool")
st.write("This tool allows you to explore stock market data with sample data for ACC102 assignment.")

st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter stock ticker (e.g. AAPL, MSFT)", "AAPL")

end_date = datetime.now()
start_date = end_date - timedelta(days=180)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

base_price = 150
prices = []
current_price = base_price
for _ in range(len(dates)):
    change = np.random.normal(0, 0.5)
    current_price += change
    prices.append(max(current_price, 10))

df = pd.DataFrame({
    'Date': dates,
    'Open': np.array(prices) * 1.01,
    'High': np.array(prices) * 1.03,
    'Low': np.array(prices) * 0.99,
    'Close': np.array(prices),
    'Adj Close': np.array(prices),
    'Volume': np.random.randint(1000000, 5000000, size=len(dates))
})
df = df.round(2)

st.subheader("Data Sample")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Basic Statistics")
avg_price = df["Close"].mean()
st.write(f"📊 Average Closing Price: **$ {avg_price:.2f}**")

st.subheader("Price Trend Chart")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Date'], df['Close'], color='#1f77b4', linewidth=2, label='Close Price')
ax.fill_between(df['Date'], df['Close'], alpha=0.2, color='#1f77b4')
ax.set_title(f"{ticker} Stock Price Trend (Last 180 Days)")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.grid(True, alpha=0.3)
plt.xticks(rotation=45)
ax.legend()
st.pyplot(fig)

st.markdown("---")
st.write("📌 Built with Streamlit for ACC102 Track 4")
st.write("📊 Data: Simulated sample data for demonstration purposes")
