from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import routes

from app.core.database import create_db_and_tables
from app.services.predictor import StockPredictor
import os

from app.services.scheduler import start_scheduler, stop_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB
    create_db_and_tables()
    
    # Load ML models
    print("Initializing Predictor...")
    model_path = "app/models/stock_model.h5"
    if not os.path.exists(model_path):
         model_path = os.path.abspath(os.path.join(os.getcwd(), "app/models/stock_model.h5"))
    
    predictor = StockPredictor(model_path)
    app.state.predictor = predictor

    # Start Scheduler
    start_scheduler(app)

    yield
    print("Shutting down...")
    stop_scheduler()

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to StockSwing API"}
