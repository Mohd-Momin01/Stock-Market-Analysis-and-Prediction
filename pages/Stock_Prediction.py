import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import datetime

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Stock Prediction",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Price Prediction")

st.write("""
Predict future stock prices using a simple Linear Regression model.

This prediction is based on historical closing prices and is intended
for educational and portfolio purposes only.
""")

st.divider()

# ----------------------------------------------------
# USER INPUT
# ----------------------------------------------------

today = datetime.date.today()

col1, col2, col3 = st.columns(3)

with col1:

    ticker = st.text_input(
        "Enter Stock Symbol",
        "AAPL"
    ).upper()

with col2:

    start_date = st.date_input(

        "Training Start Date",

        datetime.date(
            today.year-5,
            today.month,
            today.day
        )

    )

with col3:

    prediction_days = st.slider(

        "Days to Predict",

        5,

        60,

        30

    )

# ----------------------------------------------------
# DOWNLOAD DATA
# ----------------------------------------------------

stock = yf.Ticker(ticker)

history = stock.history(
    start=start_date,
    end=today
)

if history.empty:

    st.error("No stock data found.")

    st.stop()

history.reset_index(inplace=True)

history = history[["Date", "Close"]]

st.success("Historical stock data loaded successfully.")

st.subheader("Historical Closing Prices")

st.dataframe(history.tail(10), use_container_width=True)

st.divider()

# ----------------------------------------------------
# FEATURE ENGINEERING
# ----------------------------------------------------

st.subheader("⚙️ Feature Engineering")

# Create Day Index
history["Day"] = np.arange(len(history))

st.write("The model uses the day number as the input feature and Closing Price as the target variable.")

st.dataframe(history.tail(), use_container_width=True)

# ----------------------------------------------------
# INPUT & TARGET
# ----------------------------------------------------

X = history[["Day"]]

y = history["Close"]

# ----------------------------------------------------
# TRAIN MODEL
# ----------------------------------------------------

# Remove missing values
# Remove missing values
history = history.dropna()

# Check if enough data is available
if len(history) < 30:
    st.error("Not enough historical data available for prediction.")
    st.stop()

X = history[["Day"]]
y = history["Close"]

# Check for NaN values
if X.isnull().values.any() or y.isnull().values.any():
    st.error("Missing values found in stock data.")
    st.stop()
    
history = history.dropna()

# Check if enough data is available
if len(history) < 30:
    st.error("Not enough historical data available for prediction.")
    st.stop()

X = history[["Day"]]
y = history["Close"]

# Check for NaN values
if X.isnull().values.any() or y.isnull().values.any():
    st.error("Missing values found in stock data.")
    st.stop()

model = LinearRegression()

model.fit(X, y)

st.success("✅ Linear Regression Model Trained Successfully")

# ----------------------------------------------------
# MODEL ACCURACY
# ----------------------------------------------------

predictions = model.predict(X)

score = r2_score(y, predictions)

st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "R² Score",
        f"{score:.4f}"
    )

with col2:

    st.metric(
        "Training Samples",
        len(history)
    )

st.info("""
R² Score measures how well the Linear Regression model fits the historical data.

• Closer to **1.0** → Better Fit

• Closer to **0.0** → Poor Fit

Since this project uses a simple Linear Regression model,
the score is intended only for educational demonstration.
""")

st.divider()

# ----------------------------------------------------
# FUTURE PREDICTION
# ----------------------------------------------------

st.subheader("🔮 Future Stock Price Prediction")

future_days = np.arange(
    len(history),
    len(history) + prediction_days
).reshape(-1,1)

future_predictions = model.predict(future_days)

future_dates = pd.date_range(

    start=history["Date"].iloc[-1] + pd.Timedelta(days=1),

    periods=prediction_days,

    freq="B"

)

prediction_df = pd.DataFrame({

    "Date": future_dates,

    "Predicted Closing Price": future_predictions

})

st.success("Future stock prices predicted successfully.")

st.dataframe(
    prediction_df,
    use_container_width=True
)

st.divider()

# =====================================================
# PART 3A
# Prediction Visualization & Insights
# =====================================================

# -----------------------------
# Currency Detection
# -----------------------------

if ticker.endswith(".NS") or ticker.endswith(".BO"):
    currency_symbol = "₹"
else:
    currency_symbol = "$"

# -----------------------------
# Historical vs Predicted Chart
# -----------------------------

st.subheader("📈 Historical vs Predicted Price")

fig = go.Figure()

# Historical Price
fig.add_trace(

    go.Scatter(

        x=history["Date"],

        y=history["Close"],

        mode="lines",

        name="Historical Price",

        line=dict(

            color="royalblue",

            width=3

        )

    )

)

# Predicted Price
fig.add_trace(

    go.Scatter(

        x=future_dates,

        y=future_predictions,

        mode="lines",

        name="Predicted Price",

        line=dict(

            color="red",

            width=3,

            dash="dash"

        )

    )

)

fig.update_layout(

    template="plotly_dark",

    height=550,

    xaxis_title="Date",

    yaxis_title="Price",

    hovermode="x unified",

    legend_title="Stock Data"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -----------------------------
# Prediction Insights
# -----------------------------

st.subheader("📋 Prediction Insights")

last_price = history["Close"].iloc[-1]

predicted_price = future_predictions[-1]

change = predicted_price - last_price

change_percent = (change / last_price) * 100

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "Current Price",

        f"{currency_symbol}{last_price:,.2f}"

    )

with col2:

    st.metric(

        f"Predicted Price ({prediction_days} Days)",

        f"{currency_symbol}{predicted_price:,.2f}"

    )

with col3:

    st.metric(

        "Expected Return",

        f"{change_percent:.2f}%"

    )

st.divider()

# =====================================================
# PART 3B
# Model Interpretation & Investment Summary
# =====================================================

st.subheader("🧠 Model Interpretation")

if change_percent >= 10:

    st.success("""
### 📈 Strong Bullish Trend

The model predicts a strong upward movement based on historical price trends.

This indicates positive momentum if current market conditions continue.
""")

elif change_percent >= 5:

    st.success("""
### 📈 Moderate Bullish Trend

The model predicts a moderate upward trend.

The stock may continue moving higher over the selected prediction period.
""")

elif change_percent > -5:

    st.warning("""
### ➖ Sideways Trend

The predicted movement is relatively small.

The stock is expected to trade within a narrow price range.
""")

elif change_percent > -10:

    st.error("""
### 📉 Moderate Bearish Trend

The model predicts a moderate downward trend.

Investors should monitor price action before taking decisions.
""")

else:

    st.error("""
### 📉 Strong Bearish Trend

The model predicts a strong downward movement.

Additional analysis is recommended before investing.
""")

st.divider()

# =====================================================
# Investment Summary
# =====================================================

st.subheader("📊 Investment Summary")

# Recommendation

if change_percent >= 10:

    recommendation = "🟢 BUY"

elif change_percent >= 5:

    recommendation = "🟢 ACCUMULATE"

elif change_percent > -5:

    recommendation = "🟡 HOLD"

elif change_percent > -10:

    recommendation = "🟠 REDUCE"

else:

    recommendation = "🔴 AVOID"

summary = pd.DataFrame({

    "Metric":[

        "Current Price",

        "Predicted Price",

        "Expected Return",

        "Model Accuracy (R²)",

        "Recommendation"

    ],

    "Value":[

        f"{currency_symbol}{last_price:,.2f}",

        f"{currency_symbol}{predicted_price:,.2f}",

        f"{change_percent:.2f}%",

        f"{score:.4f}",

        recommendation

    ]

})

st.dataframe(

    summary,

    use_container_width=True,

    hide_index=True

)

st.divider()

# =====================================================
# Quick Analysis
# =====================================================

st.subheader("📌 Quick Analysis")

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
**Current Price**

{currency_symbol}{last_price:,.2f}
""")

    st.info(f"""
**Predicted Price**

{currency_symbol}{predicted_price:,.2f}
""")

with col2:

    st.info(f"""
**Expected Return**

{change_percent:.2f}%
""")

    st.info(f"""
**Recommendation**

{recommendation}
""")

st.divider()

# =====================================================
# PART 3C
# About the Model
# =====================================================

st.subheader("📚 About This Prediction Model")

st.info("""

### Machine Learning Model Used

This project uses a **Linear Regression** model from the
Scikit-Learn library.

The model learns the historical closing price trend and
estimates future prices using a simple linear relationship
between time and stock price.

This model is intentionally simple because the goal of this
project is to demonstrate:

• Data Collection using Yahoo Finance

• Data Cleaning using Pandas

• Feature Engineering

• Machine Learning with Scikit-Learn

• Data Visualization using Plotly

• Interactive Dashboard using Streamlit

""")

st.divider()

# =====================================================
# Model Limitations
# =====================================================

st.subheader("⚠️ Model Limitations")

st.warning("""

The prediction generated by this dashboard is based only on
historical closing prices.

The model DOES NOT consider:

• Company Financial Results

• Quarterly Earnings

• Market News

• Global Events

• Interest Rates

• Investor Sentiment

• Government Policies

Therefore, actual market prices may differ significantly
from the predicted values.

""")

st.divider()

# =====================================================
# Investment Disclaimer
# =====================================================

st.subheader("⚠️ Investment Disclaimer")

st.error("""

This dashboard is developed ONLY for educational,
learning and portfolio purposes.

The prediction shown in this application should NOT be
considered financial or investment advice.

Always perform your own research before making
investment decisions.

The developer is not responsible for any financial loss
resulting from the use of this application.

""")

st.divider()

# =====================================================
# Last Updated
# =====================================================

st.caption(
    f"Last Updated : {datetime.datetime.now().strftime('%d %B %Y')}"
)

# =====================================================
# Footer
# =====================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center">

<h4>📈 Stock Prediction Dashboard</h4>

Developed by <b>Momin Analyst</b>

Python • Pandas • NumPy • Scikit-Learn • Plotly • Streamlit • Yahoo Finance

© 2026 All Rights Reserved

</div>
""",
unsafe_allow_html=True
)

