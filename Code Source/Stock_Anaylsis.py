import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Analysis Dashboard")

st.write("""
Analyze any listed company using historical stock data,
company information and financial metrics.
""")

st.divider()

# ---------------------------------------------------
# FORMAT FUNCTIONS
# ---------------------------------------------------

def format_market_cap(value, currency):

    if value is None:
        return "N/A"

    if currency == "INR":

        crore = value / 10000000

        if crore >= 100000:
            return f"₹ {crore/100000:.2f} Lakh Crore"

        return f"₹ {crore:,.2f} Crore"

    else:

        if value >= 1_000_000_000_000:
            return f"$ {value/1_000_000_000_000:.2f} Trillion"

        elif value >= 1_000_000_000:
            return f"$ {value/1_000_000_000:.2f} Billion"

        elif value >= 1_000_000:
            return f"$ {value/1_000_000:.2f} Million"

        return f"$ {value:,.0f}"


def format_employees(value):

    if value is None:
        return "N/A"

    if value >= 100000:

        return f"{value/100000:.2f} Lakh"

    elif value >= 1000:

        return f"{value/1000:.1f} K"

    return str(value)


# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

today = datetime.date.today()

col1,col2,col3 = st.columns(3)

with col1:

    ticker = st.text_input(
        "Stock Symbol",
        "PWL.NS"
    ).upper()


with col2:

    start_date = st.date_input(

        "Start Date",

        datetime.date(
            today.year-1,
            today.month,
            today.day
        )

    )


with col3:

    end_date = st.date_input(

        "End Date",

        today

    )


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

stock = yf.Ticker(ticker)

try:

    info = stock.info

except:

    st.error("Unable to fetch company information.")

    st.stop()


history = stock.history(

    start=start_date,

    end=end_date

)

if history.empty:

    st.error("No historical data found.")

    st.stop()


# ---------------------------------------------------
# CURRENCY DETECTION
# ---------------------------------------------------

currency = info.get("currency","USD")

currency_symbols = {

    "USD":"$",

    "INR":"₹",

    "EUR":"€",

    "GBP":"£",

    "JPY":"¥"

}

currency_symbol = currency_symbols.get(currency,currency+" ")

st.divider()

# ---------------------------------------------------
# COMPANY NAME
# ---------------------------------------------------

st.header(f"🏢 {info.get('longName', ticker)}")

st.caption(
    f"{info.get('sector','N/A')} • {info.get('industry','N/A')}"
)

st.divider()

# ---------------------------------------------------
# COMPANY OVERVIEW
# ---------------------------------------------------

st.subheader("📌 Company Overview")

left,right = st.columns([2,1])

with left:

    st.markdown("### Business Summary")

    summary = info.get(
        "longBusinessSummary",
        "No Company Information Available."
    )

    st.write(summary)

with right:

    st.markdown("### Basic Information")

    st.write("**🌍 Country:**", info.get("country","N/A"))

    st.write("**🏙 City:**", info.get("city","N/A"))

    st.write("**🏢 Sector:**", info.get("sector","N/A"))

    st.write("**💼 Industry:**", info.get("industry","N/A"))

    st.write("**🏦 Exchange:**", info.get("exchange","N/A"))

    st.write("**💱 Currency:**", currency)

    st.write("**👨‍💼 Employees:**",
             format_employees(
                 info.get("fullTimeEmployees")
             )
    )

    st.write("**🌐 Website:**")

    st.markdown(info.get("website","N/A"))

st.divider()

# ---------------------------------------------------
# COMPANY AT A GLANCE
# ---------------------------------------------------

st.subheader("📖 Company at a Glance")

employees = format_employees(
    info.get("fullTimeEmployees")
)

market_cap = format_market_cap(
    info.get("marketCap"),
    currency
)

st.markdown(f"""

### 🏢 Company Snapshot

- 🌍 **Country:** {info.get("country","N/A")}

- 🏙 **Headquarters:** {info.get("city","N/A")}

- 💼 **Industry:** {info.get("industry","N/A")}

- 🏦 **Sector:** {info.get("sector","N/A")}

- 👨‍💼 **Employees:** {employees}

- 💰 **Market Cap:** {market_cap}

- 💱 **Trading Currency:** {currency}

""")

st.info("""

This section provides a quick overview of the company,
its business category, employee strength,
market size and geographical information.

""")

st.divider()

# ---------------------------------------------------
# FINANCIAL HIGHLIGHTS
# ---------------------------------------------------

st.subheader("📊 Financial Highlights")

m1,m2,m3,m4 = st.columns(4)

with m1:

    st.metric(

        "Market Cap",

        format_market_cap(

            info.get("marketCap"),

            currency

        )

    )

with m2:

    st.metric(

        "EPS",

        f"{currency_symbol}{info.get('trailingEps',0):,.2f}"

    )

with m3:

    st.metric(

        "PE Ratio",

        round(

            info.get("trailingPE",0),

            2

        )

    )

with m4:

    st.metric(

        "Beta",

        round(

            info.get("beta",0),

            2

        )

    )

st.caption(
    "Financial metrics are collected from Yahoo Finance."
)

st.divider()

# ---------------------------------------------------
# STOCK PRICE SUMMARY
# ---------------------------------------------------

st.subheader("📈 Stock Price Summary")

current_price = round(history["Close"].iloc[-1], 2)

highest_price = round(history["High"].max(), 2)

lowest_price = round(history["Low"].min(), 2)

average_price = round(history["Close"].mean(), 2)

week52_high = round(history["High"].max(), 2)

week52_low = round(history["Low"].min(), 2)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Current Price",
        f"{currency_symbol}{current_price:,.2f}"
    )

with col2:

    st.metric(
        "52 Week High",
        f"{currency_symbol}{week52_high:,.2f}"
    )

with col3:

    st.metric(
        "52 Week Low",
        f"{currency_symbol}{week52_low:,.2f}"
    )

col4, col5, col6 = st.columns(3)

with col4:

    st.metric(
        "Highest Price",
        f"{currency_symbol}{highest_price:,.2f}"
    )

with col5:

    st.metric(
        "Lowest Price",
        f"{currency_symbol}{lowest_price:,.2f}"
    )

with col6:

    st.metric(
        "Average Price",
        f"{currency_symbol}{average_price:,.2f}"
    )

st.divider()

# ---------------------------------------------------
# PRICE PERFORMANCE
# ---------------------------------------------------

st.subheader("📊 Price Performance")

price_change = current_price - average_price

price_change_percent = (price_change / average_price) * 100

if price_change > 0:

    st.success(
        f"""
Current price is **{price_change_percent:.2f}%**
above the average price for the selected period.
"""
    )

else:

    st.error(
        f"""
Current price is **{abs(price_change_percent):.2f}%**
below the average price for the selected period.
"""
    )

st.divider()

# ---------------------------------------------------
# RISK ANALYSIS
# ---------------------------------------------------

st.subheader("🛡 Risk Analysis")

beta = info.get("beta", 0)

if beta >= 1.2:

    st.error("🔴 High Risk Stock")

elif beta >= 0.8:

    st.warning("🟡 Moderate Risk Stock")

else:

    st.success("🟢 Low Risk Stock")

st.write(f"**Beta Value:** {beta}")

st.info("""
Beta measures how much a stock moves compared to the market.

• Beta > 1 → Higher Volatility

• Beta ≈ 1 → Similar to Market

• Beta < 1 → Lower Risk
""")

st.divider()

# ---------------------------------------------------
# VALUATION
# ---------------------------------------------------

st.subheader("💰 Valuation")

pe = info.get("trailingPE")

if pe:

    if pe < 20:

        st.success("🟢 The stock appears Undervalued.")

    elif pe <= 35:

        st.warning("🟡 The stock appears Fairly Valued.")

    else:

        st.error("🔴 The stock appears Expensive.")

st.write(f"**PE Ratio:** {pe}")

st.info("""
Price-to-Earnings (PE) Ratio compares the company's share price
with its earnings per share.

A lower PE may indicate a cheaper valuation,
while a higher PE may indicate premium pricing.
""")

st.divider()

# ---------------------------------------------------
# STOCK PRICE CHART
# ---------------------------------------------------

st.subheader("📉 Closing Price Trend")

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=history.index,

        y=history["Close"],

        mode="lines",

        name="Closing Price"

    )

)

fig.update_layout(

    template="plotly_dark",

    height=550,

    xaxis_title="Date",

    yaxis_title=f"Price ({currency})",

    hovermode="x unified"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ---------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------

st.divider()

st.subheader("⚠️ Investment Disclaimer")

st.warning("""
### Educational Purpose Only

This dashboard has been developed for **educational, learning, and portfolio purposes only**.

The stock market data displayed in this application is collected from **Yahoo Finance** using the **yfinance** library.

The charts, financial metrics, valuation, risk analysis, and investment summary are generated using publicly available data and simple analytical methods.

This application **does not provide financial, investment, or trading advice**.

Before making any investment decision, always perform your own research and consult a qualified financial advisor.
""")

st.divider()