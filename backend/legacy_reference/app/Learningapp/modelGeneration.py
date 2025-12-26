from modelCreation import PredictionModel
import pandas as pd


class NSEModelGen():
    NSE_TICKER: list = ['NESTLEIND.NS',
                        'SUNPHARMA.NS',
                        'ITC.NS',
                        'DRREDDY.NS',
                        'TITAN.NS',
                        'EICHERMOT.NS',
                        'SBIN.NS',
                        'BPCL.NS',
                        'INDUSINDBK.NS',
                        'HDFCBANK.NS',
                        'HINDUNILVR.NS',
                        'HDFCLIFE.NS',
                        'BRITANNIA.NS',
                        'HDFC.NS',
                        'BHARTIARTL.NS',
                        'ASIANPAINT.NS',
                        'SBILIFE.NS',
                        'HEROMOTOCO.NS',
                        'ICICIBANK.NS',
                        'CIPLA.NS',
                        'TATACONSUM.NS',
                        'POWERGRID.NS',
                        'DIVISLAB.NS',
                        'ADANIPORTS.NS',
                        'KOTAKBANK.NS',
                        'BAJAJ-AUTO.NS',
                        'JSWSTEEL.NS',
                        'APOLLOHOSP.NS',
                        'COALINDIA.NS',
                        'GRASIM.NS',
                        'NTPC.NS',
                        'M&M.NS',
                        'ADANIENT.NS',
                        'LT.NS',
                        'MARUTI.NS',
                        'AXISBANK.NS',
                        'TATAMOTORS.NS',
                        'BAJFINANCE.NS',
                        'TATASTEEL.NS',
                        'BAJAJFINSV.NS',
                        'RELIANCE.NS',
                        'ONGC.NS',
                        'ULTRACEMCO.NS',
                        'HINDALCO.NS',
                        'UPL.NS',
                        'TCS.NS',
                        'WIPRO.NS',
                        'INFY.NS',
                        'TECHM.NS',
                        'HCLTECH.NS']
    TICKER_DATASET_PATH: str = 'tickerData/'
    TICKER_MODEL_PATH: str = 'models/'

    def __init__(self, extended_data_path: str = '', extended_model_path: str = '', excluded: list = [], offset: int = 61, ) -> None:
        self.TICKER_DATASET_PATH = self.TICKER_DATASET_PATH + extended_data_path
        self.TICKER_MODEL_PATH = self.TICKER_MODEL_PATH + extended_model_path
        self.excluded = excluded
        self.offset = offset
        self.ticker_list = self.NSE_TICKER
        if self.excluded is not None:
            self.ticker_list = [
                ticker for ticker in self.NSE_TICKER if ticker not in self.excluded]

    def _generate_models(self) -> None:
        for ticker in self.ticker_list:
            print(f'Compiling and Fitting model for {ticker}')
            df = pd.read_csv(self.TICKER_DATASET_PATH + ticker + '.csv')
            df = df.dropna()
            pmt = PredictionModel(df, offset=self.offset)
            model = pmt.create_model()
            pmt.train_model(model)  # time consuming
            pmt.save_model(model, self.TICKER_MODEL_PATH + ticker + '.h5')

    def run(self) -> None:
        self._generate_models()


if __name__ == '__main__':
    # nse = NSEModelGen(
    #     extended_data_path='data_221211/',
    #     extended_model_path='models_221211/',
    # )
    # nse.run()
    pass
