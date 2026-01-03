
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "X-API-Key"
API_KEYS = {"research_key": "researcher", "review_key": "reviewer"}
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def authenticate(api_key: str = Security(api_key_header)) -> str:
    if api_key in API_KEYS:
        return API_KEYS[api_key]
    raise HTTPException(status_code=403, detail="Invalid API key")
