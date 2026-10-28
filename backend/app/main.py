"""FastAPI application entry point."""

import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import Settings, get_settings
from app.core.logging_config import configure_logging

logger = logging.getLogger(__name__)


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the API application without loading any speech models."""
    app_settings = settings or get_settings()
    configure_logging(app_settings.log_level)

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncIterator[None]:
        application.state.settings = app_settings
        logger.info("Starting speech translation API")
        try:
            yield
        finally:
            logger.info("Shutting down speech translation API")

    application = FastAPI(
        title="English ↔ Hindi Speech Translation API",
        description="Local-first speech translation and transcription service.",
        version="0.1.0",
        lifespan=lifespan,
    )
    application.include_router(router, prefix="/api")
    return application


app = create_app()
