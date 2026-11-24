# HISinOne MCP server

This server gives Model Context Protocol (MCP) clients read-only access to projects, publications, patents, and research infrastructure in HISinOne. Sign in with your HISinOne account. HISinOne checks your role and your approved scopes on each read.

## Use the server

Connect your MCP client to the server's Streamable HTTP URL. For local development, use `http://127.0.0.1:8000/mcp`.

| Task | Guide |
| --- | --- |
| Connect with MCP Inspector, find a project, or change accounts | [User guide](docs/user-guide.md) |
| Look up tool names, arguments, fields, and date formats | [Tool reference](docs/tool-interface.md) |

## Run and maintain the server

| Task | Guide |
| --- | --- |
| Register the OAuth client, assign scopes, and configure the scientist role | [HISinOne configuration](docs/oauth.md) |
| Start Redis for local development | [Redis setup](infrastructure/README.md) |
| Configure the MCP server, start it, and check the connection | [Server setup and settings](docs/server-setup.md) |
| Investigate a sign-in failure or a difference in record visibility | [Development installation findings](docs/dev-findings.md) |
| Trace a tool call, regenerate the REST client, or run the tests | [Developer guide](docs/client-generation.md) |
