from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Dict, Any


class PredictedDataModel(BaseModel):
    stock: str
    predictions: Dict[str, Any]
