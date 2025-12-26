from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class StockPrediction():

    def __init__(self, model, data, timestep: int = 60):
        self.model = model
        self.data = data
        self.timestep = timestep
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def predict(self, data):
        if not self.check_unit_data_shape(data):
            raise ValueError('data should be in shape of (1, timestep, 1)')
        prediction = self.model.predict(data)
        return prediction

    def check_unit_data_shape(self, data) -> bool:
        '''Check the shape of the data'''
        return data.shape == (1, self.timestep, 1)

    def daily_prediction(self, daily_data, inv_transform: bool = True):
        '''daily_data should be in shape of (1, timestep, 1)'''
        if not self.check_unit_data_shape(daily_data):
            raise ValueError('data should be in shape of (1, timestep, 1)')
        prediction = self.predict(daily_data)
        if not inv_transform:
            return prediction
        prediction = self.scaler.inverse_transform(prediction)
        return prediction

    def weekly_prediction(self, daily_data):
        '''daily prediction should be included in daily data to predict weekly data'''
        if not self.check_unit_data_shape(daily_data):
            raise ValueError('data should be in shape of (1, timestep, 1)')
        weekly_data = []
        i = 0
        while i < 5:
            lst_input = [x[0] for x in daily_data[0]]
            p = self.daily_prediction(daily_data, inv_transform=False)
            x = lst_input[1:]
            x.append(p[0].tolist()[0])
            weekly_data.append(self.scaler.inverse_transform(p))
            daily_data = np.array(x).reshape(1, self.timestep, 1)
            i += 1
        return np.array(weekly_data).flatten().reshape(5, 1)

    def run_daily(self):
        test_set = self.data.iloc[-60:, 3:4].values
        test_set = self.scaler.fit_transform(test_set)
        test_set = np.reshape(test_set, (1, self.timestep, 1))
        return self.daily_prediction(test_set)

    def continuous_weekly_prediction(self):
        test_set = self.data.iloc[-60:, 3:4].values
        test_set = self.scaler.fit_transform(test_set)
        test_set = np.reshape(test_set, (1, self.timestep, 1))
        return self.weekly_prediction(test_set)

    def long_prediction(self, range):
        test_set = self.data.iloc[-60:, 3:4].values
        test_set = self.scaler.fit_transform(test_set)
        test_set = np.reshape(test_set, (1, self.timestep, 1))
        long_data = []
        i = 0
        while i < range:
            lst_input = [x[0] for x in test_set[0]]
            p = self.daily_prediction(test_set, inv_transform=False)
            x = lst_input[1:]
            x.append(p[0].tolist()[0])
            long_data.append(self.scaler.inverse_transform(p))
            test_set = np.array(x).reshape(1, self.timestep, 1)
            i += 1
        return np.array(long_data).flatten().reshape(range, 1)

    def long_prediction_graph(self, range):
        long_data = self.long_prediction(range)
        plt.plot(long_data, color='red', label='Predicted Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()

    def real_data_graph(self, real_data):
        '''real_data should be in shape of (60, 1)'''
        plt.plot(real_data, color='blue', label='Real Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()

    def weekly_prediction_graph(self, weekly_data):
        '''weekly_data should be in shape of (5, 1)'''
        if not weekly_data.shape == (5, 1):
            raise ValueError('data should be in shape of (5, 1)')
        plt.plot(weekly_data, color='red', label='Predicted Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()

    def real_week_data_graph(self, real_data):
        '''real_data should be in shape of (5, 1)'''
        if not real_data.shape == (5, 1):
            raise ValueError('data should be in shape of (5, 1)')
        plt.plot(real_data, color='blue', label='Real Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    from tensorflow.keras.models import load_model
    model = load_model('test_model.h5')
    df = pd.read_csv('SBIN.NS.csv')
    df = df.dropna()
    df_test = df.iloc[:-59]
    # print(df.iloc[-61:-54].values)
    # print(len(df_test))
    sp = StockPrediction(model, df_test)
    # w_result = sp.continuous_weekly_prediction()
    # print([x.flatten() for x in w_result])
    # print('tomorrows prediction is: ', sp.run_daily().flatten()[0])
    # print(sp.run_daily())
    print(sp.long_prediction(5).flatten())
    # print(sp.continuous_weekly_prediction())
