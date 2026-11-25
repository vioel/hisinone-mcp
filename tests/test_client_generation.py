import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from unittest.mock import patch

import hisinone_client
import httpx2
import pytest
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
    JavaUtilHashMap,
)
from hisinone_client.models import (
    FsResResearchInfrastructureResearchInfrastructure as Infrastructure,
)
from hisinone_client.models import (
    FsResResearchInfrastructureSimpleResearchInfrastructure as SimpleInfrastructure,
)

from scripts import generate_client

from .api_client import mock_api_client

FIXTURES = Path(__file__).with_name("fixtures")
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

    for row in json.loads((FIXTURES / "patent-list.json").read_bytes()):
        visit("fs.res.patent.Patent", row)
    visit(
        "fs.res.patent.Patent",
        json.loads((FIXTURES / "patent-lookup.json").read_bytes()),
    )
    for row in json.loads((FIXTURES / "project-search.json").read_bytes()):
        visit("fs.res.project.ProjectObj", row)
    for row in json.loads((FIXTURES / "publication-search.json").read_bytes()):
        visit("fs.res.publication.SimplePublication", row)
    visit(
        "fs.res.project.ProjectObj",
        json.loads((FIXTURES / "project-lookup.json").read_bytes()),
    )
    visit(
        "fs.res.publication.Publication",
        json.loads((FIXTURES / "publication-lookup.json").read_bytes()),
    )
    search = FIXTURES / "research-infrastructure-search.json"
    for row in json.loads(search.read_bytes()):
        visit("fs.res.researchInfrastructure.SimpleResearchInfrastructure", row)
    visit(
        "fs.res.researchInfrastructure.ResearchInfrastructure",
        json.loads((FIXTURES / "research-infrastructure-lookup.json").read_bytes()),
    )
    return observed


def run_generator(source: Path, *options: str) -> tuple[list[str], bytes]:
    calls: list[tuple[list[str], Path, bytes]] = []

    def capture_input(command: list[str], **_: object) -> None:
        option = next(arg for arg in command if arg.startswith("--path="))
        normalized = Path(option.removeprefix("--path="))
        calls.append((command, normalized, normalized.read_bytes()))

    with (
        patch.object(sys, "argv", ["generate_client.py", str(source), *options]),
        patch.object(subprocess, "run", side_effect=capture_input),
    ):
        generate_client.main()

    assert len(calls) == 1
    command, normalized, contents = calls[0]
    assert normalized != source.resolve()
    assert not normalized.exists()
    return command, contents


def test_normalization_preserves_the_complete_contract(
    tmp_path: Path, hisinone_openapi: Path
) -> None:
    expected = json.loads(hisinone_openapi.read_bytes())
    expected["info"]["title"] = "Alternate HISinOne export"
    source = tmp_path / "export.json"
    original = json.dumps(expected).encode("utf-8")
    source.write_bytes(original)
    _, normalized = run_generator(source)
    assert source.read_bytes() == original
    contract = json.loads(normalized)

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


COLLECTION_MODELS = {
    "project-search.json": FsResProjectProjectObj,
    "publication-search.json": FsResPublicationSimplePublication,
    "patent-list.json": FsResPatentPatent,
    "research-infrastructure-search.json": SimpleInfrastructure,
}


@pytest.mark.parametrize("filename", COLLECTION_MODELS)
def test_collection_response_round_trip(filename: str) -> None:
    model = COLLECTION_MODELS[filename]
    rows: list[dict[str, object]] = json.loads((FIXTURES / filename).read_bytes())
    assert rows
    assert [model.from_dict(row).to_dict() for row in rows] == rows


LOOKUP_MODELS = {
    "project-lookup.json": FsResProjectProjectObj,
    "publication-lookup.json": FsResPublicationPublication,
    "patent-lookup.json": FsResPatentPatent,
    "research-infrastructure-lookup.json": Infrastructure,
}


@pytest.mark.parametrize("filename", LOOKUP_MODELS)
def test_lookup_response_round_trip(filename: str) -> None:
    model = LOOKUP_MODELS[filename]
    row: dict[str, object] = json.loads((FIXTURES / filename).read_bytes())
    assert model.from_dict(row).to_dict() == row


@pytest.mark.parametrize("media_type", ["text/plain", "application/json"])
async def test_bibtex_response_uses_its_media_type(media_type: str) -> None:
    citation = "@article{example,\n  title = {Grüße},\n}\n"
    body = json.dumps(citation) if media_type == "application/json" else citation
    response = httpx2.Response(
        200,
        content=body.encode(),
        headers={"Content-Type": f"{media_type}; charset=utf-8"},
    )
    async with mock_api_client(lambda _: response) as client:
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


@pytest.fixture
def small_export(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(
        generate_client, "NULLABLE_FIELDS", {"Example": ("name", "ref")}
    )
    update = "/cs/psv/personProfile/entries/update/{personId}"
    bibtex = "/fs/res/publication/{id}/bibtex"
    string = {"type": "string"}
    ref = {"$ref": "#/components/schemas/Example"}
    properties = {"name": string, "ref": ref, "unchanged": string}
    content = {"application/json": {"schema": string}}
    original = json.dumps(
        {
            "paths": {
                update: {"post": {}},
                bibtex: {"get": {"responses": {"200": {"content": content}}}},
            },
            "components": {"schemas": {"Example": {"properties": properties}}},
        }
    ).encode()
    source = tmp_path / "original export.json"
    source.write_bytes(original)
    return source


def test_normalization_from_a_small_export(small_export: Path) -> None:
    original = small_export.read_bytes()
    _, normalized = run_generator(small_export)
    result = json.loads(normalized)

    update = "/cs/psv/personProfile/entries/update/{personId}"
    bibtex = "/fs/res/publication/{id}/bibtex"
    string = {"type": "string"}
    ref = {"$ref": "#/components/schemas/Example"}
    assert result["paths"][update]["post"]["parameters"] == [
        {
            "name": "personId",
            "in": "path",
            "required": True,
            "schema": {"type": "integer"},
        }
    ]
    assert result["components"]["schemas"]["Example"]["properties"] == {
        "name": {"type": "string", "nullable": True},
        "ref": {"oneOf": [ref, {"type": "object", "nullable": True, "enum": [None]}]},
        "unchanged": string,
    }
    assert result["paths"][bibtex]["get"]["responses"]["200"]["content"] == {
        "application/json": {"schema": string},
        "text/plain": {"schema": string},
    }
    _, repeated = run_generator(small_export)
    assert repeated == normalized
    assert small_export.read_bytes() == original


def test_generator_resolves_custom_paths_from_the_working_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, small_export: Path
) -> None:
    monkeypatch.chdir(tmp_path)
    config = tmp_path / "custom config.yml"
    templates = tmp_path / "custom templates"
    output = tmp_path / "custom client"
    config.touch()
    templates.mkdir()
    command, _ = run_generator(
        small_export.relative_to(tmp_path),
        "--config",
        config.name,
        "--custom-template-path",
        templates.name,
        "--output-path",
        output.name,
    )

    assert f"--config={config}" in command
    assert f"--custom-template-path={templates}" in command
    assert f"--output-path={output}" in command


def test_generator_rejects_the_named_input_path() -> None:
    result = subprocess.run(
        [sys.executable, generate_client.__file__, "--path", "export.json"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "unrecognized arguments: --path" in result.stderr


@pytest.mark.parametrize("output", ["exports", "config", "templates"])
def test_generator_rejects_inputs_inside_the_output(
    tmp_path: Path, output: str
) -> None:
    source = tmp_path / "exports" / "openapi.json"
    config = tmp_path / "config" / "client.yml"
    templates = tmp_path / "templates"
    for directory in (source.parent, config.parent, templates):
        directory.mkdir()
    source.write_bytes(b"{}")
    config.touch()
    result = subprocess.run(
        [
            sys.executable,
            generate_client.__file__,
            source,
            "--config",
            config,
            "--custom-template-path",
            templates,
            "--output-path",
            output,
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "would overwrite an input" in result.stderr
    assert source.read_bytes() == b"{}"


def test_generated_operations_cover_the_export(hisinone_openapi: Path) -> None:
    paths = json.loads(hisinone_openapi.read_bytes())["paths"]
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
    async with mock_api_client(echo) as client:
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

    async with mock_api_client(respond) as client:
        response = await get_config.asyncio_detailed(
            "test/system", "first key", client=client
        )
    assert response.parsed == []
