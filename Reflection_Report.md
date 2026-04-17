# Reflection Report
## ACC102 Python Data Product Assignment

**Student Name:** [Your Name]
**Student ID:** [Your ID]
**Date:** April 2026

---

## 1. Analytical Problem and Target Audience

The analytical problem I aimed to address is the difficulty that beginner investors and students face when trying to understand and interpret raw stock market data. Many financial data platforms present overwhelming amounts of information without proper context or visualization, making it challenging for newcomers to extract meaningful insights.

My target audience consists of:
- Economics and finance students learning about stock markets
- Beginner investors who want to understand basic stock analysis
- Anyone interested in learning how to work with financial data using Python

---

## 2. Dataset Description and Selection Rationale

**Dataset:** Stock price data from Yahoo Finance

**Data Source:** Yahoo Finance (via yfinance Python library)

**Date Accessed:** April 2026

**Selection Rationale:**
I chose this dataset because:
1. Stock data is highly relevant to my Economics and Finance program
2. Yahoo Finance provides reliable, free access to historical stock data
3. The data structure (OHLCV format) is ideal for learning data analysis techniques
4. Stock analysis is a practical application that combines financial knowledge with technical skills

The dataset includes:
- Date
- Open, High, Low, Close prices
- Volume (trading activity)

---

## 3. Python Methods Used

Throughout this project, I used several Python libraries and techniques:

### Data Collection
- **yfinance**: To download historical stock data from Yahoo Finance
- Handling date ranges and data retrieval

### Data Processing
- **pandas**: For data manipulation and analysis
- Handling missing values
- Calculating returns and moving averages
- DataFrame operations

### Data Visualization
- **matplotlib** and **plotly**: For creating charts and graphs
- Line charts for price trends
- Candlestick charts for price patterns
- Bar charts for volume analysis

### Interactive Interface
- **Streamlit**: To create an interactive web application
- User input widgets
- Real-time data updates
- Interactive charts

---

## 4. Main Insights and Outputs

Through this analysis, I developed an interactive stock analysis tool that provides:

1. **Price Visualization**: Interactive charts showing stock price movements over time

2. **Technical Indicators**: Moving averages that help identify trends (20-day and 50-day MA)

3. **Statistical Summary**: Daily returns, volatility, and other key metrics

4. **Trading Volume Analysis**: Understanding market activity through volume charts

5. **Data Export**: Ability to download data for further analysis

Key learning points:
- How to collect and process financial data
- Understanding stock price patterns
- Basic technical analysis concepts
- Building interactive data tools with Python

---

## 5. Limitations, Reliability Issues, and Improvements

### Limitations:
1. **Data Source**: Yahoo Finance data has a 1-2 day delay for non-premium users
2. **Scope**: Analysis is limited to US stocks only
3. **No Real-Time Data**: Cannot perform real-time trading analysis
4. **Technical Analysis Only**: No fundamental analysis included

### Reliability Issues:
1. Stock data accuracy depends on the data provider
2. Moving averages are lagging indicators (historical data only)
3. Past performance does not guarantee future results

### Possible Improvements:
1. Add more technical indicators (RSI, MACD, Bollinger Bands)
2. Include fundamental analysis features
3. Add stock comparison functionality
4. Support for international markets
5. Add predictive modeling using machine learning

---

## 6. Personal Contribution and Learning

### What I Did:
1. **Problem Definition**: Identified the need for accessible stock analysis tools for beginners
2. **Data Collection**: Set up data retrieval from Yahoo Finance
3. **Analysis Development**: Created Python scripts for data analysis
4. **Visualization**: Built interactive charts and dashboards
5. **Testing**: Verified the tool works correctly with various stock tickers

### What I Learned:
1. **Python Skills**: Improved my understanding of pandas, matplotlib, and Streamlit
2. **Financial Knowledge**: Applied theoretical knowledge from my program to real data
3. **Data Analysis Process**: Learned the workflow from data collection to insight generation
4. **Problem Solving**: Debugged issues with data retrieval and visualization
5. **Technical Communication**: Learned to explain technical concepts clearly

### Challenges Faced:
1. Understanding the OHLCV data structure
2. Debugging Streamlit application issues
3. Ensuring charts display correctly with different date ranges
4. Managing API rate limits from Yahoo Finance

### How I Overcame:
1. Researched documentation for each library
2. Tested with multiple stock examples
3. Used print statements for debugging
4. Asked for help when needed

---

## 7. AI Use Disclosure

In completing this assignment, I used AI tools as follows:

**AI Tool Used:** [Specify if applicable, e.g., ChatGPT]
**Version:** [Version if available]
**Access Date:** [Date]
**Purpose:** [What the AI was used for - e.g., debugging, syntax help, explaining concepts]

**Note:** All code was written and understood by me. AI was used only for troubleshooting and clarification of concepts. The final submission represents my own work and understanding of the material.

---

## Conclusion

This project helped me understand how Python can be applied to solve real-world financial analysis problems. I learned that effective data analysis requires not just technical skills, but also domain knowledge and attention to user needs. The experience has strengthened my interest in combining finance and technology, and I plan to continue developing my skills in this area.

---

*Word Count: Approximately 750 words*
