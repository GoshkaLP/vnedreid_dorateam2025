from datetime import datetime

from pydantic import Field

from api.routes.schemas.base import (
    BaseApiSchema,
)
from api.services.schemas import radar as service_schemas


class RadarFilters(BaseApiSchema[service_schemas.RadarFilters]):
    publication_date_gte: datetime | None = Field(None)
    publication_date_lte: datetime | None = Field(None)
    age_gte: int | None = Field(None)
    age_lte: int | None = Field(None)
    region: list[str] | None = Field(None)
    specialization: list[str] | None = Field(None)
    gender: list[str] | None = Field(None)

    @classmethod
    def to_service_schema(
        cls, service_schema: service_schemas.RadarFilters
    ) -> "RadarFilters":
        return cls(**service_schema.model_dump())


class BenifitsCompany(BaseApiSchema[service_schemas.BenifitsCompany]):
    company: str
    benifits: list[int]

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.BenifitsCompany
    ) -> "BenifitsCompany":
        return cls(company=service_schema.company, benifits=service_schema.benifits)
