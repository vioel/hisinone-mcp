# Findings from the HISinOne development installation

These observations come from `http://desktop:8080` on 20–24 November 2026. The export identifies HISinOne 2024.06, build 2024.06.12335, hotfix 108. Settings and record visibility can differ on another installation. [Original OpenAPI export](../openapi/openapi.json) · [HIS OAuth guide for this investigation](https://wiki.his.de/mediawiki/index.php?title=Autorisierung_mit_OAuth_2.0-HISinOne&oldid=2680274)

## Sign-in before consent

HISinOne showed the scientist a client-ID-or-redirect error even when the **Client-Key** and the exact callback matched. Clearing the cache did not resolve it. The scientist role lacked `cs.psv.self.AUTHORIZE_OAUTH_CLIENT`. After the administrator assigned this right for the MCP client, the scientist reached consent and completed sign-in. [Role setup](oauth.md#allow-the-scientist-to-authorize-the-client)

The following checks used the development installation root `http://desktop:8080/qisserver`.

| Endpoint | Without credentials | Successful use |
| --- | --- | --- |
| `GET /pages/oauth.faces` | HTTP 403 with a login page | Scientist sign-in and consent returned a code to the exact callback. Omitting the callback produced `invalid_request` on this build. |
| `POST /api/v1/cs/psv/oauth/token` | A GET returned HTTP 405 and advertised POST. | The proxy exchanged the code with HTTP Basic client authentication and the matching S256 PKCE verifier. |
| `GET /api/v1/cs/psv/oauth/userinfo` | HTTP 400 with an OAuth error | A grant with `openid` returned HTTP 200 and a nonempty `sub`. A grant without `openid` returned HTTP 401 even though project search succeeded. |

The export calls the two REST endpoints unreleased. It omits the success response schemas. The HIS guide specifies a 60-second authorization code lifetime. The successful exchange used S256. Rejection of an incorrect upstream verifier still needs a live check. [HIS OAuth guide](https://wiki.his.de/mediawiki/index.php?title=Autorisierung_mit_OAuth_2.0-HISinOne&oldid=2680274)

## OAuth and token lifetime

| Boundary | Behavior |
| --- | --- |
| MCP client to MCP server | The client registers with the proxy and receives a signed MCP access token. The proxy reserves the HISinOne client ID for upstream use. |
| MCP server to HISinOne | The proxy stores the user's opaque HISinOne token in encrypted Redis records. Each protected MCP request checks that token with UserInfo. |
| Tool to REST API | The tool receives a generated API client with the verified HISinOne token for this caller. HISinOne checks the role and granted rights for the read. |

The signed MCP claims identify the downstream client, scopes, and expiry. The HIS design includes an unsigned ID token example. The verifier takes the subject directly from UserInfo. The `profile` scope was unnecessary on development. The export lists a separate right for introspection, `RIGHT_CS_PSV_SECURITY_VIEW_OAUTH2_TOKEN_INFO`. [Proxy](../src/hisinone_mcp/auth/provider.py) · [Verifier](../src/hisinone_mcp/auth/verifier.py) · [HIS OpenID Connect design](https://wiki.his.de/mediawiki/index.php?title=FD-PSV:_OpenID_Connect_Core&oldid=1957046)

A live browser sign-in completed MCP initialization and tool discovery. A read-only Redis check found an encrypted grant with a positive time to live. The tool's `CurrentAccessToken` dependency receives the verified HISinOne token for that grant. [Request-scoped client](../src/hisinone_mcp/tools.py)

Two fresh sign-ins on 23 November showed how the HISinOne limits interact.

| Client limit (minutes) | Installation limit (minutes) | Lifetime in both token responses |
| --- | --- | --- |
| 129600 | 2880 | 172800 seconds (48 hours) |
| 129600 | 129600 | 7776000 seconds (90 days) |

Neither sign-in issued a refresh token. FastMCP starts the MCP lifetime when the client redeems its code. A delay can make the advertised MCP expiry later than the actual HISinOne expiry. UserInfo still checks the upstream grant on each protected request. If the grant expires or HISinOne revokes it, the client must authorize again. [Lifetime settings and fallbacks](server-setup.md#oauth-settings) · [FastMCP 4.2.4 token issuance](https://github.com/PrefectHQ/fastmcp/blob/v4.2.4/fastmcp_slim/fastmcp/server/auth/oauth_proxy/proxy.py#L1390-L1458)

## Remembered consent

The development client grants `openid` by default. A fresh request for only `fs.res.projects:read` returned both scopes. The same token returned a UserInfo subject.

HISinOne 2024.06 remembers consent for the combination of client, user, and role. After the scientist approved four research scopes, another request for only `openid` still returned those research scopes. FastMCP reports the scopes HISinOne granted. Inspector displays them under **Connection Info → OAuth Details**. HISinOne can also add a `ROLE_*` scope.

A clean `openid` grant permitted tool discovery. Research reads with that grant returned permission denied. After adding only the project scope, the scientist could find and read projects. Other resource reads still returned permission denied. [Change or reduce a grant](user-guide.md#change-scopes-or-switch-accounts)

## Record visibility

| Development record | Result with an approved resource scope |
| --- | --- |
| Project `100002`, **Ein super Projekt** | The assigned scientist found the hidden project and read it by ID. A second scientist saw it in HISinOne but received an empty search and a permission error through MCP. |
| Publication | One scientist found a publication and read its record and BibTeX citation. Both the own-publication and visible-publication rights were active. |
| Patent `1`, **Ein krasses Patent** | The scientist listed the patent and read it by ID. Both the own-patent and visible-patent rights were active. |
| Research infrastructure `1`, **Super krasses Labor** | The scientist found the facility by title and read it by ID with the visible-infrastructure right. |

Project `100002` had one member, visibility **versteckt** (level `4000`), and status **vorbereitet** (key `101`). Its API ID matched its logical `lid`. The database row ID was `1`. Use the ID from the tool result.

The second scientist belonged to the same organizational unit. The role's general `fs.res.project.VIEW_PROJECT` right covered status keys `101` and `102`. That broader right can explain why the UI showed the project. The OAuth scope supplied member access and visibility up to level `2000`. [Scientist role restrictions](oauth.md#check-the-roles-research-rights) · [Project search and lookup](../openapi/openapi.json#L13128)

To repeat the comparison, use two browser profiles. Sign in with the same scientist role and project scope in each profile. Run `find_projects` with `{"query":"super"}` and `get_project` with `{"project_id":100002}` in each. Compare the member's result with the nonmember's result. [Inspector sign-in](user-guide.md#connect-with-mcp-inspector)

An empty collection alone does not establish access to an individual record. The publication and patent checks also leave own-only access unverified. Isolating that right requires a record that the visibility right excludes.

## API differences that affect tools

- **Project titles.** HISinOne can supply a pseudonymized title and a separate decision about access to original data. Both search and lookup honor that decision. [Public field rules](tool-interface.md#project-visibility) · [HIS release notes on project visibility](https://wiki.his.de/mediawiki/index.php/Release_Notes_HISinOne_2022.06_RES)
- **Project search.** The export marks project search and lookup as unreleased. Search accepts `q` and `l`. The contract leaves the matched fields unspecified and associates `offset` with `until`. Ordering across REST pages still needs verification. The MCP tools expose bounded results. [Project search contract](../openapi/openapi.json#L12765) · [HIS release notes on `from` and `until`](https://wiki.his.de/mediawiki/index.php/Release_Notes_HISinOne_2023.12_RES)
- **Publication details page.** On 23 November, `/fs/res/publication/1/details` returned HTTP 500 in the HISinOne UI. The application log reported `J2V8 native library not loaded` in `PublicationCitationServiceImpl.renderCitation`. The native library was in the deployed JAR. The load failure remains unexplained. The MCP lookup uses `/fs/res/publication/{id}`, which returned HTTP 200. The separate BibTeX route returned `text/plain`.
- **Unreadable records.** A successful REST request could still fail during decoding. Project search returned `publications: null`. Publication, patent, and infrastructure responses also contained nulls where their schemas specified objects or strings. The generator now accepts the observed values. [Documented schema changes and fixtures](client-generation.md#contract-normalization)
- **Project and patent dates.** The development installation sends calendar days as epoch milliseconds at local midnight. The tool returns each timestamp with the offset that applies in the configured HISinOne time zone. [Verified date examples](tool-interface.md#calendar-dates)
- **Prize rights.** The catalog uses `fs.res.prize.VIEW_PRIZE` for prizes. A personal award is a separate **Preisanerkennung**. Its `fs.res.prize.VIEW_NOMINATION_OWN` right covers a recipient. Prize tools remain outside the current interface. [Prize operation](../openapi/openapi.json#L12626) · [Award operation](../openapi/openapi.json#L11900)

## Permission failures and automated checks

The development project lookup returned a bare HTTP 401 for a user without access. The research service reports a permission error for this response. An explicit `invalid_token` from a research read tells the user to sign in again. The exact challenge for a live revoked HISinOne grant still needs verification. [Domain error handling](../src/hisinone_mcp/protocol.py) · [HIS authorization server design](https://wiki.his.de/mediawiki/index.php?title=FD-PSV:_OAuth_2.0_mit_HISinOne_als_Autorisierungsserver&oldid=1578275)

The integration tests use a mock HISinOne issuer and a private Redis process. They cover authorization code binding, PKCE, expiry, revocation, and user-specific permissions. They also check server restarts and concurrent calls from two users. The callers share connections while their bearer tokens stay separate. [OAuth integration tests](../tests/test_oauth.py)
