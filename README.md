# HISinOne MCP server

This server accepts Streamable HTTP connections at `/mcp`. Sign in with your HISinOne account.

Start the local [Redis service](infrastructure/README.md). Copy `.env.example` to `.env`. Set the server address, HISinOne client credentials, OAuth keys and Redis password.

Start the server from the repository root.

```sh
uv run --locked hisinone-mcp
```
