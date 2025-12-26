from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class StockPrice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ticker: str = Field(index=True)
    date: datetime = Field(index=True)
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockPrediction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ticker: str = Field(index=True)
    predicted_date: datetime
    price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
