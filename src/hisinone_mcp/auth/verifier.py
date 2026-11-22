import httpx2
from fastmcp.server.auth import AccessToken, TokenVerificationError, TokenVerifier
from pydantic import BaseModel, Field, ValidationError

from hisinone_mcp.bearer import oauth_error


class InsufficientScope(TokenVerificationError):
    """HISinOne explicitly denied access to UserInfo."""


class UserInfo(BaseModel):
    sub: str = Field(min_length=1, pattern=r"\S")


class HisinoneTokenVerifier(TokenVerifier):
    def __init__(
        self,
        *,
        http: httpx2.AsyncClient,
        userinfo_endpoint: str,
        client_id: str,
        required_scopes: list[str],
    ) -> None:
        super().__init__(required_scopes=required_scopes)

        self.http = http
        self.userinfo_endpoint = userinfo_endpoint
        self.client_id = client_id

    async def get_subject(self, token: str) -> str | None:
        try:
            response = await self.http.get(
                self.userinfo_endpoint,
                headers={"Authorization": f"Bearer {token}"},
            )
        except httpx2.HTTPError:
            raise TokenVerificationError("UserInfo unavailable") from None

        if response.status_code == 403:
            raise InsufficientScope("HISinOne denied access to UserInfo")

        if response.status_code in {400, 401}:
            code = oauth_error(
                response.headers.get("WWW-Authenticate", ""), response.content
            )
            if code == "insufficient_scope":
                raise InsufficientScope("HISinOne denied access to UserInfo")

            if code == "invalid_token" or (
                response.status_code == 401 and code is None
            ):
                return None

        if response.status_code != 200:
            raise TokenVerificationError("UserInfo unavailable")

        try:
            user = UserInfo.model_validate_json(response.content)
            return user.sub
        except ValidationError:
            raise TokenVerificationError("Invalid UserInfo response") from None

    async def verify_token(self, token: str) -> AccessToken | None:
        subject = await self.get_subject(token)

        if subject is None:
            return None

        return AccessToken(
            token=token, subject=subject, client_id=self.client_id, scopes=[]
        )
