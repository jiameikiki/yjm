[README(1).md](https://github.com/user-attachments/files/26928406/README.1.md)
# Stock Data Analysis Dashboard

## Project Overview

This project is a **Streamlit-based interactive web application** called **Stock Data Analysis Dashboard**, developed for **ACC102 Track 4**.  

It provides a simple, visual way to explore stock market data — including price trends, key statistics, and interactive charts — making it easy for business students and beginner investors to understand financial data without writing any code themselves.

This project is intended for educational and descriptive analysis only. It does not provide investment advice or predict future stock prices.

---

## Objective

The main objective of this project is to use Python and Streamlit to:

- build an interactive, web-based data analysis tool
- generate simulated stock market data for demonstration purposes
- calculate and display key financial statistics
- visualise stock price trends with clear, professional charts
- offer a user-friendly interface that requires no coding knowledge

---

## Target Users

The target users of this project are:

- business and finance students (ACC102 Track 4)
- beginner investors
- users interested in learning how Python and Streamlit can be used for financial data analysis

---

## Data Source

The data used in this project is **simulated sample stock data** generated programmatically.

Why simulated data?

- Stock price data accessed through APIs (e.g., Yahoo Finance) requires internet access and API keys
- Simulated data ensures the app runs reliably in any environment without external dependencies
- The simulation mimics realistic price movements using random walks with normal distribution

Dataset details:

- Period: Last 180 days of trading data
- Variables included:
  - Date
  - Open price
  - High price
  - Low price
  - Close price
  - Adjusted Close price
  - Trading Volume

---

## Key Features

### 1. Interactive Ticker Input

Users can enter any stock ticker symbol (e.g. AAPL, MSFT, GOOGL) in the sidebar. The dashboard will display the chart and statistics for the selected stock.

### 2. Data Sample Display

The app displays the most recent 10 rows of the stock data in a clean, scrollable table using Streamlit's built-in data viewer.

### 3. Basic Statistics

Key summary statistics are calculated and displayed, including:

- **Average Closing Price** — the mean closing price over the 180-day period

### 4. Price Trend Chart

A professional line chart is rendered showing:

- the closing price trend over the last 180 days
- a shaded area under the curve for better visual readability
- automatically updated labels and title based on the selected ticker

### 5. Clean, Wide Layout

The dashboard uses Streamlit's wide layout for a clean, full-screen presentation that is easy to read and navigate.

---

## Technologies Used

This project uses the following tools and Python libraries:

- **Python** — core programming language
- **Streamlit** — framework for building the interactive web app
- **pandas** — data manipulation and analysis
- **numpy** — numerical computation and random data generation
- **matplotlib** — data visualisation

---

## Repository Structure

```text
yjm/
│
├── app.py              # Main Streamlit application
├── README.ipynb        # Project documentation
└── requirements.txt    # Python dependencies
```

---

## How to Run

1. Install dependencies:
   ```bash
   pip install streamlit pandas numpy matplotlib
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Open the local URL shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## Project Notes

- **Data disclaimer**: All stock data shown is simulated for educational purposes only.
- **ACC102 Track 4**: This project was developed as part of the ACC102 course assessment.
- **Default ticker**: AAPL (Apple Inc.) is used as the default stock for demonstration.



```python

```
