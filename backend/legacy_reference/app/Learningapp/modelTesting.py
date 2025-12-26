from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime
import matplotlib.pyplot as plt
import json
from tickers import Tickers

tickers = Tickers()


class PmTesting():
    '''
    Testing the model created using Model Creation
    '''

    def __init__(self, model, data, timestep: int = 60) -> None:
        self.model = model
        self.data = data
        self.timestep = timestep
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def test_model(self):
        '''
        Testing the model
        '''
        test_set = self.data.iloc[:, 3:4].values
        test_set = self.scaler.fit_transform(test_set)
        X_test = []
        y_test = []
        for i in range(self.timestep, len(test_set)):
            X_test.append(test_set[i-self.timestep:i, 0])
            y_test.append(test_set[i, 0])
        X_test, y_test = np.array(X_test), np.array(y_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        predicted_stock_price = self.model.predict(X_test)
        predicted_stock_price = self.scaler.inverse_transform(
            predicted_stock_price)
        return predicted_stock_price

    def model_accuracy(self, predicted_stock_price, offset: int = 0) -> float:
        '''
        Calculating the accuracy of the model
        '''
        test_set = self.data.iloc[:, 3:4].values
        test_set = test_set[self.timestep:, :]
        accuracy = 0
        for i in range(len(predicted_stock_price)):
            accuracy += abs(
                (predicted_stock_price[i] - test_set[i])/test_set[i])
        accuracy = (1 - accuracy/len(predicted_stock_price))*100
        accuracy = accuracy[0]
        return accuracy

    def real_v_predicted_graph(self, predicted_stock_price):
        '''
        Plotting the graph of the real stock price vs predicted stock price
        '''
        test_set = self.data.iloc[:, 3:4].values
        test_set = test_set[self.timestep:, :]
        plt.plot(test_set, color='red', label='Real Stock Price')
        plt.plot(predicted_stock_price, color='blue',
                 label='Predicted Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()


class TickerTesting():
    NSETICKER: list = tickers.NSE_TICKER
    TICKER_DATASET_PATH: str = 'tickerData/'
    TICKER_MODEL_PATH: str = 'models/'

    def __init__(self, extended_data_path: str = '', extended_model_path: str = '', excluded: list = [], offset: int = 61, graph: bool = False) -> None:
        self.TICKER_DATASET_PATH = self.TICKER_DATASET_PATH + extended_data_path
        self.TICKER_MODEL_PATH = self.TICKER_MODEL_PATH + extended_model_path
        self.excluded = excluded
        self.offset = offset+1
        self.NSETICKER = [
            ticker for ticker in self.NSETICKER if ticker not in self.excluded]
        self.graph = graph

    def _test_models(self) -> dict:
        '''
        Testing the models
        if graph is True, it will save the graph of the real stock price vs predicted stock price
        '''
        accuracy = {}
        for ticker in self.NSETICKER:
            data = pd.read_csv(
                self.TICKER_DATASET_PATH+f'{ticker}.csv')
            data = data[-self.offset:]
            model = load_model(
                self.TICKER_MODEL_PATH+f'{ticker}.h5')
            pmt = PmTesting(model, data)
            predicted_stock_price = pmt.test_model()
            accuracy[ticker] = pmt.model_accuracy(
                predicted_stock_price)
            # print(accuracy, accuracy[ticker])
        return dict(accuracy)

    def run_and_log(self) -> None:
        '''
        Running the model and logging the accuracy of the model
        '''
        accuracy = self._test_models()
        with open(f'{self.TICKER_MODEL_PATH}accuracy.json', 'w') as f:
            json.dump(accuracy, f)


if __name__ == '__main__':
    # data = pd.read_csv('SBIN.NS.csv')
    # data['Date'] = pd.to_datetime(data['Date'])
    # data = data[data['Date'] > datetime.datetime(2022, 1, 1)]
    # model = load_model(f'test_model.h5')
    # pmt = PmTesting(model, data)
    # predicted_stock_price = pmt.test_model()
    # print(predicted_stock_price)
    # accuracy = pmt.model_accuracy(predicted_stock_price)
    # print(accuracy)
    # pmt.real_v_predicted_graph(predicted_stock_price)
    ttt = TickerTesting(
        extended_data_path='data_221211/', extended_model_path='models_221211/'
    )
    ttt.run_and_log()
