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
