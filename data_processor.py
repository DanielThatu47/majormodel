# data_processor.py
import pandas as pd

def preprocess_data(data):
    """
    Preprocesses stock data, creating features for model training.

    Args:
        data (pandas.DataFrame): Stock data from Yahoo Finance.

    Returns:
        pandas.DataFrame: Processed DataFrame with features.
    """
    if data is None or data.empty:
        return pd.DataFrame() # Return empty DataFrame if input is invalid

    data = data[['Open', 'Close']] # Focus on Open and Close prices
    data['Close_Lag1'] = data['Close'].shift(1)
    data['Open_Lag1'] = data['Open'].shift(1)
    data = data.dropna() # Remove rows with NaN due to shifting
    return data

if __name__ == '__main__':
    from data_fetcher import fetch_stock_data  # Assuming data_fetcher.py is in the same directory

    stock_symbol = "AAPL"
    stock_data = fetch_stock_data(stock_symbol)
    if stock_data is not None:
        processed_data = preprocess_data(stock_data)
        print("Processed Data:\n", processed_data.head())