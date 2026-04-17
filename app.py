"""
Stock Data Analysis Dashboard
Track 4: Interactive Data Analysis Tool
ACC102 Python Data Product Assignment

This is a simple stock analysis tool that allows users to explore
stock price data and basic financial metrics.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import yfinance as yf

# Page configuration
st.set_page_config(
    page_title="Stock Analysis Tool",
    page_icon="📈",
    layout="wide"
)

# Title and introduction
st.title("📈 Stock Data Analysis Dashboard")
st.markdown("""
**Track 4: Interactive Data Analysis Tool**

This tool allows you to explore stock market data for selected companies.
Enter a stock ticker symbol and date range to view price trends and basic analysis.
""")

# Sidebar for user inputs
st.sidebar.header("⚙️ Settings")

# Stock ticker input
ticker = st.sidebar.text_input(
    "Enter Stock Ticker (e.g., AAPL, MSFT, TSLA)",
    value="AAPL",
    help="Enter a valid US stock ticker symbol"
)

# Date range selection
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

col1, col2 = st.sidebar.columns(2)
with col1:
    start_date = st.date_input("Start Date", start_date)
with col2:
    end_date = st.date_input("End Date", end_date)

# Analysis options
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Display Options")

show_volume = st.sidebar.checkbox("Show Trading Volume", value=True)
show_ma = st.sidebar.checkbox("Show Moving Averages", value=True)
ma_periods = st.sidebar.slider("MA Period (days)", 5, 50, 20)

# Main content area
try:
    # Download stock data
    with st.spinner("Loading stock data..."):
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date + timedelta(days=1))
    
    if df.empty:
        st.error(f"❌ No data found for ticker '{ticker}'. Please check the ticker symbol.")
    else:
        # Display basic information
        st.subheader(f"📋 Basic Information: {ticker.upper()}")
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Calculate basic metrics
        current_price = df['Close'].iloc[-1]
        previous_close = df['Close'].iloc[-2] if len(df) > 1 else current_price
        price_change = current_price - previous_close
        price_change_pct = (price_change / previous_close) * 100
        
        high_price = df['High'].max()
        low_price = df['Low'].min()
        avg_volume = df['Volume'].mean()
        
        with col1:
            st.metric("Current Price", f"${current_price:.2f}", 
                     f"{price_change:+.2f} ({price_change_pct:+.2f}%)")
        with col2:
            st.metric("52-Week High", f"${high_price:.2f}")
        with col3:
            st.metric("52-Week Low", f"${low_price:.2f}")
        with col4:
            st.metric("Avg Volume (Daily)", f"{avg_volume:,.0f}")
        
        st.markdown("---")
        
        # Price chart
        st.subheader("📈 Price Chart")
        
        # Create figure
        fig = go.Figure()
        
        # Candlestick chart
        fig.add_trace(go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name="Price"
        ))
        
        # Add moving average if selected
        if show_ma:
            df['MA'] = df['Close'].rolling(window=ma_periods).mean()
            fig.add_trace(go.Scatter(
                x=df.index,
                y=df['MA'],
                mode='lines',
                name=f'{ma_periods}-Day MA',
                line=dict(color='orange', width=2)
            ))
        
        fig.update_layout(
            title=f"{ticker.upper()} Stock Price",
            yaxis_title="Price (USD)",
            xaxis_title="Date",
            template="plotly_dark",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Trading volume
        if show_volume:
            st.subheader("📊 Trading Volume")
            fig_vol = px.bar(
                df,
                x=df.index,
                y='Volume',
                title="Daily Trading Volume",
                color_discrete_sequence=['#1f77b4']
            )
            fig_vol.update_layout(
                height=300,
                showlegend=False,
                template="plotly_dark"
            )
            st.plotly_chart(fig_vol, use_container_width=True)
        
        # Data table
        st.subheader("📋 Historical Data")
        st.markdown("*Click on column headers to sort, or use filters below*")
        
        # Format dataframe for display
        display_df = df.reset_index()
        display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
        display_df = display_df.round(2)
        
        # Interactive data table with sorting
        st.dataframe(
            display_df,
            use_container_width=True,
            height=400
        )
        
        # Download data button
        st.markdown("---")
        csv = df.to_csv()
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv,
            file_name=f"{ticker}_stock_data.csv",
            mime="text/csv"
        )
        
        # Statistical summary
        st.subheader("📊 Statistical Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Daily Returns**")
            returns = df['Close'].pct_change().dropna()
            returns_df = pd.DataFrame({
                'Mean Return': [returns.mean()],
                'Std Deviation': [returns.std()],
                'Min Return': [returns.min()],
                'Max Return': [returns.max()]
            }).T
            returns_df.columns = ['Value']
            returns_df['Value'] = returns_df['Value'].apply(lambda x: f"{x:.4f}" if abs(x) < 1 else f"{x:.2f}")
            st.dataframe(returns_df, use_container_width=True)
        
        with col2:
            st.markdown("**Price Statistics**")
            price_stats = pd.DataFrame({
                'Mean Price': [df['Close'].mean()],
                'Median Price': [df['Close'].median()],
                'Total Trading Days': [len(df)]
            }).T
            price_stats.columns = ['Value']
            price_stats['Value'] = price_stats['Value'].apply(lambda x: f"${x:.2f}" if 'Price' in price_stats.index else str(int(x)))
            st.dataframe(price_stats, use_container_width=True)

except Exception as e:
    st.error(f"❌ An error occurred: {str(e)}")
    st.info("💡 Please check that the stock ticker is valid and try again.")

# Footer
st.markdown("---")
st.markdown("""
**How to Use This Tool:**
1. Enter a valid US stock ticker symbol (e.g., AAPL, MSFT, GOOGL)
2. Select your desired date range
3. Explore the interactive charts and data tables
4. Download the data for further analysis

*Data provided by Yahoo Finance. Data is for educational purposes only.*
""")
