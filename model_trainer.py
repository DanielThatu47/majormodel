# model_trainer.py
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib # For saving the model

def train_model(processed_data):
    """
    Trains an XGBoost model on processed stock data.

    Args:
        processed_data (pandas.DataFrame): Processed stock data.

    Returns:
        xgboost.XGBRegressor: Trained XGBoost model.
    """
    if processed_data.empty:
        print("Error: No processed data available for training.")
        return None

    X = processed_data[['Open', 'Close_Lag1', 'Open_Lag1']]
    y = processed_data['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42) # Basic parameters
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred)
    print(f"Model RMSE on Test Set: {rmse}")

    return model

def save_model(model, filepath="stock_price_model.pkl"):
    """Saves the trained model to a file."""
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")

if __name__ == '__main__':
    from data_fetcher import fetch_stock_data
    from data_processor import preprocess_data

    stock_symbol = "AAPL"
    stock_data = fetch_stock_data(stock_symbol)
    if stock_data is not None:
        processed_data = preprocess_data(stock_data)
        if not processed_data.empty:
            model = train_model(processed_data)
            if model:
                save_model(model)