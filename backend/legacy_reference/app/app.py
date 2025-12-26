from fastapi import FastAPI

# from app.database.database import connect_db,db
from app.config import AppConfig


def register_routes(application: FastAPI) -> None:
    from app.routers.predict.route import predict
    from app.routers.generate.route import generate

    application.include_router(predict)
    application.include_router(generate)


def create_application(config=AppConfig()) -> FastAPI:
    application = FastAPI()

    register_routes(application)
    # connect_db(config)
    # print(db)
    return application
