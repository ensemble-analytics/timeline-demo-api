from fastapi import FastAPI
from .routes import timeline


def create_app() -> FastAPI:
    app = FastAPI(title="Ensemble Analytics")
    app.include_router(timeline.router)

    @app.get("/")
    def root():
        return {"message": "Ensemble Analytics"}

    return app
