from dataclasses import dataclass, field

from fastapi import APIRouter, status

healthcheck_router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@dataclass(frozen=True)
class OkStatus:
    status: str = field(default="OK")


OK_STATUS = OkStatus()


@healthcheck_router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="Health check endpoint",
    response_model=OkStatus,
    responses={
        status.HTTP_200_OK: {"description": "Successful Response"},
    }
)
async def get_status():
    """Health check endpoint"""
    return OK_STATUS
