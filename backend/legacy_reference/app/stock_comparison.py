from app.Learningapp.tickers import Tickers
from app.stock_prediction import StockPrediction
from app.data_extraction import HistoricalData
from tensorflow.keras.models import load_model
import json
import datetime

tickers = Tickers()


class BestStocks():
    NSETICKERS: list = tickers.NSE_TICKER
    TICKER_DATASET_PATH: str = 'app/Learningapp/tickerData/'
    TICKER_MODEL_PATH: str = 'app/Learningapp/models/'

    def __init__(self, extended_model_path: str = '', excluded: list = []) -> None:
        self.TICKER_MODEL_PATH = self.TICKER_MODEL_PATH + extended_model_path
        self.excluded = excluded
        self.NSETICKERS = [
            ticker for ticker in self.NSETICKERS if ticker not in self.excluded]

    def _stock_movement(self, days: int = 6) -> list:
        '''
        Returns the stock movement of the last 5 days
        '''
        stock_movement = []
        hd = HistoricalData()
        data = hd.get_recent_data()
        for ticker in self.NSETICKERS:
            previous_close = data[ticker]['Close'].iloc[-1]
            model = load_model(self.TICKER_MODEL_PATH+f'{ticker}.h5')
            sp = StockPrediction(model, data[ticker])
            results = sp.long_prediction(days).flatten() # flatten to 1D array
            predictions = {
                f'day{i}': {
                    'prediction': int(results[i-1]),
                    'profit/loss': 'profit' if results[i-1] > previous_close else 'loss',
                    'diff': int(results[i-1] - previous_close)
                } for i in range(1, days+1)
            }
            predictions['previous_close'] = previous_close
            predictions["date"] = datetime.datetime.now().strftime("%y%m%d")
            dict1 = {
                "stock": ticker,
                "predictions" : predictions
            }
            stock_movement.append(dict1)
            
        return stock_movement

    def generate(self) -> list:
        result = self._stock_movement()
        return result
        
if __name__ == '__main__':
    bs = BestStocks(extended_model_path='models_221211/')
    p = bs.generate()
    with open('Learningapp/best_stocks.json', 'w') as f:
        json.dump(p, f, indent=4)

            