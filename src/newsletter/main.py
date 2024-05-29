from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from newsletter.presentation.api.endpoints.setup import setup_endpoints


def create_app() -> FastAPI:
    app = FastAPI(title="Newsletter", version="0.0.1", prefix="/api")

    origins = [
        "http://localhost",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    setup_endpoints(app)

    return app
