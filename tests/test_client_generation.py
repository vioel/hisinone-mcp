import json
import re
from pathlib import Path
from runpy import run_path
from typing import Any

import pytest

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
