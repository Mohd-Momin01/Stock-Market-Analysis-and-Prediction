## 🚀 Live Application

### 🌐 Launch the Dashboard

👉 **Live Demo:**  
[https://stock-market-analysis-and-prediction-cozi96ayccrleaadtt8szv.streamlit.app/](https://stock-market-analysis-and-prediction-madwiynkvdjyr3ezctvgdr.streamlit.app/)

### 📊 Stock Analysis

👉 [https://stock-market-analysis-and-prediction-cozi96ayccrleaadtt8szv.streamlit.app/Stock_Analysis](https://stock-market-analysis-and-prediction-madwiynkvdjyr3ezctvgdr.streamlit.app/Stock_Analysis)

### 🤖 Stock Prediction

👉 [https://stock-market-analysis-and-prediction-cozi96ayccrleaadtt8szv.streamlit.app/Stock_Prediction
](https://stock-market-analysis-and-prediction-madwiynkvdjyr3ezctvgdr.streamlit.app/Stock_Prediction)
# 📈 Stock Market Analysis & Prediction Dashboard

An interactive **Data Analytics and Machine Learning** dashboard built with **Python** and **Streamlit** to analyze stock market data, visualize financial insights, and generate basic future price predictions.

This project demonstrates the complete **data analytics workflow**, including data collection, data processing, visualization, business analysis, and predictive modeling.

---

# 📌 Project Overview

The dashboard allows users to enter any supported stock ticker (e.g., **AAPL**, **MSFT**, **RELIANCE.NS**, **TCS.NS**) and instantly explore:

* Company Profile
* Financial Metrics
* Historical Stock Performance
* Risk Analysis
* Valuation Analysis
* Interactive Price Charts
* Future Price Prediction using Machine Learning

The application supports both **US** and **Indian** stock markets.

---

# 🎯 Project Objectives

The objective of this project is to demonstrate practical Data Analytics skills by:

* Collecting live stock market data
* Cleaning and transforming data
* Performing financial analysis
* Creating interactive dashboards
* Building a basic Machine Learning prediction model
* Presenting insights in a business-friendly format

---

# 🚀 Features

## 📊 Stock Analysis

* Company Overview
* Company Information
* Market Capitalization
* Employee Information
* Industry & Sector
* Financial Highlights
* Price Summary
* Risk Analysis
* Valuation Analysis
* Interactive Stock Price Chart
* Investment Summary
* Company News *(if available)*
* Investment Disclaimer

---
# Home Dashboard

![Home Dashboard](Streamlit%20UI%20Images/Home%20DashBoard.png)

# Stock Analysis
![Stock Analysis](Streamlit%20UI%20Images/Stock%20Anaylsis%20DashBoard.png)

# Stock Prediction

![Stock Prediction](Streamlit%20UI%20Images/Stock%20Prediction%20DashBoard.png)

## 🤖 Stock Prediction

* Historical Data Analysis
* Feature Engineering
* Linear Regression Model
* Future Price Prediction
* Historical vs Predicted Price Chart
* Model Performance (R² Score)
* Prediction Insights
* Investment Recommendation
* Model Limitations
* Prediction Disclaimer

---

# 🛠 Technologies Used

| Technology               | Purpose                  |
| ------------------------ | ------------------------ |
| Python                   | Programming Language     |
| Streamlit                | Dashboard Development    |
| Pandas                   | Data Cleaning & Analysis |
| NumPy                    | Numerical Computing      |
| Plotly                   | Interactive Charts       |
| Yahoo Finance (yfinance) | Live Stock Data          |
| Scikit-Learn             | Machine Learning         |

---

# 📈 Data Analytics Workflow

```
User Input
      │
      ▼
Yahoo Finance API
      │
      ▼
Data Collection
      │
      ▼
Data Cleaning (Pandas)
      │
      ▼
Business Analysis
      │
      ▼
Visualization (Plotly)
      │
      ▼
Machine Learning
      │
      ▼
Prediction Dashboard
```

---
## 📥. Data Collection

Historical stock market data is collected using the Yahoo Finance API.

```python
stock = yf.Ticker(ticker)
history = stock.history(start=start_date, end=end_date)
```
## 🏢 Company Information

Company details are fetched directly from Yahoo Finance.

```python
info = stock.info
company = info.get("longName")
industry = info.get("industry")
market_cap = info.get("marketCap")
```
## ⚙ Feature Engineering

The Date column is converted into numerical values before training the model.

```python
history["Day"] = np.arange(len(history))
```
## 🤖 Model Training

Linear Regression is used for price forecasting.

```python
model = LinearRegression()

model.fit(X, y)
```
## 📈 Future Prediction

```python
future_predictions = model.predict(future_days)
```
## 📊 Interactive Visualization

```python
fig.add_trace(
    go.Scatter(
        x=history["Date"],
        y=history["Close"]
    )
)
```
## 🛡 Risk Analysis

```python
if beta >= 1.2:
    st.error("High Risk")
elif beta >= 0.8:
    st.warning("Moderate Risk")
else:
    st.success("Low Risk")
```
## 🌍 Automatic Currency Detection

```python
if ticker.endswith(".NS"):
    currency_symbol = "₹"
else:
    currency_symbol = "$"
```
## 💡 Investment Recommendation

```python
if change_percent >= 10:
    recommendation = "BUY"
elif change_percent >= 5:
    recommendation = "ACCUMULATE"
else:
    recommendation = "HOLD"
```
## 🎨 Dashboard Layout

```python
col1, col2, col3 = st.columns(3)
```

# 📂 Project Structure

```text
Stock-Market-Analysis-and-Prediction/

│
├── Trading_app.py
│
├── pages/
│   ├── Stock_Analysis.py
│   └── Stock_Prediction.py
│
├── app.png
├── README.md
├── requirements.txt
└── .gitignore
```


# 📊 Key Analysis Performed

### Company Analysis

* Company Overview
* Industry
* Sector
* Country
* Employees
* Market Capitalization

### Financial Analysis

* Market Cap
* PE Ratio
* EPS
* Beta

### Stock Analysis

* Current Price
* Highest Price
* Lowest Price
* Average Price
* 52 Week High
* 52 Week Low

### Risk Analysis

* Low Risk
* Moderate Risk
* High Risk

### Valuation

* Undervalued
* Fairly Valued
* Expensive

### Machine Learning

* Feature Engineering
* Linear Regression
* Price Prediction
* Model Evaluation (R² Score)

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Stock-Market-Analysis-and-Prediction.git
```

Move into the project folder

```bash
cd Stock-Market-Analysis-and-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run Trading_app.py
```

---

# 📚 Skills Demonstrated

* Data Collection
* Data Cleaning
* Data Transformation
* Data Visualization
* Dashboard Development
* Business Analysis
* Financial Data Analysis
* Feature Engineering
* Machine Learning
* Predictive Analytics
* API Integration
* Python Programming

---

# 📌 Project Limitations

This project uses a simple **Linear Regression** model for educational purposes.

The prediction model does **not** consider:

* Market News
* Financial Statements
* Economic Events
* Company Earnings
* Investor Sentiment

Therefore, predicted prices should be treated as educational estimates rather than investment advice.

---

# 🔮 Future Improvements

* LSTM Forecasting
* ARIMA Model
* Facebook Prophet
* Technical Indicators (RSI, MACD)
* Candlestick Charts
* Real-Time News Integration
* Sentiment Analysis
* Portfolio Optimization
* Multiple ML Model Comparison

---

# ⚠ Disclaimer

This project has been developed for **educational and portfolio purposes only**.

The stock market data is collected using the **Yahoo Finance API (yfinance)**.

The analysis and predictions generated by this application should **not** be considered financial or investment advice.

Always perform your own research before making investment decisions.

---

# 👨‍💻 Author

**Momin Analyst**

**Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning**

If you found this project helpful, feel free to ⭐ the repository.

