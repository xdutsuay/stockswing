import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
import datetime


class PredictionModel():
    def __init__(self, data, timestep: int = 60, offset: int = 0):
        self.data = data
        self.offset = offset
        self.timestep = timestep
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def create_model(self):
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True,
                       input_shape=(self.timestep, 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def train_model(self, model):
        training_set = self.data.iloc[:, 3:4].values
        training_set = training_set[:-self.offset] if self.offset > 0 else training_set
        training_set = self.scaler.fit_transform(training_set)
        X_train = []
        y_train = []
        for i in range(self.timestep, len(training_set)):
            X_train.append(training_set[i-self.timestep:i, 0])
            y_train.append(training_set[i, 0])
        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)
        return model

    def save_model(self, model, name: str):
        model.save(name)


if __name__ == '__main__':
    pass
    # data = pd.read_csv('SBIN.NS.csv')
    # data = data.dropna()
    # data['Date'] = pd.to_datetime(data['Date'])
    # data = data[data['Date'] < datetime.datetime(2022, 1, 1)]
    # pm = PredictionModel(data)
    # model = pm.create_model()
    # model = pm.train_model(model)
    # model.save('test_model.h5')
