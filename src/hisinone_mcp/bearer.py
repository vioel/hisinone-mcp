from urllib.request import parse_http_list

from pydantic import BaseModel, ValidationError


class _OAuthError(BaseModel):
    error: str


def _bearer_error_from_header(header: str) -> str | None:
    scheme, _, params = header.partition(" ")
    if scheme.lower() != "bearer":
        return None

    for param in parse_http_list(params):
        key, _, value = param.partition("=")
        if key.strip().lower() == "error":
            return value.strip().strip('"')

    return None


def oauth_error(header: str, body: bytes) -> str | None:
    if (code := _bearer_error_from_header(header)) is not None:
        return code
    try:
        error = _OAuthError.model_validate_json(body)
        return error.error
    except ValidationError:
        return None
