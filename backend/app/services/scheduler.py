
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sqlmodel import Session, select
from app.core.database import engine
from app.models.db_models import StockPrice, StockPrediction
from app.services.data_manager import DataManager
from app.services.predictor import StockPredictor
import logging

logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler()

async def auto_update_job(app_state):
    """
    Background job to sync data and run predictions for all tickers.
    """
    logger.info("Starting background auto-update job...")
    
    with Session(engine) as session:
        # Get distinct tickers from database (or a fixed list if you have one)
        # For this prototype, we'll scan the StockPrice table for unique tickers
        statement = select(StockPrice.ticker).distinct()
        results = session.exec(statement).all()
        tickers = list(results)
        
        logger.info(f"Found {len(tickers)} tickers to update: {tickers}")
        
        dm = DataManager(session)
        predictor = app_state.predictor
        
        for ticker in tickers:
            try:
                logger.info(f"Updating {ticker}...")
                
                # 1. Sync Data
                dm.sync_data(ticker)
                
                # 2. Get History
                df = dm.get_history(ticker, limit=730)
                if df.empty or len(df) < 60:
                    logger.warning(f"Not enough data for {ticker} to predict.")
                    continue
                
                # 3. Predict (using 0 sentiment for auto-run, or could fetch news)
                # For efficiency/API limits, we might skip news fetching in background for now
                predictions = predictor.predict(df, days=7, sentiment_score=0.0)
                trend, confidence = predictor.analyze_trend(df, predictions)
                
                # 4. Save Prediction (Need a table for this, or just log for now)
                # Currently we don't have a 'StockPrediction' table in db_models.py used for persistence
                # So we will just log it. In a real app, we would save to DB.
                logger.info(f"Generated prediction for {ticker}: {trend} ({confidence})")
                
            except Exception as e:
                logger.error(f"Failed to update {ticker}: {e}")

    logger.info("Background auto-update job completed.")

def start_scheduler(app):
    # Run every 12 hours
    scheduler.add_job(
        auto_update_job, 
        IntervalTrigger(hours=12), 
        args=[app.state],
        id="auto_update",
        replace_existing=True
    )
    scheduler.start()
    logger.info("Scheduler started.")

def stop_scheduler():
    scheduler.shutdown()
    logger.info("Scheduler stopped.")
