
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_distribution(final_values, initial_value, var_level=0.05):
    """
    Create and return a matplotlib figure for the distribution
    of simulated final portfolio values, so it can be used in Streamlit.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(final_values, bins=50, kde=True, color="skyblue", ax=ax)

    var_threshold = np.percentile(final_values, var_level * 100)
    ax.axvline(var_threshold, color="red", linestyle="--", label=f"{int(var_level*100)}% VaR")

    ax.axvline(initial_value, color="black", linestyle="--", label="Initial Value")

    ax.set_title("Simulated Portfolio Value Distribution")
    ax.set_xlabel("Final Portfolio Value")
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()

    return fig
