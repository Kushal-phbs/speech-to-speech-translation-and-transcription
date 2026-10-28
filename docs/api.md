# API

The FastAPI server provides interactive documentation at `/docs` and an
OpenAPI schema at `/openapi.json`.

## Health

`GET /api/health` reports whether the API process is running. It does not load
or download speech models.

Successful response (`200 OK`):

```json
{
  "status": "ok"
}
```

Run the API tests from the repository root with `python -m pytest`. These tests
use FastAPI's in-process test client and do not require model downloads or a
GPU.
