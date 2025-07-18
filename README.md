# Monte Carlo Simulation for Portfolio Risk Analysis

This Streamlit app simulates the potential future value of a portfolio using Monte Carlo methods. It computes key risk metrics such as Value at Risk (VaR), Conditional Value at Risk (CVaR), expected return, and probability of loss based on historical log returns of selected stocks.

---

## 📊 Features

- Select from popular stock tickers (AAPL, MSFT, GOOGL, AMZN, TSLA)
- Adjust portfolio weights using sliders
- Simulate portfolio performance over a chosen investment horizon
- Run thousands of Monte Carlo simulations with customizable parameters
- Compute and visualize:
  - **Value at Risk (VaR)**
  - **Conditional VaR (CVaR)**
  - **Expected Return**
  - **Probability of Loss**
- Histogram of final portfolio values with VaR threshold indicator

---

## 🧠 Methods Used

- Historical log returns via `yfinance`
- Portfolio returns sampled using multivariate normal distribution
- Monte Carlo simulation for generating possible future scenarios
- Risk metrics calculated from simulated portfolio value distribution

---

🚀 Running the App

Simply run:

streamlit run main.py

Your browser should open the app at http://localhost:8501


⚙️ Dependencies
Make sure the following Python packages are installed:

streamlit

numpy

pandas

matplotlib

seaborn

yfinance

Install all at once with:

pip install streamlit numpy pandas matplotlib seaborn yfinance

Or use:

pip install -r requirements.txt

🧪 Example Usage
Tickers: AAPL, MSFT, GOOGL

Weights: 30%, 40%, 30%

Initial Portfolio Value: $100,000

Investment Horizon: 30 days

Simulations: 10,000

VaR Confidence Level: 95%

You’ll get output metrics like:

Value at Risk (VaR): $2,789.31
Conditional VaR (CVaR): $4,032.56
Expected Return: $1,189.78
Probability of Loss: 41.73%

📌 Notes
Prices are pulled using Yahoo Finance with auto_adjust=True

Log returns are used for accurate modeling of compounded returns

Simulations assume normally distributed returns, which may not capture extreme events or skewness

