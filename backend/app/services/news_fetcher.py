
import random
from datetime import datetime, timedelta
from typing import List, Optional
from abc import ABC, abstractmethod
from app.models.schemas import NewsArticle

class NewsProvider(ABC):
    @abstractmethod
    def fetch_news(self, ticker: str, days: int = 7) -> List[NewsArticle]:
        pass

class SimulatedNewsProvider(NewsProvider):
    def fetch_news(self, ticker: str, days: int = 7) -> List[NewsArticle]:
        bullish_templates = [
            "{ticker} beats earnings estimates by {percent}%",
            "{ticker} announces new strategic partnership with global tech giant",
            "Analysts upgrade {ticker} to 'Buy' citing strong growth",
            "{ticker} launches innovative new product line",
            "Market sentiment shifts positively for {ticker}"
        ]
        
        bearish_templates = [
            "{ticker} faces regulatory scrutiny over new policies",
            "{ticker} misses revenue targets for Q3",
            "Supply chain issues likely to impact {ticker} growth",
            "Competitor gains market share from {ticker}",
            "CEO of {ticker} announces unexpected departure"
        ]
        
        neutral_templates = [
            "{ticker} to hold annual shareholder meeting next week",
            "Market watch: {ticker} stays steady amidst volatility",
            "{ticker} releases annual sustainability report",
            "Industry outlook remains stable for {ticker} sector",
            "{ticker} confirms dividend payout date"
        ]
        
        articles = []
        company_name = ticker.split('.')[0]
        
        if "RELIANCE" in ticker:
            company_name = "Reliance Industries"
        elif "TCS" in ticker:
            company_name = "TCS"
        elif "SBIN" in ticker:
            company_name = "SBI"
        
        num_articles = random.randint(3, 6)
        current_time = datetime.now()
        
        for i in range(num_articles):
            sentiment_type = random.choice(["bullish", "bearish", "neutral"])
            
            if sentiment_type == "bullish":
                template = random.choice(bullish_templates)
                percent = random.randint(5, 20)
                title = template.format(ticker=company_name, percent=percent)
                sentiment_score = random.uniform(0.3, 0.9)
                sentiment_label = "Bullish"
                impact_score = random.randint(60, 95)
            elif sentiment_type == "bearish":
                template = random.choice(bearish_templates)
                title = template.format(ticker=company_name)
                sentiment_score = random.uniform(-0.9, -0.3)
                sentiment_label = "Bearish"
                impact_score = random.randint(50, 90)
            else:
                template = random.choice(neutral_templates)
                title = template.format(ticker=company_name)
                sentiment_score = random.uniform(-0.2, 0.2)
                sentiment_label = "Neutral"
                impact_score = random.randint(10, 40)
                
            pub_date = current_time - timedelta(days=random.randint(0, days), hours=random.randint(0, 23))
            
            article = NewsArticle(
                ticker=ticker,
                title=title,
                url=f"https://finance.yahoo.com/quote/{ticker}/news",
                published_date=pub_date,
                source=random.choice(["Financial Times", "Reuters", "Bloomberg", "Economic Times", "CNBC"]),
                summary=f"Detailed analysis of how {title.lower()} is affecting the market perception of {company_name}.",
                sentiment_score=sentiment_score,
                sentiment_label=sentiment_label,
                impact_score=impact_score,
                evidence="['Strong quarterly results', 'Positive analyst guidance', 'Sector tailwinds']" if sentiment_label == "Bullish" else "[]"
            )
            articles.append(article)
            
        articles.sort(key=lambda x: x.published_date, reverse=True)
        return articles

class NewsFetcher:
    """
    Service to fetch news articles for stocks.
    Delegates to a NewsProvider.
    """
    def __init__(self, provider: Optional[NewsProvider] = None):
        self.provider = provider or SimulatedNewsProvider()
    
    def get_news(self, ticker: str, days: int = 7) -> List[NewsArticle]:
        return self.provider.fetch_news(ticker, days)
