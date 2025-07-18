import streamlit as st
import numpy as np

# Import your existing modules/functions
from data_loader import download_price_data, compute_log_returns
from simulation import simulate_portfolio_paths
from risk_metrics import compute_risk_metrics
from plots import plot_distribution

st.title("Monte Carlo Simulation for Portfolio Risk Analysis")

# Sidebar inputs
st.sidebar.header("Input Parameters")

tickers = st.sidebar.multiselect(
    "Select Tickers",
    options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
    default=["AAPL", "MSFT", "GOOGL"]
)

if len(tickers) == 0:
    st.warning("Please select at least one ticker.")
    st.stop()

weights = []
st.sidebar.markdown("### Portfolio Weights")
for ticker in tickers:
    w = st.sidebar.slider(f"Weight for {ticker}", 0.0, 1.0, 0.3, step=0.05)
    weights.append(w)

# Normalize weights
weights = np.array(weights)
weights = weights / weights.sum()

initial_value = st.sidebar.slider("Initial Portfolio Value ($)", 10000, 1000000, 100000, step=10000)
horizon_days = st.sidebar.slider("Investment Horizon (days)", 1, 365, 10)
n_simulations = st.sidebar.slider("Number of Simulations", 100, 100000, 10000, step=100)
confidence_level = st.sidebar.slider("VaR Confidence Level (%)", 90, 99, 95) / 100

st.write("### Simulation Settings")
st.write(f"Tickers: {tickers}")
st.write(f"Weights: {weights}")
st.write(f"Initial Value: ${initial_value}")
st.write(f"Horizon: {horizon_days} days")
st.write(f"Number of Simulations: {n_simulations}")
st.write(f"VaR Confidence Level: {int(confidence_level*100)}%")

if st.button("Run Simulation"):

    with st.spinner("Running Monte Carlo simulation..."):
        # Download price data and compute returns
        price_df = download_price_data(tickers)
        returns_df = compute_log_returns(price_df)

        # Run simulation
        final_values = simulate_portfolio_paths(
            returns_df, weights, initial_value, horizon_days, n_simulations
        )

        # Compute risk metrics
        metrics = compute_risk_metrics(final_values, initial_value, confidence_level)

        var = metrics["VaR"]
        cvar = metrics["CVaR"]
        expected_return = metrics["Expected Return"]
        prob_loss = metrics["Probability of Loss"]

        # Display metrics
        st.subheader("Risk Metrics")
        st.write(f"Value at Risk (VaR): ${var:,.2f}")
        st.write(f"Conditional VaR (CVaR): ${cvar:,.2f}")
        st.write(f"Expected Return: ${expected_return:,.2f}")
        st.write(f"Probability of Loss: {prob_loss:.2%}")

        # Plot distribution
        fig = plot_distribution(final_values, initial_value, var_level=1-confidence_level)
        st.pyplot(fig)
