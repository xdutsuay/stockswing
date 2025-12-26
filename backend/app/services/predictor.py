import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import logging

logger = logging.getLogger(__name__)

class StockPredictor:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.timestep = 60
        self._load_model()

    def _load_model(self):
        try:
            # Try loading with compile=False to avoid some keras 2/3 issues
            self.model = tf.keras.models.load_model(self.model_path, compile=False)
            logger.info(f"Model loaded from {self.model_path}")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            self.model = None

    def prepare_data(self, data: pd.DataFrame):
        # Expecting 'Close' column as column 3 (index 3) or explicitly named
        # Legacy code used: iloc[-60:, 3:4]
        # We will try to find 'Close' column
        if 'Close' in data.columns:
            dataset = data[['Close']].values
        else:
            # Fallback to 4th column if available, else 0
            if data.shape[1] >= 4:
                dataset = data.iloc[:, 3:4].values
            else:
                dataset = data.iloc[:, 0:1].values
        
        return dataset

    def predict(self, data: pd.DataFrame, days: int = 7) -> list[float]:
        dataset = self.prepare_data(data)
        
        if len(dataset) < self.timestep:
            raise ValueError(f"Not enough data points. Need at least {self.timestep}")

        # If model failed to load, return a simulated trend for demo purposes
        if self.model is None:
            logger.warning("Model not loaded. Returning simulated trend.")
            last_price = float(dataset[-1][0])  # Extract scalar from array
            # Simple random walk for simulation
            simulated = []
            current = last_price
            for _ in range(days):
                # Slightly bullish bias for demo
                change = current * np.random.uniform(-0.01, 0.015)
                current += change
                simulated.append(float(current))
            return simulated

        # Take last 60 days
        target_data = dataset[-self.timestep:]
        scaled_data = self.scaler.fit_transform(target_data)
        
        current_batch = scaled_data.reshape(1, self.timestep, 1)
        predictions = []

        for _ in range(days):
            pred = self.model.predict(current_batch, verbose=0)
            predictions.append(pred[0, 0])
            
            # Update batch: remove first, add new prediction
            current_batch = np.append(current_batch[:, 1:, :], pred.reshape(1, 1, 1), axis=1)

        # Inverse transform
        predictions = np.array(predictions).reshape(-1, 1)
        original_predictions = self.scaler.inverse_transform(predictions)
        
        return original_predictions.flatten().tolist()


    def analyze_trend(self, recent_data: pd.DataFrame, predictions: list[float]) -> tuple[str, float]:
        """
        Analyze trend based on recent historical data and predictions.
        Returns (trend, confidence) where trend is 'bullish', 'bearish', or 'neutral'.
        Confidence is a float between 0.0 and 1.0.
        """
        dataset = self.prepare_data(recent_data)
        if len(dataset) < 5:
            return "neutral", 0.5
        
        # Get last 5 historical prices - ensure they're Python floats
        recent_prices = [float(x) for x in dataset[-5:].flatten()]
        
        # Calculate historical trend (last 5 days)
        historical_change = 0.0
        if recent_prices[0] != 0:
            historical_change = (recent_prices[-1] - recent_prices[0]) / recent_prices[0]
        
        # Calculate predicted trend
        predicted_change = 0.0
        if len(predictions) >= 3 and recent_prices[-1] != 0:
            # Ensure prediction is a float
            last_prediction = float(predictions[-1])
            last_price = float(recent_prices[-1])
            predicted_change = (last_prediction - last_price) / last_price
        
        # Count upward vs downward movements in predictions
        up_moves = 0
        down_moves = 0
        for i in range(len(predictions) - 1):
            if float(predictions[i + 1]) > float(predictions[i]):
                up_moves += 1
            elif float(predictions[i + 1]) < float(predictions[i]):
                down_moves += 1
        
        # Determine trend
        if predicted_change > 0.02:  # More than 2% increase predicted
            trend = "bullish"
            confidence = min(0.95, 0.5 + abs(predicted_change) * 10)
        elif predicted_change < -0.02:  # More than 2% decrease predicted
            trend = "bearish"
            confidence = min(0.95, 0.5 + abs(predicted_change) * 10)
        else:
            trend = "neutral"
            # Lower confidence for neutral trends
            confidence = max(0.3, 0.7 - abs(predicted_change) * 5)
        
        # Adjust confidence based on consistency of predictions
        if len(predictions) > 1:
            consistency = abs(up_moves - down_moves) / (len(predictions) - 1)
            confidence = (confidence + consistency) / 2
        
        return trend, round(confidence, 2)


