from flask import Flask, request, jsonify , render_template
from predictor import load_model, predict_future_prices # Keep predictor functions
from flask_cors import CORS
from data_fetcher import fetch_stock_data # **ADD THIS LINE**
from data_processor import preprocess_data # **ADD THIS LINE**
from news_scraper import scrape_stock_news # **ADD THIS LINE** (optional, if you use news scraping)

app = Flask(__name__)
CORS(app)

model = load_model() # Load model *globally* when app starts - crucial for testing

if model is None: # **Critical check: Add this error handling immediately after loading**
    print("Error: Model not loaded! Application will not function correctly.")
else:
    print("Model loaded successfully (in app.py global scope).") # Confirmation in global scope




@app.route('/test_predict') # Simple test route
def test_predict_route():
    if model is None: # **Critical check inside route as well**
        return jsonify({"error": "Model is not loaded in the route!"}), 500

    # Create dummy input data for a quick test prediction
    dummy_last_day_data = {'Open': 150.0, 'Close_Lag1': 152.0, 'Open_Lag1': 149.5} # Example values
    predictions = predict_future_prices(model, pd.Series(dummy_last_day_data), days_to_predict=1)

    # **Convert NumPy float32 to Python float for JSON serialization:**
    python_float_predictions = [float(pred) for pred in predictions] 

    return jsonify({"test_prediction": python_float_predictions}) # Use the converted list

@app.route('/')  # Route for the root URL "/"
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_stock():
    stock_symbol = request.json.get('stock_symbol')
    days_to_predict = int(request.json.get('days', 1))

    if not stock_symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    stock_data = fetch_stock_data(stock_symbol, period="1y") # Fetch data
    if stock_data is None:
        return jsonify({"error": f"Could not fetch data for {stock_symbol}"}), 400

    processed_data = preprocess_data(stock_data) # Preprocess data
    if processed_data.empty:
        return jsonify({"error": "Insufficient data for prediction"}), 400

    last_day_data = processed_data.iloc[[-1]][['Open', 'Close_Lag1', 'Open_Lag1']].iloc[0] # Get last day's data
    predictions = predict_future_prices(model, last_day_data, days_to_predict) # Make predictions
    python_float_predictions = [float(pred) for pred in predictions] # Convert to Python floats

    news = scrape_stock_news(stock_symbol) # Scrape news (optional)
    
    return jsonify({ # Return full response
        "stock_symbol": stock_symbol,
        "predictions": python_float_predictions, # Use converted predictions
        "news_headlines": news if news else [],
    })


if __name__ == '__main__':
    import pandas as pd # Import pandas here, as it's used in dummy data in test_predict_route
    app.run(host='0.0.0.0')
