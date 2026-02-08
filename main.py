import uvicorn
from src.routers import base_router
from fastapi import FastAPI

def main():
    app = FastAPI()

    app.include_router(base_router)

    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=5000
    )

if __name__ == "__main__":
    main()
