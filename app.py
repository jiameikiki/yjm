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


df = yf.download(ticker, start=start_date, end=end_date, group_by='ticker')

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)


df = df.dropna()
df = df.round(2)


st.subheader("Data Sample")
if not df.empty:
    st.dataframe(df.head(10))
else:
    st.error("No data found for the selected ticker. Please check the symbol.")


st.subheader("Basic Statistics")
if not df.empty:
    avg_price = df["Close"].mean()
    st.write(f"Average Close Price: $ {avg_price:.2f}")


st.subheader("Price Trend")
if not df.empty:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df.index, df["Close"], color="blue", linewidth=2)
    ax.set_title(f"{ticker} Close Price Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)

st.write("--------------------------------")
st.write("Data source: Yahoo Finance")
st.write("Built for ACC102 Track 4")
