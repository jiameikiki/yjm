import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
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
st.dataframe(df.head(10), width='stretch')

st.subheader("Basic Statistics")
avg_price = df["Close"].mean()
st.write(f"📊 Average Closing Price: **$ {avg_price:.2f}**")

st.subheader("Price Trend Chart")
fig = px.line(
    df, 
    x='Date', 
    y='Close',
    title=f"{ticker} Stock Price Trend (Last 180 Days)",
    labels={'Date': 'Date', 'Close': 'Price (USD)'}
)
fig.update_traces(line=dict(color='#1f77b4', width=2), fill='tozeroy', fillcolor='rgba(31,119,180,0.2)')
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    hovermode='x unified',
    template='plotly_white'
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.write("📌 Built with Streamlit for ACC102 Track 4")
st.write("📊 Data: Simulated sample data for demonstration purposes")
