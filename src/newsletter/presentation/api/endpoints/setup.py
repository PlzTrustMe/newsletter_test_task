from fastapi import FastAPI

from .default import default_router
from .healthcheck import healthcheck_router
from .newsletter import newsletter_router


def setup_endpoints(app: FastAPI) -> None:
    app.include_router(default_router)
    app.include_router(healthcheck_router)
    app.include_router(newsletter_router)
