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


class PatentSummary(_Record):
    patent_id: int = Field(validation_alias="id")
    title: str | None
    patent_number: str | None
    status: str | None
    country: str | None


class Patent(PatentSummary):
    publication_number: str | None
    registration_type: str | None
    inventors: list[str] | None
    registration_date: AwareDatetime | None
    grant_date: AwareDatetime | None


class ResearchInfrastructureSummary(_Record):
    research_infrastructure_id: int = Field(validation_alias="id")
    title: str | None


class InfrastructureOrganization(BaseModel):
    name: str
    is_coordinator: bool | None


class ResearchInfrastructure(ResearchInfrastructureSummary):
    description: str | None
    kind: str | None
    type: str | None
    access_modes: list[str] | None
    organizations: list[InfrastructureOrganization] | None
