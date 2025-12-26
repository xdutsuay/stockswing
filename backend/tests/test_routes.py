
from fastapi.testclient import TestClient
from sqlmodel import Session
from datetime import datetime
from app.models.db_models import StockPrice

def test_health_check(client: TestClient):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_search_stocks(client: TestClient):
    # Depending on implementation of search_tickers, we test for a known stock
    response = client.get("/api/v1/search?q=REL&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Ideally search_tickers searches a static list or DB. 
    # If static, we expect results.

def test_get_stock_history_404(client: TestClient):
    response = client.get("/api/v1/history/UNKNOWN_TICKER")
    assert response.status_code == 404
    assert response.json()["detail"] == "No data found. Please sync first."

def test_get_stock_history_success(client: TestClient, session: Session):
    # Seed data
    ticker = "TEST.NS"
    price = StockPrice(
        ticker=ticker,
        date=datetime(2023, 1, 1),
        open=100.0,
        high=110.0,
        low=95.0,
        close=105.0,
        volume=1000
    )
    session.add(price)
    session.commit()
    
    response = client.get(f"/api/v1/history/{ticker}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["close"] == 105.0
