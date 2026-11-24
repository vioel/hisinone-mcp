# Use the HISinOne MCP server

You need a running MCP server, its URL, and a HISinOne account with access to the records you want to read. Your administrator can supply the URL. The local examples use `http://127.0.0.1:8000/mcp`.

## Connect your MCP client

1. Add a remote server in your MCP client.
2. Enter the URL from your administrator.
3. Select **Streamable HTTP** as the transport.
4. Select **OAuth** for authentication.
5. If the client has a scope field, enter `openid fs.res.projects:read` for project access on the development installation.
6. Connect to the server.
7. Approve the MCP connection in the browser.
8. Sign in to HISinOne when prompted.
9. Select the HISinOne role you want to use.
10. Approve the research permissions you need.

In a chat client, try “Find projects matching ‘super’ and show their titles and statuses.” The assigned scientist can then ask for details of **Ein super Projekt** on development. Inspector provides explicit scope selection for testing.

## Connect with MCP Inspector

These steps use MCP Inspector 2.16.0. You need Node.js with `npx` on the computer where you open the browser. [Inspector release](https://github.com/modelcontextprotocol/inspector/releases/tag/2.16.0)

1. Start Inspector from a terminal.

   ```sh
   npx --yes @modelcontextprotocol/inspector@2.16.0 --web
   ```

2. Open the local URL that Inspector prints.
3. Select **Add Servers → + Add manually**.
4. Enter the connection settings.

   | Field | Local example |
   | --- | --- |
   | **Server ID** | `hisinone-dev` |
   | **Transport** | `streamable-http` |
   | **URL** | `http://127.0.0.1:8000/mcp` |

5. Select **Add**.
6. On the server card, open **Settings → OAuth Settings**.
7. Enter `openid fs.res.projects:read` in **Scopes** for the project example below.
8. Leave **Client ID** and **Client Secret** empty. Inspector registers its own client with the MCP server.
9. Turn on the connection switch.
10. Approve the MCP connection in the browser.
11. Sign in to HISinOne when prompted.
12. Select your HISinOne role. For the development project, use **Wissenschaftler/-in eigene Hochschule**.
13. Approve **Forschungsprojekte lesen** for the project example.
14. In Inspector, open **Tools**. You can see all nine tools. HISinOne checks access when you run one.

## Find and read a project

1. Run `find_projects` with these arguments.

   ```json
   {"query":"super","limit":2}
   ```

2. Find the project's `project_id` in the `result` array. On the development installation, the assigned scientist sees **Ein super Projekt** with ID `100002`.
3. Pass the returned ID to `get_project`.

   ```json
   {"project_id":100002}
   ```

The lookup returns one object. It includes the visible title, status, and project dates. Use the ID from your own search on other installations. [Result fields and date examples](tool-interface.md)

## Read other research records

Keep `openid` for sign-in. Add the scope for each resource you need. The development client offers the following scopes.

| Resource | Additional scope | How to get the record |
| --- | --- | --- |
| Project | `fs.res.projects:read` | Use `find_projects`. Pass the `project_id` to `get_project`. |
| Publication | `fs.res.publications:read` | Use `find_publications`. Pass the `publication_id` to `get_publication` or `get_publication_bibtex`. |
| Patent | `fs.res.patents:read` | Use `list_patents`. Pass the `patent_id` to `get_patent`. |
| Research infrastructure | `fs.res.research-infrastructures:read` | Use `find_research_infrastructures`. Pass the `research_infrastructure_id` to `get_research_infrastructure`. |

For example, to export a citation, search for a publication title. Run `get_publication_bibtex` with its `publication_id`. Copy the `bibtex` field from the result.

## Change scopes or switch accounts

1. On a connected server card, select **Connection Info → OAuth Details → Clear and disconnect**. For a disconnected card, select **Settings → OAuth Settings → Clear stored OAuth state**.
2. To switch accounts, select **Abmelden** in the HISinOne portal. Otherwise the browser can reuse your current login.
3. Open **Settings → OAuth Settings → Scopes** in Inspector.
4. Enter `openid` and the scopes you need, separated by spaces.
5. Save the settings.
6. Turn on the connection switch.
7. Select the intended role on the HISinOne consent screen.
8. Approve the requested permissions.
9. Check the granted scopes under **Connection Info → OAuth Details**.

HISinOne can remember earlier consent for the same client, user, and role. Clearing Inspector removes the local authorization state. To test a smaller grant, use a fresh account or revoke the existing grant in HISinOne. Revocation interrupts sessions that use that grant. [Observed scope behavior](dev-findings.md#remembered-consent)

To revoke your grant, open **Verbundene Apps verwalten** in HISinOne. Revoke access for the intended application. Repeat the procedure above with the smaller scope list.

## Use the FastMCP command line

From the repository root, list the tools on the local server.

```sh
uv run fastmcp list http://127.0.0.1:8000/mcp --auth oauth
```

The default challenge requests `openid`. Tool discovery works with that scope. If the command-line client already has a project grant, it can also run this lookup.

```sh
uv run fastmcp call http://127.0.0.1:8000/mcp get_project project_id=100002 --auth oauth --json
```

## Interpret a result or error

| What you see | What to do |
| --- | --- |
| An empty `result` array | The search or list succeeded. For a search, try text from a record visible to your role. |
| HISinOne rejects the client before consent | Ask the administrator to check the Client-Key, callback URL, and your role's right to authorize that client. [Sign-in findings](dev-findings.md#sign-in-before-consent) |
| Permission denied | Check the granted scope in **OAuth Details**. If it is present, ask the administrator to check the role and the record's visibility. |
| The server asks you to sign in again | Start a new browser authorization. The MCP token or the HISinOne grant can expire. |
| Record not found | Select an ID from a current search or list result. |
| HISinOne returned an unreadable record | Give the maintainer the tool name and the time of the call. The response could differ from its schema. |
| Rate limit or temporary failure | Try again later. If the problem continues, give the administrator the time and any request ID. |
