import yfinance as yf
from sqlmodel import Session, select
from datetime import datetime
import pandas as pd
from app.models.db_models import StockPrice
import logging

logger = logging.getLogger(__name__)

class DataManager:
    def __init__(self, session: Session):
        self.session = session

    def get_history(self, ticker: str, limit: int = 100) -> pd.DataFrame:
        # Try local first
        statement = select(StockPrice).where(StockPrice.ticker == ticker).order_by(StockPrice.date.desc()).limit(limit)
        results = self.session.exec(statement).all()
        
        if not results or len(results) < limit: # Simple logic: if not enough data, fetch all
             # Actually, simpler: just sync if requested or missing. 
             # For 100% local, we should have a "Sync" button or auto-sync.
             pass

        # Convert to DataFrame
        data = [
            {
                "Date": r.date, 
                "Open": r.open, 
                "High": r.high, 
                "Low": r.low, 
                "Close": r.close, 
                "Volume": r.volume
            } for r in reversed(results)
        ]
        return pd.DataFrame(data)

    def sync_data(self, ticker: str, period: str = "2y"):
        logger.info(f"Syncing data for {ticker}...")
        tick = yf.Ticker(ticker)
        df = tick.history(period=period)
        
        # Save to DB
        count = 0
        for index, row in df.iterrows():
            # index is Date
            date_val = index.to_pydatetime() if hasattr(index, 'to_pydatetime') else index
            
            # Check if exists
            existing = self.session.exec(select(StockPrice).where(StockPrice.ticker == ticker, StockPrice.date == date_val)).first()
            if not existing:
                stock_price = StockPrice(
                    ticker=ticker,
                    date=date_val,
                    open=row['Open'],
                    high=row['High'],
                    low=row['Low'],
                    close=row['Close'],
                    volume=row['Volume']
                )
                self.session.add(stock_price)
                count += 1
        
        self.session.commit()
        logger.info(f"Synced {count} new records for {ticker}")
        return count
