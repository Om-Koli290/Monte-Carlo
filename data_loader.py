
import yfinance as yf
import numpy as np
import pandas as pd


def download_price_data(tickers, start="2020-01-01", end="2024-12-31"):
    """
    Downloads adjusted price data. Uses 'Close' by default since yfinance auto-adjusts now.
    """
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)

    # If multiple tickers, 'Close' is a column level; else it's a Series
    if isinstance(data.columns, pd.MultiIndex):
        return data["Close"].dropna()
    else:
        return data.dropna().to_frame(name=tickers[0])  # convert Series to DataFrame

def compute_log_returns(price_df):
    """
    Compute daily log returns from price data.
    """
    return np.log(price_df / price_df.shift(1)).dropna()
