from fastapi import APIRouter
from app.routers.generate.service import check_in_db
from fastapi.responses import JSONResponse
from app.routers.generate.models import PredictedDataModel

generate = APIRouter(
    prefix="/generate",
    tags=["predict"],
    responses={404: {"description": "Not found"}},
)


@generate.get("/")
async def generate_():
    data = await check_in_db()
    print(data, "THESE DATAS")
    return [PredictedDataModel(**data) for data in data]
