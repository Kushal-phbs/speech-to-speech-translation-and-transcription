"""Application logging configuration."""

import logging


def configure_logging(level: str) -> None:
    """Configure standard-library logging for the application."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
