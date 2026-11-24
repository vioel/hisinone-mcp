# Set up the MCP server

The MCP process runs on the host. Redis stores OAuth state. HISinOne supplies the login page and the research data.

## Prepare the local environment

1. Register the confidential client in HISinOne. Keep its **Client-Key** and **Client-Secret** for the server configuration. [HISinOne setup](oauth.md)
2. Start Redis. Keep the Redis password for the next section. [Redis setup](../infrastructure/README.md)
3. Open a terminal in the repository root.
4. Install the locked Python dependencies with uv. The project requires Python 3.13 or later.

   ```sh
   uv sync --locked
   ```

5. Create the server's settings file. This command preserves an existing file.

   ```sh
   cp -n .env.example .env
   ```

## Set the local values

1. Set these entries in the root `.env` for the development installation. Include only the research scopes assigned to your HISinOne client.

   ```dotenv
   SERVER_BASE_URL=http://127.0.0.1:8000
   SERVER_HOST=127.0.0.1
   SERVER_PORT=8000
   UPSTREAM_BASE_URL=http://desktop:8080/qisserver
   OAUTH_REQUIRED_SCOPES=["openid"]
   OAUTH_AVAILABLE_SCOPES=["openid","fs.res.projects:read","fs.res.publications:read","fs.res.patents:read","fs.res.research-infrastructures:read"]
   ```

2. Set `UPSTREAM_CLIENT_ID` to the HISinOne **Client-Key**.
3. Set `UPSTREAM_CLIENT_SECRET` to the matching **Client-Secret**. The server requires at least 64 characters.
4. Copy `REDIS_PASSWORD` from `infrastructure/.env` into the root `.env`.
5. Generate a separate signing key for `OAUTH_SIGNING_KEY`. The server requires at least 32 characters.

   ```sh
   openssl rand -hex 32
   ```

6. Generate a Fernet key for `OAUTH_ENCRYPTION_KEY`. Save the entire output, including the final `=`.

   ```sh
   uv run python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'
   ```

Keep both OAuth keys across restarts. Use the same keys on all replicas. Losing the encryption key makes stored registrations and grants unreadable. Replacing the signing key invalidates existing MCP tokens and consent cookies.

## Start and check the server

1. Start the server from the repository root.

   ```sh
   uv run hisinone-mcp
   ```

   For development with automatic reload, use this command instead.

   ```sh
   uv run uvicorn hisinone_mcp.app:create_app --factory --reload --host 127.0.0.1 --port 8000
   ```

2. In another terminal, check the protected endpoint.

   ```sh
   curl -sS -D - -o /dev/null -X POST http://127.0.0.1:8000/mcp
   ```

   Expect HTTP 401 and a `WWW-Authenticate` header with a `resource_metadata` URL. This check reaches the server before sign-in.

3. Complete a browser sign-in and run a tool to check the connection to HISinOne. [First project lookup](user-guide.md#connect-with-mcp-inspector)

To stop a foreground server, press **Ctrl+C**.

## Settings reference

The server reads `.env` from its working directory. Environment variables take precedence. Empty settings use their defaults. Restart the process after you change a setting. [Application settings](../src/hisinone_mcp/settings.py) · [Example file](../.env.example)

### Server and upstream addresses

| Setting | Default or requirement | Use |
| --- | --- | --- |
| `SERVER_NAME` | `HISinOne` | Name shown to MCP clients. |
| `SERVER_BASE_URL` | Required | Browser-accessible base URL of the MCP server. Register its `/auth/callback` in HISinOne. |
| `SERVER_HOST`, `SERVER_PORT` | Both required | IPv4 listening address and port (1–65535). Direct Uvicorn launches use the address and port in their command. |
| `FASTMCP_STREAMABLE_HTTP_PATH` | `/mcp` | FastMCP transport path. A custom path changes the client connection URL. The HISinOne callback stays at `/auth/callback`. |
| `UPSTREAM_BASE_URL` | Required | HISinOne installation root. Omit the trailing slash. Use paths without a leading slash below. |
| `UPSTREAM_API_BASE_PATH` | `api/v1` | Research API base path. |
| `UPSTREAM_AUTHORIZATION_PATH` | `pages/oauth.faces` | Browser authorization page. |
| `UPSTREAM_TOKEN_PATH` | `api/v1/cs/psv/oauth/token` | Token exchange endpoint. |
| `UPSTREAM_USERINFO_PATH` | `api/v1/cs/psv/oauth/userinfo` | Identity check for each protected request. |
| `UPSTREAM_TIMEZONE` | `Europe/Berlin` | IANA time zone of the HISinOne application. Set it to the upstream JVM's zone. |

Use HTTPS for both the public server URL and the upstream installation in a deployment. The local HTTP callback assumes the browser can reach the MCP server at its own loopback address. [FastMCP transport settings](https://gofastmcp.com/docs/more/settings#transport--http) · [Date fields](tool-interface.md#calendar-dates)

### OAuth settings

| Setting | Value and effect |
| --- | --- |
| `UPSTREAM_CLIENT_ID`, `UPSTREAM_CLIENT_SECRET` | Credentials of the confidential client registered in HISinOne. |
| `OAUTH_SIGNING_KEY` | Stable secret for FastMCP token signing. |
| `OAUTH_ENCRYPTION_KEY` | A 32-byte Fernet key in canonical, padded URL-safe Base64 (44 characters). Protects OAuth records in Redis. |
| `OAUTH_AVAILABLE_SCOPES` | JSON array of scopes the server advertises. Defaults to `["openid"]`. |
| `OAUTH_REQUIRED_SCOPES` | JSON array of scopes every protected request needs. Defaults to `["openid"]`. Include `openid` and make every required scope available. |
| `OAUTH_MCP_ACCESS_TOKEN_EXPIRY_SECONDS` | Optional positive number of seconds. Leave empty to inherit the upstream lifetime. Without an upstream refresh token, FastMCP caps an override at that lifetime. |
| `OAUTH_FALLBACK_ACCESS_TOKEN_EXPIRY_SECONDS` | Optional positive number of seconds for grants that omit `expires_in`. FastMCP otherwise uses 365 days without a refresh token or one hour with one. |
| `OAUTH_ALLOWED_CLIENT_REDIRECT_URIS` | Optional JSON array of downstream callback patterns. For example, `["https://client.example.org/oauth/callback"]`. An empty array blocks every downstream callback. |

An upstream `expires_in` of zero or less causes FastMCP to return `invalid_grant` at redemption. The fallback applies when HISinOne omits the field. [Token lifetime tests](../tests/test_oauth.py)

By default, the proxy checks each registered MCP client's callback. Loopback ports can vary. Configured patterns apply across dynamically registered clients. Clearing the setting restores registration-specific checks after restart. HISinOne separately requires the exact upstream callback URL. [FastMCP redirect validation](https://gofastmcp.com/docs/servers/auth/oauth-proxy#redirect-uri-validation)

### Redis settings

| Setting | Default | Use |
| --- | --- | --- |
| `REDIS_HOST`, `REDIS_PORT` | `127.0.0.1`, `6379` | IPv4 address and port. |
| `REDIS_DB` | `0` | Database number. |
| `REDIS_SCHEME` | `redis` | Use `rediss` for TLS. |
| `REDIS_USERNAME`, `REDIS_PASSWORD` | Empty | Enter the original credentials. The server URL-encodes them when it builds the connection URL. Local Compose requires the password. |

### Migrate an older settings file

1. Rename `MCP_` keys to `SERVER_` and `HISINONE_` keys to `UPSTREAM_`. Use one underscore after the prefix.
2. Set `SERVER_HOST` and `SERVER_PORT` explicitly.
3. Replace the full HISinOne endpoint URLs with `UPSTREAM_BASE_URL` and any custom paths.
4. Remove the old upstream HTTP timeout setting.
5. Split `REDIS_DSN` into the Redis settings above. Decode percent escapes before you enter the username or password.

## Diagnose a connection problem

An HTTP 401 before sign-in is the expected response from `/mcp`. If a valid session fails, check Redis and the UserInfo endpoint. A UserInfo permission denial returns HTTP 403. A verification outage normally returns HTTP 503. Some Redis read failures can produce HTTP 401 during grant lookup. [How the proxy verifies a request](dev-findings.md#oauth-and-token-lifetime)

To see which scopes a client can request, read the authorization server metadata.

```sh
curl -fsS http://127.0.0.1:8000/.well-known/oauth-authorization-server
```

`scopes_supported` lists the available scopes. The HTTP 401 challenge lists the required scopes. Inspector's **OAuth Details** shows the scopes HISinOne granted for the current connection.

For more detail, set `FASTMCP_LOG_LEVEL=DEBUG` in the server environment. Add `--log-level debug` to the Uvicorn command for Uvicorn diagnostics. Keep access and debug logs private. Callback URLs can contain authorization codes. FastMCP can also show upstream error details to the browser. [Uvicorn logging](https://uvicorn.dev/settings/#logging)

UserInfo has a five-second timeout per network operation. FastMCP uses a 30-second timeout for the upstream token exchange. The generated research client has no HTTP timeout. A stalled research read can therefore wait indefinitely.
