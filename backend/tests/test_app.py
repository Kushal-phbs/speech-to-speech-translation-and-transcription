"""Tests for FastAPI application initialization."""

from fastapi.testclient import TestClient

from app.core.config import Settings
from app.main import create_app


def test_app_exposes_openapi_docs_and_api_router() -> None:
    app = create_app(Settings(_env_file=None))

    assert app.title == "English ↔ Hindi Speech Translation API"
    assert app.docs_url == "/docs"
    assert app.openapi_url == "/openapi.json"
    assert app.router.routes


def test_app_lifespan_starts_and_shuts_down_without_loading_models() -> None:
    app = create_app(Settings(_env_file=None))

    with TestClient(app) as client:
        response = client.get("/docs")

        assert response.status_code == 200
        assert app.state.settings.device == "auto"
        assert not hasattr(app.state, "models")
