import uvicorn

from src.application import create_app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, port=8000, log_level="info")
