# Configure OAuth in HISinOne

Use an administrator account on the target installation. These steps describe the development system at `http://desktop:8080`. The German labels match its administration screens. Changes to roles or global settings can also affect other applications. [HIS OAuth administration guide](https://wiki.his.de/mediawiki/index.php?title=Autorisierung_mit_OAuth_2.0-HISinOne&oldid=2680274)

## Register the confidential client

1. Open **OAuth2-Clients verwalten**.
2. Create a dedicated client for the MCP server. For the development client, use the following values.

   | HISinOne field | Development value |
   | --- | --- |
   | **Schlüssel** | `hisinone-mcp-dev` |
   | **Anzeigename** | `HISinOne MCP (Entwicklung)` |
   | **Beschreibung** | `Ermöglicht die Suche nach Forschungsprojekten mit den Berechtigungen der angemeldeten Person.` |
   | **Standardsprache** | `deutsch` |
   | **Weiterleitungs-URL** | `http://127.0.0.1:8000/auth/callback` |
   | **Typ** | `vertrauenswürdig` |
   | **PKCE erzwingen** | Enabled |
   | **Technische Rolle** | Empty |
   | **Gültig von**, **Gültig bis** | The saved development client shows `01.01.1900` and `31.12.2100`. |

3. On the new client, select **Key und Secret neu erzeugen** to generate the **Client-Key**.
4. Generate a 64-character secret locally.

   ```sh
   openssl rand -hex 32
   ```

5. Enter the generated value in **Client-Secret**.
6. Select **Speichern**.
7. Store **Client-Key** as `UPSTREAM_CLIENT_ID` in the MCP server's `.env`.
8. Store **Client-Secret** as `UPSTREAM_CLIENT_SECRET` in the same file.

The **Schlüssel** identifies the administration record. The **Client-Key** is the OAuth `client_id`. Register the exact browser callback for your installation, including its scheme, host, port, and path.

## Create the scopes

A *scope* names a permission that an OAuth client can request. A HISinOne *right* controls an operation or access to data. Each research scope on this installation groups one or more rights.

1. In **OAuth-Scopes verwalten**, search for the exact **Schlüssel** from the table.
2. Open the existing scope, or create it if the search returns no match.
3. Set **Anzeigename** and **Beschreibung** for the consent screen. Keep the intended validity dates.
4. Select **Speichern**. The development system keeps the scope form open.
5. For a research scope, open **Zugeordnete Rechte → Rechte hinzufügen**.
6. Select its rights by **Schlüssel** from the table.
7. Select **Auswahl übernehmen**.
8. Select **Speichern** again. Reopen the scope to check its assignments.

| Scope key | Consent label | Rights assigned on development |
| --- | --- | --- |
| `openid` | Anmeldung mit HISinOne | Leave **Zugeordnete Rechte** empty. UserInfo uses this scope to return the person's identifier. |
| `fs.res.projects:read` | Forschungsprojekte lesen | **Sichtbares Projekt sehen** (`fs.res.project.VIEW_PROJECT_VISIBLE`), **Eigenes Projekt sehen** (`fs.res.project.VIEW_PROJECT_OWN`) |
| `fs.res.publications:read` | Publikationen lesen | **Sichtbare Publikation sehen** (`fs.res.publication.VIEW_PUBLICATION_VISIBLE`), **Eigene Publikation sehen** (`fs.res.publication.VIEW_PUBLICATION_OWN`) |
| `fs.res.patents:read` | Patente lesen | **Sichtbares Patent sehen** (`fs.res.patent.VIEW_PATENT_VISIBLE`), **Eigenes Patent sehen** (`fs.res.patent.VIEW_PATENT_OWN`) |
| `fs.res.research-infrastructures:read` | Forschungsinfrastrukturen lesen | **Sichtbare Forschungsinfrastruktur sehen** (`fs.res.researchinfrastructure.VIEW_RESEARCH_INFRASTRUCTURE_VISIBLE`) |

For a new installation, these German descriptions can serve as consent text.

| **Schlüssel** | **Beschreibung** |
| --- | --- |
| `openid` | Die Anwendung darf zur Anmeldung Ihre eindeutige HISinOne-Personenkennung abrufen. |
| `fs.res.projects:read` | Die Anwendung darf nach Forschungsprojekten suchen und die Projektdaten lesen, die Sie in Ihrer aktuellen Rolle sehen dürfen. |
| `fs.res.publications:read` | Die Anwendung darf eigene Publikationen und weitere in Ihrer aktuellen Rolle sichtbare Publikationen suchen, lesen und als BibTeX abrufen. |
| `fs.res.patents:read` | Die Anwendung darf eigene und weitere in Ihrer aktuellen Rolle sichtbare Patente lesen. |
| `fs.res.research-infrastructures:read` | Die Anwendung darf Forschungsinfrastrukturen suchen und lesen, die in Ihrer aktuellen Rolle sichtbar sind. |

## Assign the scopes to the client

1. Open the saved client in **OAuth2-Clients verwalten**.
2. Select **Zugeordnete Scopes → Scopes hinzufügen**.
3. Select `openid` and each research scope the client should offer.
4. Select **Auswahl übernehmen**.
5. Set `openid` as a default grant for this client.
6. Keep user consent enabled for each research scope.
7. Select **Speichern**.
8. Reopen the client to check **Zugeordnete Scopes**.

On the MCP server, include the assigned keys in `OAUTH_AVAILABLE_SCOPES`. For the development setup, set `OAUTH_REQUIRED_SCOPES=["openid"]`. Restart the MCP server after a settings change. [Server settings](server-setup.md#oauth-settings)

## Allow the scientist to authorize the client

1. Open **Rollen und Rechte → Rollen bearbeiten → Wissenschaftler/-in**.
2. Under **Rechte hinzufügen**, find `cs.psv.self.AUTHORIZE_OAUTH_CLIENT`.
3. Assign **OAuth2-Client autorisieren** to this role.
4. Open **Rechteparameter** for this right.
5. Under **Rechteeinschränkung hinzufügen**, select **Einschränkung auf OAuth2-Clients** (`OAuth2Client.objGuid`).
6. Select only **HISinOne MCP (Entwicklung)** for the development role.
7. Save the restriction.
8. Save the role.
9. Reopen the role to check the selected client.

HISinOne checks this role right before it shows the consent screen. A missing assignment can produce the same message as an unknown client ID or a callback mismatch. [Development sign-in findings](dev-findings.md#sign-in-before-consent)

## Check the role's research rights

Open **Rechteparameter** for each applicable right under **Rollen bearbeiten → Wissenschaftler/-in**. Check the restrictions before granting access. An unrestricted right can expose other records in the permitted organizations.

| Right on the scientist role | Development restriction |
| --- | --- |
| **Sichtbares Projekt sehen** | **Einschränkung auf Sichtbarkeit** is `[Visibility].visibilityLevel <= ownRoleVisibility`. **Einschränkung Orgunit (Auswahl)** is **Alle Organisationseinheiten**. |
| **Eigenes Projekt sehen** | **Einschränkung auf Mitglieder** is `[Member].id = ownPersonId`. The HISinOne right can include financial details for assigned projects. |
| **Eigene Publikation sehen** | **Einschränkung auf eigene Forschungsobjekte** uses `ownPersonId` for an author or editor. The visible-publication right has separate visibility and status restrictions. |
| **Eigenes Patent sehen** | The own-record restriction uses `ownPersonId` for an inventor. The role also restricts patent status. |
| **Sichtbare Forschungsinfrastruktur sehen** | Visibility is limited to `<= ownRoleVisibility`. The development rights catalog has no per-person ownership right for this resource. |

## Set the development token lifetime

HISinOne uses the smaller of the installation limit and the client limit. It measures both in minutes. The installation setting affects every client that depends on it.

1. In **OAuth2-Clients verwalten**, set **Gültigkeitsdauer des Token** to `129600` for `hisinone-mcp-dev`.
2. Save the client.
3. Check the limits for the other clients before raising the installation limit. The other development client has an explicit value of `2880` to keep its 48-hour limit.
4. Open **Administration → System-Konfiguration → Globale Konfiguration bearbeiten**.
5. Search for `core.psv.interface.oauth2.access_token_lifetime`.
6. Set **Gültigkeitsdauer eines Access-Tokens** to `129600` in the active configuration source.
7. Save the change. On development, **Verwendeter Wert** shows `129600 (HAWK)`.
8. Leave `OAUTH_MCP_ACCESS_TOKEN_EXPIRY_SECONDS` empty on the MCP server.
9. Start a fresh authorization. Existing tokens keep their previous expiry.

On development, both token responses reported `expires_in=7776000` seconds (90 days). Neither token response contained a refresh token. [Expiry and fallback behavior](dev-findings.md#oauth-and-token-lifetime)

## Verify the registration

1. In Inspector, set **Scopes** to `openid fs.res.projects:read` before connecting. [Inspector setup](user-guide.md#connect-with-mcp-inspector)
2. Connect as the project member.
3. Select **Wissenschaftler/-in eigene Hochschule** in HISinOne.
4. Approve **Forschungsprojekte lesen**.
5. Check the granted scopes in **Connection Info → OAuth Details**.
6. Find a known project. Use its returned ID for a lookup. [Project example](user-guide.md#find-and-read-a-project)

## Change the client secret

1. Open the existing confidential client in **OAuth2-Clients verwalten**.
2. Generate a new secret with `openssl rand -hex 32`.
3. Replace **Client-Secret**. Keep the current **Client-Key**.
4. Select **Speichern**.
5. Set `UPSTREAM_CLIENT_SECRET` to the new value on the MCP server.
6. Restart the MCP server.
7. Verify a fresh sign-in to test the new secret.
