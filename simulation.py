
import numpy as np

def simulate_portfolio_paths(
    returns_df, weights, initial_value=100000, horizon_days=10, n_simulations=10000
):
    """
    Simulate future portfolio values using Monte Carlo simulation.
    """

    mu = returns_df.mean().values         # Daily mean returns (vector)
    cov = returns_df.cov().values         # Covariance matrix
    weights = np.array(weights)           # Ensure numpy array

    n_assets = len(weights)

    # Generate simulations: shape (n_simulations, horizon_days, n_assets)
    simulations = np.random.multivariate_normal(mu, cov, (n_simulations, horizon_days))

    # Calculate daily portfolio return for each simulation path
    portfolio_returns = np.dot(simulations, weights)

    # Sum log returns across horizon (compounded return)
    total_log_returns = portfolio_returns.sum(axis=1)

    # Convert to final values
    final_values = initial_value * np.exp(total_log_returns)

    return final_values
