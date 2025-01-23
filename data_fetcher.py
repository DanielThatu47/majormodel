# data_fetcher.py
import yfinance as yf

def fetch_stock_data(stock_symbol, period="5y"):
    """
    Fetches historical stock data from Yahoo Finance.

    Args:
        stock_symbol (str): The stock ticker symbol (e.g., 'AAPL').
        period (str): The period for which to fetch data (e.g., '5y', '10y', 'max').

    Returns:
        pandas.DataFrame: DataFrame containing stock data, or None if error.
    """
    try:
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period=period)
        return data
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")
        return None

if __name__ == '__main__':
    stock_symbol = "AAPL"  # Example: Apple Inc.
    stock_data = fetch_stock_data(stock_symbol)
    if stock_data is not None:
        print(f"Data for {stock_symbol}:\n", stock_data.head())