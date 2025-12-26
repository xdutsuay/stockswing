from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class StockDataPoint(BaseModel):
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

class NewsArticle(BaseModel):
    ticker: str
    title: str
    url: str
    published_date: datetime
    source: str
    summary: Optional[str] = None
    sentiment_score: float = 0.0
    sentiment_label: str = "Neutral"
    impact_score: int = 0
    evidence: Optional[str] = None

class PredictionRequest(BaseModel):
    ticker: str
    days: int = 7

class PredictionResponse(BaseModel):
    ticker: str
    predictions: List[float]
    unit: str = "price"
    last_updated: datetime
    # New metadata fields
    data_loaded_at: datetime
    data_points_used: int
    processing_steps: List[str]
    trend: str  # "bullish", "bearish", or "neutral"
    trend_confidence: float  # 0.0 to 1.0

class SearchResult(BaseModel):
    symbol: str
    name: str
    exchange: str
    match_type: str  # "symbol" or "name"

class HealthCheck(BaseModel):
    status: str
