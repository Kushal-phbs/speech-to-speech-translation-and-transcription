"""API router registration."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["health"], summary="Check API health")
def health_check() -> dict[str, str]:
    """Return the service status without initializing model providers."""
    return {"status": "ok"}
