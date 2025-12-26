
from fastapi.testclient import TestClient

def test_get_news(client: TestClient):
    ticker = "RELIANCE.NS"
    response = client.get(f"/api/v1/news/{ticker}")
    
    assert response.status_code == 200
    articles = response.json()
    assert isinstance(articles, list)
    assert len(articles) >= 3
    
    first_article = articles[0]
    assert "title" in first_article
    assert "sentiment_label" in first_article
    assert first_article["ticker"] == ticker
