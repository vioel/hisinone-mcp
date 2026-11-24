from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class _Record(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)


class ProjectSummary(_Record):
    project_id: int = Field(validation_alias="id")
    title: str | None
    status: str | None


class Project(ProjectSummary):
    description: str | None
    project_type: str | None
    objective: str | None
    subject_areas: list[str] | None
    start_date: AwareDatetime | None
    end_date: AwareDatetime | None


class PublicationSummary(_Record):
    publication_id: int = Field(validation_alias="id")
    title: str | None


class PublicationIdentifier(BaseModel):
    type: str
    value: str


class Publication(PublicationSummary):
    release_year: int | None
    journal: str | None
    abstract: str | None
    creators: list[str] | None
    publication_type: str | None
    identifiers: list[PublicationIdentifier] | None
    publisher: str | None
