# predictor.py
import pandas as pd
import joblib
import os

def load_model(filepath="stock_price_model.pkl"):
    """Loads the trained model from a file."""
    try:
        print(f"Attempting to load model from: {filepath}") # Print the filepath
        if not os.path.exists(filepath): # Check if file exists
            print(f"Error: Model file not found at: {filepath}")
            return None
        model = joblib.load(filepath)
        print("Model loaded successfully.") # Print success message
        return model
    except Exception as e:
        print(f"Error loading model from {filepath}: {e}") # More specific error message
        return None

def predict_future_prices(model, last_day_data, days_to_predict=1):
    """
    Predicts stock prices for the next few days.

    Args:
        model (xgboost.XGBRegressor): Trained XGBoost model.
        last_day_data (pandas.Series): Data for the last available day (Open, Close_Lag1, Open_Lag1).
        days_to_predict (int): Number of days to predict.

    Returns:
        list: List of predicted closing prices for the next days.
    """
    predictions = []
    current_features = last_day_data.to_dict() # Convert Series to dict for easy access

    for _ in range(days_to_predict):
        input_features = pd.DataFrame([current_features]) # Create DataFrame for prediction
        predicted_price = model.predict(input_features)[0]
        predictions.append(predicted_price)

        # Update features for next day prediction (simplistic approach - using predicted close as next day's open)
        current_features['Open_Lag1'] = current_features['Open'] # Shift Open to Open_Lag1
        current_features['Close_Lag1'] = predicted_price # Use predicted Close as next day's Close_Lag1
        current_features['Open'] = predicted_price # Assume predicted Close becomes next day's Open (simplification!)

    return predictions

if __name__ == '__main__':
    from data_fetcher import fetch_stock_data
    from data_processor import preprocess_data

    stock_symbol = "AAPL"
    stock_data = fetch_stock_data(stock_symbol, period="1y") # Use recent data for prediction
    if stock_data is not None:
        processed_data = preprocess_data(stock_data)
        if not processed_data.empty:
            model = load_model()
            if model:
                last_day_data = processed_data.iloc[[-1]][['Open', 'Close_Lag1', 'Open_Lag1']].iloc[0] # Get last row, select features, get Series
                days_to_predict = 3
                predicted_prices = predict_future_prices(model, last_day_data, days_to_predict)
                print(f"Predicted prices for the next {days_to_predict} days: {predicted_prices}")