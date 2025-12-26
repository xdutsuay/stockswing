from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlmodel import Session
from app.core.database import get_session
from app.services.data_manager import DataManager
from app.models.schemas import StockDataPoint, PredictionResponse, PredictionRequest, HealthCheck, SearchResult
from app.services.predictor import StockPredictor
from starlette.requests import Request
from typing import List
from app.data.stock_tickers import search_tickers
from datetime import datetime

api_router = APIRouter()

@api_router.get("/health", response_model=HealthCheck)
def health_check():
    return {"status": "ok"}

@api_router.get("/search", response_model=List[SearchResult])
def search_stocks(q: str = "", limit: int = 10):
    """
    Search for stock tickers by symbol or name.
    Returns matching results for autocomplete.
    """
    results = search_tickers(q, limit)
    return results

@api_router.post("/sync/{ticker}")
def sync_ticker_data(ticker: str, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    dm = DataManager(session)
    # Sync in background to not block
    background_tasks.add_task(dm.sync_data, ticker)
    return {"message": f"Sync started for {ticker}"}

@api_router.get("/history/{ticker}", response_model=List[StockDataPoint])
def get_stock_history(ticker: str, session: Session = Depends(get_session)):
    dm = DataManager(session)
    df = dm.get_history(ticker, limit=730)  # Get last 2 years
    if df.empty:
        raise HTTPException(status_code=404, detail="No data found. Please sync first.")
    
    # Convert DataFrame to list of dicts
    result = []
    for _, row in df.iterrows():
        result.append(StockDataPoint(
            date=row['Date'],
            open=row['Open'],
            high=row['High'],
            low=row['Low'],
            close=row['Close'],
            volume=int(row['Volume'])
        ))
    return result

@api_router.post("/predict", response_model=PredictionResponse)
def predict_stock(request: PredictionRequest, req: Request, session: Session = Depends(get_session)):
    ticker = request.ticker
    days = request.days
    
    data_load_start = datetime.now()
    processing_steps = []
    
    dm = DataManager(session)
    df = dm.get_history(ticker, limit=730)  # Need at least 60, use 2 years for better accuracy
    
    if df.empty or len(df) < 60:
         # Auto-sync attempt
         processing_steps.append("Auto-syncing data from yfinance")
         dm.sync_data(ticker)
         df = dm.get_history(ticker, limit=730)
         if len(df) < 60:
            raise HTTPException(status_code=400, detail="Not enough data history to predict. Sync initiated, please try again.")
    
    data_loaded_at = datetime.now()
    processing_steps.append(f"Loaded {len(df)} historical data points")
    
    predictor: StockPredictor = req.app.state.predictor
    try:
        processing_steps.append(f"Preparing data with {predictor.timestep}-day window")
        processing_steps.append("Normalizing prices using MinMaxScaler")
        processing_steps.append(f"Generating {days}-day predictions using LSTM model")
        
        predictions = predictor.predict(df, days=days)
        
        processing_steps.append("Inverse transforming predictions to original scale")
        
        # Analyze trend
        trend, confidence = predictor.analyze_trend(df, predictions)
        processing_steps.append(f"Analyzed trend: {trend} (confidence: {confidence})")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    return PredictionResponse(
        ticker=ticker,
        predictions=predictions,
        unit="USD",
        last_updated=df.iloc[-1]['Date'],
        data_loaded_at=data_loaded_at,
        data_points_used=len(df),
        processing_steps=processing_steps,
        trend=trend,
        trend_confidence=confidence
    )
