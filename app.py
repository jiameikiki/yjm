import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

st.set_page_config(
    page_title="Stock Analysis Tool",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Data Analysis Dashboard")
st.markdown("### Track 4: Interactive Data Analysis Tool")
st.write("This tool allows you to explore stock market data with real-time quotes from Yahoo Finance.")

st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter stock ticker (e.g. AAPL, MSFT, TSLA)", "AAPL")

st.sidebar.subheader("Date Range")
days_options = {
    "1 Month": 30,
    "3 Months": 90,
    "6 Months": 180,
    "1 Year": 365,
}
selected_range = st.sidebar.selectbox("Select time period", list(days_options.keys()))
days = days_options[selected_range]

end_date = datetime.now()
start_date = end_date - timedelta(days=days)

@st.cache_data(ttl=3600)
def load_data(ticker_symbol, start, end):
    try:
        stock = yf.Ticker(ticker_symbol.upper())
        df = stock.history(start=start, end=end)
        return df, None
    except Exception as e:
        return None, str(e)

with st.spinner(f"Loading {ticker.upper()} data..."):
    df, error = load_data(ticker, start_date, end_date)

if error:
    st.error(f"⚠️ Failed to load data: {error}")
    st.info("Please check the ticker symbol and try again.")
elif df is None or df.empty:
    st.warning(f"⚠️ No data found for '{ticker.upper()}'. Please try another ticker.")
else:
    st.subheader("Data Sample")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Basic Statistics")
    avg_price = df["Close"].mean()
    max_price = df["High"].max()
    min_price = df["Low"].min()
    total_volume = df["Volume"].sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Average Close Price", f"$ {avg_price:.2f}")
    col2.metric("Highest Price", f"$ {max_price:.2f}")
    col3.metric("Lowest Price", f"$ {min_price:.2f}")
    col4.metric("Total Volume", f"{total_volume:,.0f}")

    st.subheader("Price Trend Chart (Candlestick)")
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='OHLC'
    ))

    fig.update_layout(
        title=f"{ticker.upper()} Stock Price Trend",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=False,
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Trading Volume")
    fig_vol = go.Figure()
    fig_vol.add_trace(go.Bar(
        x=df.index,
        y=df['Volume'],
        name='Volume',
        marker_color='rgba(58, 142, 255, 0.6)'
    ))
    fig_vol.update_layout(
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
        height=250
    )
    st.plotly_chart(fig_vol, use_container_width=True)


    st.subheader("Download Data")
    csv = df.to_csv(index=True)
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name=f"{ticker.upper()}_stock_data.csv",
        mime="text/csv"
    )

st.markdown("---")
st.write("📌 Built with Streamlit for ACC102 Track 4")
st.write("📊 Data sourced from Yahoo Finance")




