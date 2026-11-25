"""Generate the HISinOne client from the complete OpenAPI export."""

import argparse
import json
import re
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

MISSING_PATH_PARAMETERS = (
    ("get", "/cm/exa/edci/{cosId}"),
    ("get", "/cs/psv/configuration/externalsystem/activeconfiguration/{interfaceName}"),
    ("get", "/cs/psv/configuration/externalsystem/configs/{interfaceName}/{key}"),
    ("get", "/cs/psv/configuration/externalsystem/configurations/{interfaceName}"),
    ("get", "/cs/psv/configuration/externalsystem/infobox/{system}"),
    ("post", "/cs/psv/personProfile/entries/update/{personId}"),
    ("get", "/cs/psv/personProfile/entries/{personId}"),
    ("get", "/cs/sys/adminutils/findPathsFromSearchPathsFile/{startEntity}"),
    ("get", "/cs/sys/fileupload/configKeyExists/{configKey}"),
)


def declare_path_parameters_from_placeholders(
    specification: dict[str, Any],
) -> dict[str, Any]:
    paths = specification["paths"]

    for method, path in MISSING_PATH_PARAMETERS:
        item = paths.get(path, {})
        if item.get("parameters"):
            continue

        operation = item.get(method)
        if operation is None or operation.get("parameters"):
            continue

        parameters: list[dict[str, Any]] = []
        for name in re.findall(r"\{([^{}]+)\}", path):
            schema = {"type": "integer" if name == "personId" else "string"}
            parameters.append(
                {"name": name, "in": "path", "required": True, "schema": schema}
            )

        operation["parameters"] = parameters

    return specification


NULLABLE_FIELDS = {
    "cs.psv.PersonRest": (
        "_foreigntext",
        "academicdegree",
        "academicdegreesuffix",
        "allfirstnames",
        "birthcity",
        "birthdate",
        "birthname",
        "country",
        "gender",
        "nameprefix",
        "namesuffix",
        "objGuid",
        "personCompleteName",
        "title",
    ),
    "fs.res.patent.Patent": (
        "_dynamicComponent",
        "_foreigntext",
        "commentary",
        "listviews",
        "priorityPatent",
        "projects",
        "researchContracts",
    ),
    "fs.res.patent.PatentInventor": ("_foreigntext", "objGuid", "researchPartner"),
    "fs.res.patent.PatentOrgunit": ("_foreigntext", "objGuid", "researchPartner"),
    "fs.res.project.ProjectObj": (
        "_dynamicComponent",
        "_foreigntext",
        "commentary",
        "documents",
        "fundingPrograms",
        "isEconomical",
        "isPseudonymized",
        "kdsfCategory",
        "listviews",
        "longtext",
        "nominations",
        "parent",
        "predecessor",
        "projectType",
        "pseudonymizedResearchPartner",
        "pseudonymizedTitle",
        "publications",
        "referenceNumber",
        "shorttext",
        "uniquename",
    ),
    "fs.res.project.ProjectMemberPosition": (
        "_foreigntext",
        "objGuid",
        "projectPeriodStatus",
        "validFrom",
        "validTo",
    ),
    "fs.res.publication.GlobalIdentifier": ("_foreigntext", "objGuid"),
    "fs.res.publication.Publication": (
        "_foreigntext",
        "accessAfterEmbargoDate",
        "articleNumber",
        "blogName",
        "changeRequest",
        "commentary",
        "conference",
        "conferenceName",
        "edition",
        "embargoDate",
        "issue",
        "journal",
        "license",
        "listviews",
        "numberInSeries",
        "numberOfPages",
        "pageRange",
        "pageRangeFrom",
        "pageRangeTo",
        "parent",
        "series",
        "subtitle",
        "textAbstract",
        "volume",
    ),
    "fs.res.publication.PublicationCreator": (
        "_foreigntext",
        "email",
        "isPublicationContact",
        "objGuid",
        "orcid",
    ),
    "fs.res.publication.Publisher": (
        "_dynamicComponent",
        "_foreigntext",
        "longtext",
        "objGuid",
        "shorttext",
        "uniquename",
    ),
    "fs.res.publication.SimplePublication": ("_foreigntext",),
    "fs.res.researchInfrastructure.ResearchInfrastructure": (
        "_foreigntext",
        "description",
        "listviews",
        "objGuid",
    ),
    "fs.res.researchInfrastructure.ResearchInfrastructureOrganisation": (
        "_foreigntext",
        "objGuid",
        "researchPartner",
    ),
    "fs.res.researchInfrastructure.SimpleResearchInfrastructure": ("_foreigntext",),
    "impl.cs.sys.dynamic.SimpleDynamicComponent": (
        "_foreigntext",
        "controlType",
        "id",
        "label",
        "lockVersion",
        "name",
        "objGuid",
        "position",
        "sortorder",
        "visibleAttributes",
    ),
    "impl.cs.sys.dynamic.SimpleDynamicObject": (
        "_foreigntext",
        "id",
        "lockVersion",
        "parentObjectGuid",
    ),
}


def allow_observed_nulls_in_responses(
    specification: dict[str, Any],
) -> dict[str, Any]:
    schemas = specification["components"]["schemas"]

    for name, fields in NULLABLE_FIELDS.items():
        properties = schemas[name]["properties"]

        for field in fields:
            prop = properties[field]
            if "$ref" in prop:
                # OpenAPI 3.0 ignores nullable next to a reference.
                properties[field] = {
                    "oneOf": [
                        prop,
                        {"type": "object", "nullable": True, "enum": [None]},
                    ]
                }
            elif "type" in prop:
                prop["nullable"] = True
    return specification


def add_bibtex_plain_text_response(specification: dict[str, Any]) -> dict[str, Any]:
    operation = specification["paths"]["/fs/res/publication/{id}/bibtex"]["get"]
    content = operation["responses"]["200"]["content"]

    schema = content.get("application/json", {}).get("schema", {})
    if schema.get("type") == "string":
        content.setdefault("text/plain", {"schema": schema})

    return specification


def get_args(path: Path, config: Path, templates: Path, output: Path) -> list[str]:
    return [
        "openapi-python-client",
        "generate",
        f"--path={path}",
        f"--config={config}",
        f"--custom-template-path={templates}",
        "--meta=uv",
        f"--output-path={output}",
        "--overwrite",
        "--fail-on-warning",
    ]


def main() -> None:
    file = Path(__file__).resolve()
    repository = file.parents[1]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path, help="Original file")
    parser.add_argument(
        "--config",
        type=Path,
        default=repository / "openapi/config.yml",
        help="Configuration file (default: %(default)s)",
    )
    parser.add_argument(
        "--custom-template-path",
        type=Path,
        default=repository / "openapi/templates",
        help="Template directory (default: %(default)s)",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=repository / "packages/hisinone-client",
        help="Output directory (default: %(default)s)",
    )

    args = parser.parse_args()
    original: Path = args.original.resolve()
    config: Path = args.config.resolve()
    templates: Path = args.custom_template_path.resolve()
    output: Path = args.output_path.resolve()

    for path in (original, config, templates, file):
        if path.is_relative_to(output):
            parser.error(f"Output directory {output} would overwrite an input: {path}")

    for path in (original, config):
        if not path.is_file():
            parser.error(f"Expected a file at {path}")

    if not templates.is_dir():
        parser.error(f"Expected a template directory at {templates}")

    with original.open("rb") as file:
        specification: dict[str, Any] = json.load(file)

    for normalizer in (
        declare_path_parameters_from_placeholders,
        allow_observed_nulls_in_responses,
        add_bibtex_plain_text_response,
    ):
        specification = normalizer(specification)

    with TemporaryDirectory() as directory:
        normalized = Path(directory) / "openapi.json"

        with normalized.open("w", encoding="utf-8") as file:
            json.dump(specification, file)

        arguments = get_args(normalized, config, templates, output)
        subprocess.run(arguments, cwd=repository, check=True)


if __name__ == "__main__":
    main()
