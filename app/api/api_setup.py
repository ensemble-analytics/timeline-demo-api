from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import timeline


def create_app() -> FastAPI:
    app = FastAPI(title="Ensemble Analytics")

    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(timeline.router)

    @app.get("/")
    def root():
        return {"message": "Ensemble Analytics"}

    return app
