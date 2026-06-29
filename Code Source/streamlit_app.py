import streamlit as st

st.set_page_config(
    page_title ="Trading App",
    page_icon= "📈",
    layout = "wide"
)
st.title("📈 Momin Analyst - Trading Dashboard")

st.header("Welcome to Momin Analyst")

st.write(
    "### An interactive trading dashboard designed to help traders analyze market data, "
    "explore stock insights, and make informed investment decisions."
)

st.image("app.png")

st.markdown("## 🚀 Key Features")

st.markdown("### 📊 1. Stock Market Analysis")
st.write(
    "Analyze historical stock data, price trends, trading volume, and key market indicators "
    "through interactive visualizations."
)

st.markdown("### 🔮 2. Stock Price Prediction")
st.write(
    "Generate future stock price predictions using machine learning models trained on historical market data."
)

st.markdown("### 📈 3. Risk & Return Analysis (CAPM)")
st.write(
    "Calculate Expected Return, Beta, and Market Risk using the Capital Asset Pricing Model (CAPM) "
    "to evaluate investment opportunities."
)

st.markdown("### 📉 4. Technical Indicators")
st.write(
    "Visualize important technical indicators such as Moving Averages, RSI, MACD, and Bollinger Bands "
    "to identify market trends."
)

st.markdown("### 📁 5. Interactive Dashboard")
st.write(
    "A clean and user-friendly dashboard that allows users to upload datasets, "
    "explore charts, and gain actionable insights."
)
