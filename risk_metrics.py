
import numpy as np


def compute_risk_metrics(final_values, initial_value, confidence_level=0.95):
    """
    Compute VaR, CVaR, expected return, and probability of loss.
    """
    sorted_values = np.sort(final_values)
    percentile_index = int((1 - confidence_level) * len(sorted_values))

    var = initial_value - sorted_values[percentile_index]
    cvar = initial_value - sorted_values[:percentile_index].mean()
    expected_return = np.mean(final_values) - initial_value
    prob_loss = np.mean(final_values < initial_value)

    return {
        "VaR": var,
        "CVaR": cvar,
        "Expected Return": expected_return,
        "Probability of Loss": prob_loss
    }
