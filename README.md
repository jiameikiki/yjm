# Stock Data Analysis Tool
## Track 4: Interactive Data Analysis Tool

### Project Overview

This is a simple stock data analysis tool designed for educational purposes. 
It allows users to explore stock market data, view price trends, and understand 
basic financial metrics through an interactive web interface.

### Target Users

- Beginner investors who want to learn about stock market data
- Students studying finance and economics
- Anyone interested in understanding stock price movements

### Features

- Interactive stock price charts
- Trading volume visualization
- Moving average calculations
- Historical data tables (sortable)
- Statistical summary
- Data export functionality

### How to Use

#### Prerequisites

Make sure you have Python 3.8 or higher installed.

#### Installation

1. Open your terminal or command prompt

2. Navigate to the project folder:
   ```
   cd ACC102_Stock_Analysis
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

#### Running the Application

After installation, run the following command:

```
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

#### Using the Tool

1. Enter a US stock ticker symbol (e.g., AAPL, MSFT, TSLA)
2. Select the date range you want to analyze
3. Choose display options (volume, moving averages)
4. Explore the interactive charts and data tables
5. Download data if needed

### Project Structure

```
ACC102_Stock_Analysis/
├── app.py              # Main Streamlit application
├── analysis.py         # Data analysis functions
├── requirements.txt    # Python package dependencies
├── README.md          # This file
└── Stock_Analysis_Demo.mp4   # Demo video (submit separately)
```

### Data Source

Stock data is obtained from Yahoo Finance through the yfinance library.
Data is for educational purposes only and should not be used for actual 
investment decisions.

### Limitations

- Data is limited to US stocks
- Historical data availability varies by ticker
- Real-time data is not available (1-2 day delay)
- No predictive or forecasting capabilities

### Future Improvements

- Add more technical indicators
- Include fundamental analysis features
- Add stock comparison functionality
- Support for more international markets

### Author

Student Name: [Your Name]
Student ID: [Your ID]
Date: April 2026

### Acknowledgments

- Yahoo Finance for providing stock data
- Streamlit for the web framework
- XJTLU ACC102 Course Materials
