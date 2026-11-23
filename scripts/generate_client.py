"""Generate the HISinOne client from the complete OpenAPI export."""

import json
import re
import subprocess
from pathlib import Path
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


def normalize(source: Path, output: Path) -> None:
    if output.exists() and source.samefile(output):
        raise ValueError(
            "Choose a separate output file to preserve the upstream export."
        )

    with source.open("rb") as file:
        specification: dict[str, Any] = json.load(file)

    for normalizer in (
        declare_path_parameters_from_placeholders,
        allow_observed_nulls_in_responses,
    ):
        specification = normalizer(specification)

    with output.open("w", encoding="utf-8") as file:
        json.dump(specification, file, ensure_ascii=False, indent=2)
        file.write("\n")


def get_args(path: Path) -> list[str]:
    return [
        "openapi-python-client",
        "generate",
        f"--path={path}",
        "--config=openapi/config.yml",
        "--meta=uv",
        "--output-path=packages/hisinone-client",
        "--overwrite",
        "--fail-on-warning",
    ]


def main() -> None:
    file = Path(__file__).resolve()
    repository = file.parents[1]

    source = repository / "openapi" / "openapi.json"
    normalize(source, normalized := source.with_suffix(".normalized.json"))

    arguments = get_args(normalized)
    subprocess.run(arguments, cwd=repository, check=True)


if __name__ == "__main__":
    main()
