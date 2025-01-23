# Stock Market Prediction Application

## Overview

This application predicts stock prices for the next few days using historical data from Yahoo Finance and an XGBoost machine learning model. It allows users to search for stocks by their ticker symbol, select the number of days for prediction, and view predicted closing prices.  Optionally, it also displays recent news headlines for the selected stock fetched from the Finnhub API. The application is built with a Python Flask backend, an XGBoost model trained on Yahoo Finance data, and a user interface styled with Tailwind CSS.

**Please note:** Stock market predictions are inherently uncertain and should not be considered financial advice. This application is for educational and demonstrational purposes only.

## Prerequisites

Before you begin, ensure you have the following software installed on your system:

1.  **Python 3.7+**:  Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  **pip**: Python package installer (usually included with Python installations).
3.  **virtualenv**:  For creating isolated Python environments. Install using: `pip install virtualenv`
4.  **Node.js and npm**: Required for Tailwind CSS and frontend asset building. Download from [https://nodejs.org/](https://nodejs.org/)
5.  **ChromeDriver**:  If you intend to use Selenium for web scraping (currently not used in the recommended setup, but might be needed if you decide to implement web scraping instead of Finnhub API for news). Download the ChromeDriver that matches your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and ensure it's in your system's PATH.
6.  **Finnhub API Key**: If you want to enable stock news fetching, you will need a free API key from [https://finnhub.io/](https://finnhub.io/).

## Installation and Setup

Follow these steps to set up the project on your local machine:

1.  **Clone the repository (if you have the code in a repository):**

    ```bash
    git clone <repository_url>
    cd stock_predictor_app
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, create one with the following content and then run the `pip install` command:

    ```
    yfinance
    xgboost
    scikit-learn
    beautifulsoup4
    requests
    flask
    flask-cors
    python-dotenv
    joblib
    pandas
    selenium  # Required only if you plan to use Selenium for web scraping (news)
    finnhub-python # Required for Finnhub API for news
    ```

5.  **Install Node.js dependencies (for Tailwind CSS):**

    ```bash
    npm install
    ```

6.  **Set up Finnhub API Key (if you want news):**

    *   **Get a Finnhub API key:** Sign up for a free account at [https://finnhub.io/](https://finnhub.io/) and obtain your API key from your dashboard.
    *   **Create a `.env` file:** In the root of your `stock_predictor_app` project directory, create a file named `.env`.
    *   **Add your API key to `.env`:** Open `.env` and add the following line, replacing `YOUR_ACTUAL_FINNHUB_API_KEY` with your actual API key:

        ```
        FINNHUB_API_KEY=YOUR_ACTUAL_FINNHUB_API_KEY
        ```
    *   **Important:** Add `.env` to your `.gitignore` file to prevent committing your API key to version control.

7.  **Train the XGBoost Model:**

    ```bash
    python model_trainer.py
    ```
    This script will fetch stock data for AAPL, train the XGBoost model, and save it as `stock_price_model.pkl` in your project directory.

8.  **Build Tailwind CSS:**

    ```bash
    npm run tailwind build
    ```
    This command uses the Tailwind CLI to process your `frontend/style.css` file and generate the compiled CSS in `frontend/output.css`.

## Running the Application

1.  **Start the Flask Backend Server:**

    ```bash
    python app.py
    ```
    You should see output indicating that the Flask development server is running, usually at `http://127.0.0.1:5000` or `http://localhost:5000`. **Keep this terminal window open while running the application.**

2.  **Access the Frontend in your Browser:**

    Open your web browser and go to the following URL:

    ```
    http://localhost:5000/
    ```

    You should see the Stock Market Prediction application interface.

## Using the Application

1.  **Enter Stock Symbol:** In the input field, type the ticker symbol of the stock you want to predict (e.g., AAPL, MSFT, GOOG).
2.  **Select Prediction Days:** Choose the number of days you want to predict using the dropdown menu (1, 2, 3, or 5 days).
3.  **Click "Predict":** Click the "Predict" button.
4.  **View Predictions:** The predicted closing prices for the selected number of days will be displayed under the "Prediction Results" section.
5.  **Latest News (Optional):** If you have set up the Finnhub API key correctly, the latest news headlines for the stock (if available from Finnhub) will be displayed under the "Latest News" section.

## Tailwind CSS Building (Development)

For development, you can run Tailwind CSS in watch mode to automatically rebuild your CSS whenever you make changes to `frontend/style.css` or your Tailwind configuration:

```bash
npm run tailwind:dev