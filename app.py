import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests


st.title("Basic Stock Analysis Tool")
st.write("This is a simple data analysis tool for ACC102 assignment.")


ticker = st.text_input("Enter stock ticker (e.g. AAPL, MSFT)", "AAPL")


end_date = datetime.now()
start_date = end_date - timedelta(days=180)

API_KEY = "demo"
try:
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}&outputsize=full"
    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        st.error("❌ No data found for the selected ticker. Please check the symbol.")
        st.stop()

    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df = df.astype(float)
    df = df.reset_index().rename(columns={"index": "Date"})

    df["Date"] = pd.to_datetime(df["Date"])
    df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
    df = df.set_index("Date").sort_index()

except Exception as e:
    st.error(f"Failed to fetch data: {e}")
    st.stop()

df = df.dropna()
df = df.round(2)


st.subheader("Data Sample")
st.dataframe(df.head(10))

st.subheader("Basic Statistics")
avg_price = df["4. close"].mean()
st.write(f"Average Close Price: $ {avg_price:.2f}")

st.subheader("Price Trend")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df.index, df["4. close"], color="#0066cc", linewidth=2)
ax.set_title(f"{ticker} Close Price Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.grid(True, alpha=0.3)
plt.xticks(rotation=45)
st.pyplot(fig)


st.write("---")
st.write("Data source: Alpha Vantage (Free Tier)")
st.write("Built for ACC102 Track 4")
