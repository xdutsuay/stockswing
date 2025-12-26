
from fastapi.testclient import TestClient

from datetime import datetime, timedelta
from app.models.db_models import StockPrice
from sqlmodel import Session

def test_predict_endpoint(client: TestClient, session: Session):
    # Seed data
    ticker = "TEST.NS"
    # Create 80 days of data
    for i in range(80):
        date = datetime.now() - timedelta(days=i)
        price = StockPrice(
            ticker=ticker,
            date=date,
            open=100.0 + i,
            high=105.0 + i,
            low=95.0 + i,
            close=102.0 + i,
            volume=1000
        )
        session.add(price)
    session.commit()

    # Mock NewsFetcher to avoid external calls and ensure consistent sentiment
    from unittest.mock import patch, MagicMock
    from app.models.schemas import NewsArticle
    from datetime import datetime

    mock_news_article = NewsArticle(
        ticker=ticker,
        title="Good News",
        url="http://test.com",
        published_date=datetime.now(),
        source="Test",
        summary="Good things happening",
        sentiment_score=0.9,
        sentiment_label="Bullish",
        impact_score=80,
        evidence="None"
    )

    with patch("app.api.routes.NewsFetcher") as MockFetcher:
        instance = MockFetcher.return_value
        instance.get_news.return_value = [mock_news_article]

        # This relies on the mock_predictor in conftest.py
        payload = {"ticker": ticker, "days": 7}
        response = client.post("/api/v1/predict", json=payload)
    
    # If 400, it means not enough data or sync failed. With 80 points, it should proceed to Predictor.
    assert response.status_code == 200
    data = response.json()
    assert data["ticker"] == ticker
    assert len(data["predictions"]) == 7
    assert data["trend"] == "Bullish"
    assert "data_loaded_at" in data
