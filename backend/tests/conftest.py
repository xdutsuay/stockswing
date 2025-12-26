
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from unittest.mock import MagicMock, patch

from app.main import app
from app.core.database import get_session
from app.main import app
from app.core.database import get_session
from app.models.db_models import StockPrice, StockPrediction # Explicit import

from sqlalchemy.pool import StaticPool

# Use in-memory SQLite for tests
sqlite_url = "sqlite:///:memory:"
engine = create_engine(
    sqlite_url, 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)

@pytest.fixture(name="session")  
def session_fixture():  
    import sys
    print(f"DEBUG: Registered tables: {SQLModel.metadata.tables.keys()}", file=sys.stderr)
    SQLModel.metadata.create_all(engine)  
    with Session(engine) as session:  
        yield session  
    SQLModel.metadata.drop_all(engine)  

@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session  

    app.dependency_overrides[get_session] = get_session_override  
    
    # Mock the predictor state to avoid loading heavy models
    mock_predictor = MagicMock()
    mock_predictor.predict.return_value = [100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0]
    mock_predictor.analyze_trend.return_value = ("Bullish", 0.85)
    app.state.predictor = mock_predictor

    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()
