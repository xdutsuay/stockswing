import yfinance as yf
import pandas as pd
from app.Learningapp.tickers import Tickers

tickers = Tickers()


class HistoricalData:
    NSE_TICKER: list = tickers.NSE_TICKER

    def __init__(self, excluded: list = []) -> None:
        self.excluded = excluded
        self.ticker_list = self.NSE_TICKER
        if self.excluded is not None:
            self.ticker_list = [
                ticker for ticker in self.NSE_TICKER if ticker not in self.excluded
            ]

    def get_data(self) -> pd.DataFrame:
        data = yf.download(self.ticker_list, period="max", group_by="ticker")
        return data

    def get_recent_data(self) -> pd.DataFrame:
        data = yf.download(self.ticker_list, period="3mo", group_by="ticker")
        return data


def save_data(data: pd.DataFrame, name: str) -> None:
    data.to_csv(name)


if __name__ == "__main__":
    hd = HistoricalData()
    conjugated_data = hd.get_recent_data()
    for ticker in hd.ticker_list:
        print(len(conjugated_data[ticker].dropna()))
