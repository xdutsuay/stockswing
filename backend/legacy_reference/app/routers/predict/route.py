from fastapi import APIRouter

predict = APIRouter(
    prefix="/predict",
    tags=["predict"],
    responses={404: {"description": "Not found"}},
)


@predict.get("/")
async def read_predict():
    return {"Hello": "World"}
