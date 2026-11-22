from functools import cache
from ipaddress import IPv4Address
from typing import Literal, Self
from urllib.parse import quote
from zoneinfo import ZoneInfo

from pydantic import (
    AnyHttpUrl,
    Field,
    RedisDsn,
    SecretStr,
    field_validator,
    model_validator,
)
from pydantic.types import Base64UrlEncoder
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_UPSTREAM_SCOPES = frozenset({"openid"})
DEFAULT_UPSTREAM_TIMEZONE = ZoneInfo("Europe/Berlin")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        frozen=True,
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
        hide_input_in_errors=True,
    )

    server_name: str = Field(default="HISinOne", min_length=1)
    server_base_url: AnyHttpUrl
    server_host: IPv4Address
    server_port: int = Field(ge=1, le=65535)

    upstream_base_url: str
    upstream_api_base_path: str = "api/v1"
    upstream_authorization_path: str = "pages/oauth.faces"
    upstream_token_path: str = "api/v1/cs/psv/oauth/token"
    upstream_userinfo_path: str = "api/v1/cs/psv/oauth/userinfo"
    upstream_client_id: str = Field(min_length=1)
    upstream_client_secret: SecretStr = Field(min_length=64, exclude=True)
    upstream_timezone: ZoneInfo = DEFAULT_UPSTREAM_TIMEZONE

    oauth_encryption_key: SecretStr = Field(exclude=True)
    oauth_signing_key: SecretStr = Field(min_length=32, exclude=True)
    oauth_allowed_client_redirect_uris: list[str] | None = None
    oauth_available_scopes: frozenset[str] = DEFAULT_UPSTREAM_SCOPES
    oauth_required_scopes: frozenset[str] = DEFAULT_UPSTREAM_SCOPES
    oauth_mcp_access_token_expiry_seconds: int | None = Field(default=None, gt=0)
    oauth_fallback_access_token_expiry_seconds: int | None = Field(default=None, gt=0)

    redis_host: IPv4Address = IPv4Address("127.0.0.1")
    redis_port: int = Field(default=6379, ge=1, le=65535)
    redis_db: int = Field(default=0, ge=0)
    redis_scheme: Literal["redis", "rediss"] = "redis"
    redis_username: str | None = None
    redis_password: SecretStr | None = Field(default=None, exclude=True)

    @model_validator(mode="after")
    def validate_oauth_scopes(self) -> Self:
        if "openid" not in self.oauth_required_scopes:
            raise ValueError("OAUTH_REQUIRED_SCOPES must include openid")

        if missing := self.oauth_required_scopes - self.oauth_available_scopes:
            raise ValueError(
                f"OAUTH_AVAILABLE_SCOPES must include {', '.join(sorted(missing))}"
            )

        return self

    @field_validator("oauth_encryption_key")
    @classmethod
    def validate_fernet_key(cls, value: SecretStr) -> SecretStr:
        secret = value.get_secret_value()

        decoded = Base64UrlEncoder.decode(encoded := secret.encode())
        if len(decoded) != 32 or Base64UrlEncoder.encode(decoded) != encoded:
            raise ValueError("Expected a 32-byte key in padded URL-safe Base64")

        return value

    @property
    def redis_dsn(self) -> RedisDsn:
        return RedisDsn.build(
            scheme=self.redis_scheme,
            host=str(self.redis_host),
            port=self.redis_port,
            path=str(self.redis_db),
            username=(
                quote(self.redis_username, safe="") if self.redis_username else None
            ),
            password=(
                quote(self.redis_password.get_secret_value(), safe="")
                if self.redis_password
                else None
            ),
        )

    @property
    def upstream_api_base_url(self) -> AnyHttpUrl:
        return AnyHttpUrl(f"{self.upstream_base_url}/{self.upstream_api_base_path}")

    @property
    def upstream_authorization_endpoint(self) -> AnyHttpUrl:
        return AnyHttpUrl(
            f"{self.upstream_base_url}/{self.upstream_authorization_path}"
        )

    @property
    def upstream_token_endpoint(self) -> AnyHttpUrl:
        return AnyHttpUrl(f"{self.upstream_base_url}/{self.upstream_token_path}")

    @property
    def upstream_userinfo_endpoint(self) -> AnyHttpUrl:
        return AnyHttpUrl(f"{self.upstream_base_url}/{self.upstream_userinfo_path}")


@cache
def load_settings() -> Settings:
    return Settings.model_validate({})
