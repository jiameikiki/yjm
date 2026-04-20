import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf

st.title("Basic Stock Analysis Tool")
st.write("This is a simple data analysis tool for ACC102 assignment.")

ticker = st.text_input("Enter stock ticker (e.g. AAPL, MSFT)", "AAPL")

end_date = datetime.now()
start_date = end_date - timedelta(days=180)
df = yf.download(ticker, start_date, end_date)

df = df.dropna()
df = df.round(2)


st.subheader("Data Sample")
st.dataframe(df.head())


st.subheader("Basic Statistics")
avg_price = df["Close"].mean()
st.write("Average Close Price: $", round(avg_price, 2))


st.subheader("Price Trend")
fig, ax = plt.subplots()
ax.plot(df["Close"], color="blue")
ax.set_title(f"{ticker} Close Price Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
st.pyplot(fig)

st.write("Built for ACC102 Track 4")
