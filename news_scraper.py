# news_scraper.py (using Finnhub API)
import finnhub
import os  # For environment variables
from dotenv import load_dotenv
load_dotenv() # Load .env file at the very beginning
def scrape_stock_news(stock_symbol):
    """
    Fetches news headlines for a stock symbol from Finnhub API.

    Args:
        stock_symbol (str): The stock ticker symbol.

    Returns:
        list: List of news headlines (and links), or None if error or no news.
    """
    finnhub_api_key = os.environ.get("FINNHUB_API_KEY") # Get API key from environment variable
    if not finnhub_api_key:
        print("Error: FINNHUB_API_KEY environment variable not set.")
        return None

    finnhub_client = finnhub.Client(api_key=finnhub_api_key)

    try:
        news = finnhub_client.company_news(
            stock_symbol, _from="2024-01-01", to="2025-01-24" # Adjust date range as needed
        )
        headlines = []
        if news: # Check if news list is not empty
            for article in news:
                headlines.append(f"{article['headline']} - {article['url']}") # Or just article['headline'] for headline only
        return headlines
    except Exception as e:
        print(f"Error fetching news from Finnhub API for {stock_symbol}: {e}")
        return None

if __name__ == '__main__':
    stock_symbol = "AAPL"
    news_headlines = scrape_stock_news(stock_symbol)
    if news_headlines:
        print(f"News headlines for {stock_symbol} (using Finnhub API):\n")
        for headline in news_headlines:
            for headline_text in news_headlines: # Now headlines is already a list of strings
                print(f"- {headline_text}")
    else:
        print(f"Could not fetch news for {stock_symbol} using Finnhub API.")