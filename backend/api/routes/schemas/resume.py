from datetime import datetime

from pydantic import Field

from api.routes.schemas.base import (
    BaseApiSchema,
)
from api.services.schemas import resume as service_schemas


class ResumeCount(BaseApiSchema[service_schemas.ResumeCount]):
    count: int | None = None

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.ResumeCount
    ) -> "ResumeCount":
        return cls(count=service_schema.count)


class ResumeFilters(BaseApiSchema[service_schemas.ResumeFilters]):
    publication_date_gte: datetime | None = Field(None)
    publication_date_lte: datetime | None = Field(None)
    age_gte: int | None = Field(None)
    age_lte: int | None = Field(None)
    region: list[str] | None = Field(None)
    specialization: list[str] | None = Field(None)
    gender: list[str] | None = Field(None)

    @classmethod
    def to_service_schema(
        cls, service_schema: service_schemas.ResumeFilters
    ) -> "ResumeFilters":
        return cls(**service_schema.model_dump())
