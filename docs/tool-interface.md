# MCP tool reference

All nine tools read HISinOne data with the caller's authorization. Tool discovery shows all nine to an authenticated client. HISinOne decides which records the caller can read. [User guide](user-guide.md) · [Tool definitions](../src/hisinone_mcp/tools.py)

## Tool catalog

The REST paths in the table start at `UPSTREAM_API_BASE_PATH`. Each tool uses GET.

| MCP tool and public arguments | Result | HISinOne path |
| --- | --- | --- |
| `find_projects(query, limit=10)` | Matching project summaries | `/fs/res/project` |
| `get_project(project_id)` | One project | `/fs/res/project/{id}` |
| `find_publications(query, limit=10)` | Matching publication summaries | `/fs/res/publication/simple` |
| `get_publication(publication_id)` | One publication | `/fs/res/publication/{id}` |
| `get_publication_bibtex(publication_id)` | `publication_id` and original `bibtex` citation string | `/fs/res/publication/{id}/bibtex` |
| `list_patents(limit=10)` | Accessible patent summaries | `/fs/res/patent` |
| `get_patent(patent_id)` | One patent | `/fs/res/patent/{id}` |
| `find_research_infrastructures(query, limit=10)` | Matching infrastructure summaries | `/fs/res/researchInfrastructure/simple` |
| `get_research_infrastructure(research_infrastructure_id)` | One research infrastructure record | `/fs/res/researchInfrastructure/{id}` |

## Arguments and results

- Use lowercase `snake_case` for tool names, arguments, and result fields.
- Use `find_<plural>` for a text search. Use `list_<plural>` for a collection that takes no search text.
- Use `get_<singular>` for a lookup. Add the representation after the resource name for a format such as BibTeX.
- Use the resource-specific integer ID in both the input and the output. For a patent, `patent_number` and `patent_id` identify different values.
- Order public arguments as follows. Put the resource ID first, then `query`, then optional filters, then `limit`. Use only the arguments in the catalog. In Python, put the injected API client last.

MCP clients send arguments by name. Searches trim `query` and require at least one non-whitespace character. The four collection tools accept a `limit` from 1 to 20. The default is 10. [MCP tool calls](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#calling-tools)

A collection returns a structured object with a `result` array in HISinOne order. A successful lookup returns one structured object. An empty array means the read succeeded and returned no rows. A full array can have more matches upstream. The tools have no next-page argument. Searches send the limit to HISinOne. Patent listing fetches and decodes the entire accessible collection before applying the limit.

## Record fields

Each lookup includes its summary fields. Missing descriptive values return `null`. For a list field, `[]` means HISinOne supplied a list with no displayable entries. An omitted list field returns `null`. [Public result models](../src/hisinone_mcp/models.py)

| Resource | Summary fields | Additional lookup fields |
| --- | --- | --- |
| Project | `project_id`, `title`, `status` | `description`, `project_type`, `objective`, `subject_areas`, `start_date`, `end_date` |
| Publication | `publication_id`, `title` | `release_year`, `journal`, `abstract`, `creators`, `publication_type`, `identifiers`, `publisher` |
| Patent | `patent_id`, `title`, `patent_number`, `status`, `country` | `publication_number`, `registration_type`, `inventors`, `registration_date`, `grant_date` |
| Research infrastructure | `research_infrastructure_id`, `title` | `description`, `kind`, `type`, `access_modes`, `organizations` |

Status and classification fields contain HISinOne display labels. A project's `objective` is an objective category. Publication `creators` follow HISinOne credit order. Names without an order follow the numbered names in source order. Each publication identifier has a `type` and a `value`, for example `{"type":"DOI","value":"10.1234/example"}`.

Patent `inventors` are display names. Each infrastructure organization has a `name` and an `is_coordinator` flag. A missing flag returns `null`.

### Project visibility

| HISinOne decision | Public `title` | Public `description` |
| --- | --- | --- |
| Supplies a pseudonymized title or marks the record as pseudonymized | Pseudonymized title if present, otherwise `null` | `null` |
| Unmarked record with explicit permission to see original data | Original title if present | Original description if present |
| Unmarked record with explicit denial | `null` | `null` |
| Unmarked record without an explicit decision | Original title if present | `null` |

The domain service reads `canViewOriginalData.uniquename` for the explicit decision. The localized display text can vary. [Project mapping](../src/hisinone_mcp/research.py) · [Visibility tests](../tests/test_research.py)

## Calendar dates

On development, HISinOne sends project and patent calendar days as Unix epoch milliseconds at local midnight. MCP returns offset-aware `date-time` strings using `UPSTREAM_TIMEZONE`. The offset corresponds to each date. UTC uses `Z`. A missing date returns `null`. [RFC 3339 date-time format](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)

| Development record | REST field and epoch milliseconds | MCP field and value in `Europe/Berlin` |
| --- | --- | --- |
| Project `100002` | `startdate=1745186400000` | `start_date=2025-04-21T00:00:00+02:00` |
| Project `100002` | `enddate=1745964000000` | `end_date=2025-04-30T00:00:00+02:00` |
| Patent `1` | `registrationDate=1781042400000` | `registration_date=2026-06-10T00:00:00+02:00` |
| Patent `1` | `grantDate=1793746800000` | `grant_date=2026-11-04T00:00:00+01:00` |

To display the recorded calendar day, use the date in the returned offset. The project's start corresponds to `2025-04-20T22:00:00Z` in UTC and April 21 in Berlin. Midnight on `end_date` begins the recorded end day. Treating it as a deadline would exclude that day.

## Migrating saved calls

Refresh the client's tool list. Update saved calls and result readers as follows.

| Previous interface | Current interface |
| --- | --- |
| `search_projects` | `find_projects` |
| `search_publications` | `find_publications` |
| `search_research_infrastructures` | `find_research_infrastructures` |
| `get_project(id=…)` | `get_project(project_id=…)` |
| `get_research_infrastructure(infrastructure_id=…)` | `get_research_infrastructure(research_infrastructure_id=…)` |
| `id` in a collection or lookup result | Use the resource-specific ID in the record fields table. |
| Project and patent calendar fields parsed as `date` | Parse the four fields above as offset-aware `date-time` values. |
