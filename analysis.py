"""
Stock Data Analysis Script
ACC102 Python Data Product Assignment

This script performs analysis on stock data to generate insights
for investment decisions and market trends.
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

def get_stock_data(ticker, start_date, end_date):
    """
    Download stock data from Yahoo Finance.
    
    Parameters:
    -----------
    ticker : str
        Stock ticker symbol
    start_date : str
        Start date in YYYY-MM-DD format
    end_date : str
        End date in YYYY-MM-DD format
        
    Returns:
    --------
    pandas.DataFrame
        Stock data with OHLCV columns
    """
    print(f"Downloading data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def calculate_returns(df):
    """
    Calculate daily and cumulative returns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Stock data with Close prices
        
    Returns:
    --------
    pandas.DataFrame
        Data with return columns added
    """
    df = df.copy()
    # Daily returns
    df['Daily_Return'] = df['Close'].pct_change()
    # Cumulative returns
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1
    return df

def calculate_moving_averages(df, periods=[5, 10, 20, 50]):
    """
    Calculate simple moving averages.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Stock data with Close prices
    periods : list
        List of periods for moving averages
        
    Returns:
    --------
    pandas.DataFrame
        Data with MA columns added
    """
    df = df.copy()
    for period in periods:
        df[f'MA_{period}'] = df['Close'].rolling(window=period).mean()
    return df

def calculate_volatility(df, window=20):
    """
    Calculate rolling volatility.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Stock data with Close prices
    window : int
        Window for volatility calculation
        
    Returns:
    --------
    pandas.DataFrame
        Data with volatility column added
    """
    df = df.copy()
    df['Volatility'] = df['Close'].pct_change().rolling(window=window).std()
    return df

def generate_summary_statistics(df):
    """
    Generate summary statistics for the stock.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Stock data with Close prices
        
    Returns:
    --------
    dict
        Dictionary of summary statistics
    """
    returns = df['Close'].pct_change().dropna()
    
    summary = {
        'Total Trading Days': len(df),
        'Start Date': df.index[0].strftime('%Y-%m-%d'),
        'End Date': df.index[-1].strftime('%Y-%m-%d'),
        'Starting Price': df['Close'].iloc[0],
        'Ending Price': df['Close'].iloc[-1],
        'Total Return (%)': ((df['Close'].iloc[-1] / df['Close'].iloc[0]) - 1) * 100,
        'Average Daily Return (%)': returns.mean() * 100,
        'Daily Return Std Dev (%)': returns.std() * 100,
        'Maximum Gain (%)': returns.max() * 100,
        'Maximum Loss (%)': returns.min() * 100,
        'Highest Price': df['High'].max(),
        'Lowest Price': df['Low'].min(),
        'Average Volume': df['Volume'].mean()
    }
    
    return summary

def analyze_stock(ticker='AAPL', days=365):
    """
    Main function to analyze a stock.
    
    Parameters:
    -----------
    ticker : str
        Stock ticker symbol
    days : int
        Number of days to analyze
        
    Returns:
    --------
    dict
        Analysis results
    """
    print(f"\n{'='*50}")
    print(f"Stock Analysis Report: {ticker}")
    print(f"{'='*50}\n")
    
    # Set date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Get data
    df = get_stock_data(ticker, start_date, end_date)
    
    if df.empty:
        print(f"Error: No data found for {ticker}")
        return None
    
    print(f"Data loaded: {len(df)} trading days")
    
    # Calculate metrics
    df = calculate_returns(df)
    df = calculate_moving_averages(df)
    df = calculate_volatility(df)
    
    # Generate summary
    summary = generate_summary_statistics(df)
    
    # Print summary
    print("\n--- Summary Statistics ---\n")
    for key, value in summary.items():
        if isinstance(value, float):
            if 'Price' in key or 'Return' in key or 'Gain' in key or 'Loss' in key:
                print(f"{key}: {value:.2f}")
            else:
                print(f"{key}: {value:,.2f}")
        else:
            print(f"{key}: {value}")
    
    print("\n--- Price Trend ---\n")
    if summary['Total Return (%)'] > 0:
        print(f"The stock showed a POSITIVE return of {summary['Total Return (%)']:.2f}%")
    else:
        print(f"The stock showed a NEGATIVE return of {summary['Total Return (%)']:.2f}%")
    
    print("\n--- Volatility Analysis ---\n")
    avg_volatility = df['Volatility'].mean() * 100
    if avg_volatility < 1:
        risk_level = "Low"
    elif avg_volatility < 2:
        risk_level = "Medium"
    else:
        risk_level = "High"
    print(f"Average daily volatility: {avg_volatility:.2f}%")
    print(f"Risk level: {risk_level}")
    
    return {
        'data': df,
        'summary': summary,
        'ticker': ticker
    }

def compare_stocks(tickers, days=365):
    """
    Compare multiple stocks.
    
    Parameters:
    -----------
    tickers : list
        List of ticker symbols
    days : int
        Number of days to analyze
        
    Returns:
    --------
    pandas.DataFrame
        Comparison summary
    """
    print(f"\n{'='*50}")
    print("Stock Comparison Report")
    print(f"{'='*50}\n")
    
    results = []
    
    for ticker in tickers:
        print(f"\nAnalyzing {ticker}...")
        try:
            result = analyze_stock(ticker, days)
            if result:
                results.append(result['summary'])
        except Exception as e:
            print(f"Error analyzing {ticker}: {e}")
    
    # Create comparison dataframe
    comparison_df = pd.DataFrame(results)
    comparison_df = comparison_df.set_index('End Date')
    
    print("\n--- Comparison Summary ---\n")
    print(comparison_df[['Total Trading Days', 'Total Return (%)', 'Average Daily Return (%)', 'Daily Return Std Dev (%)']])
    
    return comparison_df

# Main execution
if __name__ == "__main__":
    # Example: Analyze a single stock
    print("Running stock analysis...")
    
    # Analyze Apple stock
    result = analyze_stock('AAPL', days=365)
    
    if result:
        # Save results to CSV
        result['data'].to_csv('stock_analysis_results.csv')
        print("\n✓ Analysis complete! Results saved to 'stock_analysis_results.csv'")
    
    # Example: Compare multiple stocks
    # Uncomment to compare multiple stocks
    # comparison = compare_stocks(['AAPL', 'MSFT', 'GOOGL'], days=365)
    # comparison.to_csv('stock_comparison.csv')
