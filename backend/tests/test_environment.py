"""Checks for the lightweight development environment."""

import sys

import fastapi
import httpx
import pydantic
import pytest
import uvicorn


def test_supported_python_and_core_dependencies() -> None:
    assert sys.version_info[:2] == (3, 11)
    assert fastapi.__version__
    assert uvicorn.__version__
    assert pydantic.__version__
    assert pytest.__version__
    assert httpx.__version__
