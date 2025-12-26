import uvicorn

from app import app

application = app.create_application()

if __name__ == "__main__":
    #conda activate faststock
    uvicorn.run(application, host="localhost", port=8000, reload=True)
