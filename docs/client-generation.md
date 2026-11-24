# Maintain the server and generate the REST client

The uv workspace contains the MCP server and the `hisinone-client` package. Both use the root `uv.lock`. The generated package covers the full HISinOne export, including deprecated operations. The MCP server registers nine read-only research tools. [Workspace configuration](../pyproject.toml) · [uv workspace layouts](https://docs.astral.sh/uv/concepts/projects/workspaces/#workspace-layouts)

## How a tool reaches HISinOne

| Layer | Responsibility |
| --- | --- |
| MCP interface | `tools.py` registers tool names and arguments. It obtains the caller's API client and translates domain errors. `models.py` defines public record fields such as `project_id`. [Tools](../src/hisinone_mcp/tools.py) · [Public models](../src/hisinone_mcp/models.py) |
| Domain service | `research.py` calls typed REST operations and selects fields the user can see. For example, `read_project` checks the returned ID and chooses the visible title. The service runs independently of FastMCP. [Research service](../src/hisinone_mcp/research.py) |
| Generated REST client | `packages/hisinone-client/` contains typed operations and response models. The project lookup sends `GET /fs/res/project/{id}` and decodes the HISinOne response. [Generated lookup](../packages/hisinone-client/hisinone_client/api/fs_res/get_fs_res_project_id.py) |

For `get_project(project_id)`, the tool passes the ID, the time zone, and an authenticated client to `read_project`. Each caller gets a separate client with their HISinOne token. The clients share a connection pool. [Server assembly](../src/hisinone_mcp/app.py) · [Public tool contract](tool-interface.md)

## Regenerate the client

The generator replaces the entire client package. Make schema corrections in the normalizer and template changes in `openapi/templates/`. Direct edits in the generated package will be lost.

1. For a HISinOne upgrade, obtain the installation's original OpenAPI export. On development the path is `/qisserver/api/v1/cs/sys/rest/openapi.json`. Download requires `RIGHT_CS_SYS_MANAGEMENT_VIEW_SERVICES`.
2. Save the export unchanged as `openapi/openapi.json`. To reproduce the current client, use the existing file.
3. From the repository root, run the locked generator.

   ```sh
   uv run --locked --group codegen python scripts/generate_client.py
   ```

4. Check the normalized specification and the generated package. The script writes `openapi/openapi.normalized.json` before replacing `packages/hisinone-client/`.
5. Run the generation tests and the type checker.

   ```sh
   uv run pytest tests/test_client_generation.py
   uv run pyright
   ```

The script invokes `openapi-python-client==0.30.0` with `--meta=uv`, `--overwrite`, and `--fail-on-warning`. If generation fails, correct the cause and run it again. A failed run can leave a partial package. [Script](../scripts/generate_client.py) · [Configuration](../openapi/config.yml) · [Upstream generator instructions](https://github.com/openapi-generators/openapi-python-client/blob/v0.30.0/README.md#create-a-new-client)

The locked development export uses OpenAPI 3.0.0. It contains 557 operations on 476 paths, 543 component schemas, and a bearer security scheme. Its SHA-256 is `f203644a388b558bedcea7b92e71a8385991c1bb99a55a6b751832431c1cc3f0`. The generation tests compare every HTTP method and route with the original. [Original export](../openapi/openapi.json) · [Normalized export](../openapi/openapi.normalized.json) · [HIS REST administration guide](https://wiki.his.de/mediawiki/index.php?title=REST-Webservices-HISinOne&oldid=2715791)

## Contract normalization

The script applies three corrections to a copy of the original export. It retains all operations, response references, and component schemas. [Normalization code](../scripts/generate_client.py) · [Contract tests](../tests/test_client_generation.py)

### Declare missing path parameters

Nine operations have placeholders in the URL but omit the corresponding parameters. The unmodified generator produced only 548 operations. The normalizer supplies the ten required parameters below. It respects declarations that a future export supplies at the path or operation level. [OpenAPI parameter definition](https://spec.openapis.org/oas/v3.0.0.html#parameter-object)

| Method | Exported route | Added parameter types |
| --- | --- | --- |
| GET | `/cm/exa/edci/{cosId}` | `cosId` string |
| GET | `/cs/psv/configuration/externalsystem/activeconfiguration/{interfaceName}` | `interfaceName` string |
| GET | `/cs/psv/configuration/externalsystem/configs/{interfaceName}/{key}` | `interfaceName` string, `key` string |
| GET | `/cs/psv/configuration/externalsystem/configurations/{interfaceName}` | `interfaceName` string |
| GET | `/cs/psv/configuration/externalsystem/infobox/{system}` | `system` string |
| POST | `/cs/psv/personProfile/entries/update/{personId}` | `personId` integer |
| GET | `/cs/psv/personProfile/entries/{personId}` | `personId` integer |
| GET | `/cs/sys/adminutils/findPathsFromSearchPathsFile/{startEntity}` | `startEntity` string |
| GET | `/cs/sys/fileupload/configKeyExists/{configKey}` | `configKey` string |

Other routes in the export establish the types for `personId`, `interfaceName`, `key`, and `configKey`. The client accepts `cosId`, `system`, and `startEntity` as text. Accepted values for those three routes still need a live check.

### Accept observed null values

Development responses contain explicit JSON nulls for the properties below. For example, project search returned `publications: null`. Decoding failed before the tool could read the project's title. The normalizer marks inline properties as nullable. For a reference, it creates a `oneOf` with the original reference and a null-only alternative. OpenAPI 3.0 ignores sibling properties on a reference. Required properties and array item types retain their definitions. [OpenAPI reference objects](https://spec.openapis.org/oas/v3.0.0.html#reference-object)

| Component | Properties observed as null |
| --- | --- |
| `cs.psv.PersonRest` | `_foreigntext`, `academicdegree`, `academicdegreesuffix`, `allfirstnames`, `birthcity`, `birthdate`, `birthname`, `country`, `gender`, `nameprefix`, `namesuffix`, `objGuid`, `personCompleteName`, `title` |
| `fs.res.patent.Patent` | `_dynamicComponent`, `_foreigntext`, `commentary`, `listviews`, `priorityPatent`, `projects`, `researchContracts` |
| `fs.res.patent.PatentInventor` | `_foreigntext`, `objGuid`, `researchPartner` |
| `fs.res.patent.PatentOrgunit` | `_foreigntext`, `objGuid`, `researchPartner` |
| `fs.res.project.ProjectObj` | `_dynamicComponent`, `_foreigntext`, `commentary`, `documents`, `fundingPrograms`, `isEconomical`, `isPseudonymized`, `kdsfCategory`, `listviews`, `longtext`, `nominations`, `parent`, `predecessor`, `projectType`, `pseudonymizedResearchPartner`, `pseudonymizedTitle`, `publications`, `referenceNumber`, `shorttext`, `uniquename` |
| `fs.res.project.ProjectMemberPosition` | `_foreigntext`, `objGuid`, `projectPeriodStatus`, `validFrom`, `validTo` |
| `fs.res.publication.GlobalIdentifier` | `_foreigntext`, `objGuid` |
| `fs.res.publication.Publication` | `_foreigntext`, `accessAfterEmbargoDate`, `articleNumber`, `blogName`, `changeRequest`, `commentary`, `conference`, `conferenceName`, `edition`, `embargoDate`, `issue`, `journal`, `license`, `listviews`, `numberInSeries`, `numberOfPages`, `pageRange`, `pageRangeFrom`, `pageRangeTo`, `parent`, `series`, `subtitle`, `textAbstract`, `volume` |
| `fs.res.publication.PublicationCreator` | `_foreigntext`, `email`, `isPublicationContact`, `objGuid`, `orcid` |
| `fs.res.publication.Publisher` | `_dynamicComponent`, `_foreigntext`, `longtext`, `objGuid`, `shorttext`, `uniquename` |
| `fs.res.publication.SimplePublication` | `_foreigntext` |
| `fs.res.researchInfrastructure.ResearchInfrastructure` | `_foreigntext`, `description`, `listviews`, `objGuid` |
| `fs.res.researchInfrastructure.ResearchInfrastructureOrganisation` | `_foreigntext`, `objGuid`, `researchPartner` |
| `fs.res.researchInfrastructure.SimpleResearchInfrastructure` | `_foreigntext` |
| `impl.cs.sys.dynamic.SimpleDynamicComponent` | `_foreigntext`, `controlType`, `id`, `label`, `lockVersion`, `name`, `objGuid`, `position`, `sortorder`, `visibleAttributes` |
| `impl.cs.sys.dynamic.SimpleDynamicObject` | `_foreigntext`, `id`, `lockVersion`, `parentObjectGuid` |

The fixtures retain the response types and nulls from development with identifying values replaced. For the same patent, the list returned `projects: null` and the lookup returned an empty project list. Infrastructure search supplied an `objGuid` that the lookup returned as null. The tests decode and re-encode both forms with the full generated models. [Response fixtures](../tests/fixtures/) · [Development findings](dev-findings.md#api-differences-that-affect-tools)

### Accept plain-text BibTeX

The export declares a JSON string for `GET /fs/res/publication/{id}/bibtex`. Development returned HTTP 200 with `Content-Type: text/plain`. The normalizer adds `text/plain` alongside `application/json`. The endpoint template checks the response media type to select the correct string decoder. [BibTeX operation](../openapi/openapi.json#L14587) · [Endpoint template](../openapi/templates/endpoint_module.py.jinja)

## Maintain the templates

The six local Jinja templates derive from openapi-python-client 0.30.0. They type dictionary factories, lists, model exports, and JSON containers in union decoders. Non-null values in nullable model or list fields must pass their decoder. The endpoint override also handles the two BibTeX media types. Other files use the generator's bundled templates. [Template directory and MIT notice](../openapi/templates/) · [Upstream custom template guide](https://github.com/openapi-generators/openapi-python-client/blob/v0.30.0/README.md#using-custom-templates)

When you update the generator, compare the local templates with the new upstream versions. Regenerate the client. Run the generation tests and Pyright. The existing tests check path parameters, field nullability, nested lists, independent dictionaries, and list request bodies.

## Run the project checks

Install `redis-server` on `PATH` for the integration tests. They start a private Redis process and a mock HISinOne issuer on loopback ports. From the repository root, run the following commands.

```sh
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest --cov=hisinone_mcp
```

The project accepts the MPL-2.0 license for `certifi` as a transitive dependency. The Redis license applies to the separate Redis service. [certifi license](https://github.com/certifi/python-certifi/blob/master/LICENSE) · [Redis license](../infrastructure/README.md#redis-license)
