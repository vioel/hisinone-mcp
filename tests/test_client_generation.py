import json
import re
from pathlib import Path
from runpy import run_path
from typing import Any

import hisinone_client
import httpx2
import pytest
from hisinone_client import AuthenticatedClient
from hisinone_client.api.cs_psv import (
    get_cs_psv_configuration_externalsystem_configs_interface_name_key as get_config,
)
from hisinone_client.api.fs_res import (
    get_fs_res_publication_id_bibtex,
    post_fs_res_publication_type_relation,
)
from hisinone_client.models import (
    ConditionTermRest,
    ContextConfigRest,
    FsResPatentPatent,
    FsResProjectProjectObj,
    FsResProjectProjectObjForeigntextType0,
    FsResPublicationPublication,
    FsResPublicationPublicationTypeRelation,
    FsResPublicationSimplePublication,
    FsResResearchInfrastructureResearchInfrastructure,
    FsResResearchInfrastructureSimpleResearchInfrastructure,
    JavaUtilHashMap,
)

ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "openapi" / "openapi.json"
METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
PARAMETER = re.compile(r"\{([^{}]+)\}")


def observed_response_nulls(schemas: dict[str, Any]) -> set[tuple[str, str]]:
    observed: set[tuple[str, str]] = set()

    def visit(model: str, row: dict[str, Any]) -> None:
        for field, prop in schemas[model]["properties"].items():
            if field not in row:
                continue
            value = row[field]
            if value is None:
                observed.add((model, field))
            elif "$ref" in prop:
                visit(prop["$ref"].rsplit("/", 1)[-1], value)
            elif ref := prop.get("items", {}).get("$ref"):
                for item in value:
                    visit(ref.rsplit("/", 1)[-1], item)

    fixtures = ROOT / "tests" / "fixtures"
    for row in json.loads((fixtures / "patent-list.json").read_bytes()):
        visit("fs.res.patent.Patent", row)
    visit(
        "fs.res.patent.Patent",
        json.loads((fixtures / "patent-lookup.json").read_bytes()),
    )
    for row in json.loads((fixtures / "project-search.json").read_bytes()):
        visit("fs.res.project.ProjectObj", row)
    for row in json.loads((fixtures / "publication-search.json").read_bytes()):
        visit("fs.res.publication.SimplePublication", row)
    visit(
        "fs.res.project.ProjectObj",
        json.loads((fixtures / "project-lookup.json").read_bytes()),
    )
    visit(
        "fs.res.publication.Publication",
        json.loads((fixtures / "publication-lookup.json").read_bytes()),
    )
    search = fixtures / "research-infrastructure-search.json"
    for row in json.loads(search.read_bytes()):
        visit("fs.res.researchInfrastructure.SimpleResearchInfrastructure", row)
    visit(
        "fs.res.researchInfrastructure.ResearchInfrastructure",
        json.loads((fixtures / "research-infrastructure-lookup.json").read_bytes()),
    )
    return observed


def test_normalization_preserves_the_complete_contract(tmp_path: Path) -> None:
    expected = json.loads(EXPORT.read_bytes())
    expected["info"]["title"] = "Alternate HISinOne export"
    source = tmp_path / "export.json"
    original = json.dumps(expected).encode("utf-8")
    source.write_bytes(original)
    output = tmp_path / "normalized.json"
    generate = run_path(str(ROOT / "scripts" / "generate_client.py"))
    generate["normalize"](source, output)
    assert source.read_bytes() == original
    contract = json.loads(output.read_bytes())

    for path, item in expected["paths"].items():
        for method in METHODS.intersection(item):
            operation = item[method]
            names = PARAMETER.findall(path)
            if names and not item.get("parameters") and not operation.get("parameters"):
                operation["parameters"] = [
                    {
                        "name": name,
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer" if name == "personId" else "string"
                        },
                    }
                    for name in names
                ]

    bibtex = expected["paths"]["/fs/res/publication/{id}/bibtex"]["get"]["responses"]
    bibtex["200"]["content"]["text/plain"] = {"schema": {"type": "string"}}

    # Undo only nullability corrections before comparing the entire contract.
    originals = expected["components"]["schemas"]
    observed = observed_response_nulls(originals)
    for name, schema in contract["components"]["schemas"].items():
        for field, prop in schema.get("properties", {}).items():
            original = originals[name]["properties"][field]
            if prop == original:
                continue
            assert (name, field) in observed
            if "$ref" in original:
                assert prop == {
                    "oneOf": [
                        original,
                        {"type": "object", "nullable": True, "enum": [None]},
                    ]
                }
            else:
                assert prop == {**original, "nullable": True}
            schema["properties"][field] = original
    assert contract == expected


@pytest.mark.parametrize("operation", ["lookup", "search"])
def test_full_project_responses_round_trip(operation: str) -> None:
    fixture = ROOT / "tests" / "fixtures" / f"project-{operation}.json"
    payload = json.loads(fixture.read_bytes())
    rows: list[dict[str, object]] = payload if operation == "search" else [payload]
    for row in rows:
        project = FsResProjectProjectObj.from_dict(row)
        assert project.to_dict() == row


@pytest.mark.parametrize("operation", ["list", "lookup"])
def test_full_patent_responses_round_trip(operation: str) -> None:
    fixture = ROOT / "tests" / "fixtures" / f"patent-{operation}.json"
    payload = json.loads(fixture.read_bytes())
    rows: list[dict[str, object]] = payload if operation == "list" else [payload]
    for row in rows:
        assert FsResPatentPatent.from_dict(row).to_dict() == row


def test_publication_search_round_trip() -> None:
    fixture = ROOT / "tests" / "fixtures" / "publication-search.json"
    for row in json.loads(fixture.read_bytes()):
        assert FsResPublicationSimplePublication.from_dict(row).to_dict() == row


def test_publication_lookup_round_trip() -> None:
    fixture = ROOT / "tests" / "fixtures" / "publication-lookup.json"
    row = json.loads(fixture.read_bytes())
    assert FsResPublicationPublication.from_dict(row).to_dict() == row


def test_research_infrastructure_search_round_trip() -> None:
    fixture = ROOT / "tests" / "fixtures" / "research-infrastructure-search.json"
    for row in json.loads(fixture.read_bytes()):
        result = FsResResearchInfrastructureSimpleResearchInfrastructure.from_dict(row)
        assert result.to_dict() == row


def test_research_infrastructure_lookup_round_trip() -> None:
    fixture = ROOT / "tests" / "fixtures" / "research-infrastructure-lookup.json"
    row = json.loads(fixture.read_bytes())
    result = FsResResearchInfrastructureResearchInfrastructure.from_dict(row)
    assert result.to_dict() == row


@pytest.mark.parametrize("media_type", ["text/plain", "application/json"])
async def test_bibtex_response_uses_its_media_type(media_type: str) -> None:
    citation = "@article{example,\n  title = {Grüße},\n}\n"
    body = json.dumps(citation) if media_type == "application/json" else citation
    response = httpx2.Response(
        200,
        content=body.encode(),
        headers={"Content-Type": f"{media_type}; charset=utf-8"},
    )
    async with AuthenticatedClient(
        base_url="https://his.test",
        token="caller",
        httpx_args={"transport": httpx2.MockTransport(lambda _: response)},
    ) as client:
        parsed = await get_fs_res_publication_id_bibtex.asyncio(7, client=client)
        assert parsed == citation


@pytest.mark.parametrize(
    "row",
    [
        {},
        {"publications": None},
        {"publications": []},
        {"publications": [{"id": 2}], "parent": {"id": 1}},
    ],
)
def test_project_relationships_round_trip(row: dict[str, object]) -> None:
    assert FsResProjectProjectObj.from_dict(row).to_dict() == row


def test_nullable_project_relationships_use_the_generated_models() -> None:
    project = FsResProjectProjectObj.from_dict({"publications": [{"id": 4}]})
    assert isinstance(project.publications, list)
    assert project.publications == [FsResPublicationPublication(id=4)]
    with pytest.raises(TypeError):
        FsResProjectProjectObj.from_dict({"publications": [None]})
    with pytest.raises(TypeError):
        FsResProjectProjectObj.from_dict({"parent": "not a project"})


def test_saved_normalized_specification_is_current(tmp_path: Path) -> None:
    output = tmp_path / "normalized.json"
    generate = run_path(str(ROOT / "scripts" / "generate_client.py"))
    generate["normalize"](EXPORT, output)
    saved = ROOT / "openapi" / "openapi.normalized.json"
    assert output.read_bytes() == saved.read_bytes()


def test_normalization_rejects_overwriting_its_source(tmp_path: Path) -> None:
    source = tmp_path / "export.json"
    source.write_bytes(b"{}")
    output = tmp_path / "alias.json"
    output.hardlink_to(source)
    generate = run_path(str(ROOT / "scripts" / "generate_client.py"))

    with pytest.raises(ValueError, match="separate output file"):
        generate["normalize"](source, output)
    assert source.read_bytes() == b"{}"


def test_generated_operations_cover_the_export() -> None:
    paths = json.loads(EXPORT.read_bytes())["paths"]
    # The generator gives path variables Python names, e.g. personId becomes person_id.
    expected = [
        (method, PARAMETER.sub("{}", path))
        for path, item in paths.items()
        for method in METHODS.intersection(item)
    ]
    api = Path(hisinone_client.__file__).parent / "api"
    generated: list[tuple[str, str]] = []
    for module in api.glob("*/*.py"):
        if module.name == "__init__.py":
            continue
        request = re.search(
            r'"method": "([a-z]+)",\s*"url":\s*(?:\(\s*)?"([^"]+)"', module.read_text()
        )
        assert request, module
        generated.append((request[1], PARAMETER.sub("{}", request[2])))
    assert sorted(generated) == sorted(expected)


def test_nested_model_lists_round_trip() -> None:
    source = {"dnfExpression": [[{"leftOperand": "status"}], []]}
    model = ContextConfigRest.from_dict(source)

    assert model.dnf_expression == [[ConditionTermRest(left_operand="status")], []]
    assert model.to_dict() == source


def test_model_dictionary_factory_is_per_instance() -> None:
    texts = FsResProjectProjectObjForeigntextType0()
    texts["defaulttext"] = JavaUtilHashMap.from_dict({"de": "Projekttitel"})

    assert texts.to_dict() == {"defaulttext": {"de": "Projekttitel"}}
    assert FsResProjectProjectObjForeigntextType0().additional_properties == {}


async def test_optional_list_request_body_round_trips() -> None:
    received: list[bytes] = []

    def echo(request: httpx2.Request) -> httpx2.Response:
        received.append(request.content)
        return httpx2.Response(200, content=request.content or b"[]")

    relation = FsResPublicationPublicationTypeRelation(id=7)
    async with AuthenticatedClient(
        base_url="https://his.test",
        token="test",
        httpx_args={"transport": httpx2.MockTransport(echo)},
    ) as client:
        send = post_fs_res_publication_type_relation.asyncio_detailed
        await send(client=client)
        await send(client=client, body=[])
        response = await send(client=client, body=[relation])

    assert received[:2] == [b"", b"[]"]
    assert json.loads(received[2]) == [{"id": 7}]
    assert response.parsed == [relation]


async def test_repaired_route_sends_both_path_parameters() -> None:
    def respond(request: httpx2.Request) -> httpx2.Response:
        assert request.method == "GET"
        assert request.url.raw_path == (
            b"/cs/psv/configuration/externalsystem/configs/test%2Fsystem/first%20key"
        )
        return httpx2.Response(200, json=[])

    async with AuthenticatedClient(
        base_url="https://his.test",
        token="test",
        httpx_args={"transport": httpx2.MockTransport(respond)},
    ) as client:
        response = await get_config.asyncio_detailed(
            "test/system", "first key", client=client
        )
    assert response.parsed == []
