from datetime import datetime

from pydantic import Field

from api.routes.schemas.base import (
    BaseApiSchema,
)
from api.services.schemas import vacancies as service_schemas


class VacancySalaryStats(BaseApiSchema[service_schemas.VacancySalaryStats]):
    min_salary: float | None = None
    q1_salary: float | None = None
    median_salary: float | None = None
    mean_salary: float | None = None
    q3_salary: float | None = None
    max_salary: float | None = None

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacancySalaryStats
    ) -> "VacancySalaryStats":
        return cls(**service_schema.model_dump())


class VacanciesCount(BaseApiSchema[service_schemas.VacanciesCount]):
    count: int | None = None

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacanciesCount
    ) -> "VacanciesCount":
        return cls(count=service_schema.count)


class VacanciesSummaryLLM(BaseApiSchema[service_schemas.VacanciesSummaryLLM]):
    response: str

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacanciesSummaryLLM
    ) -> "VacanciesSummaryLLM":
        return cls(response=service_schema.response)


class VacanciesSalaryBins(BaseApiSchema[service_schemas.VacanciesSalaryBins]):
    salary_range: str
    count: int

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacanciesSalaryBins
    ) -> "VacanciesSalaryBins":
        return cls(salary_range=service_schema.salary_range, count=service_schema.count)


class VacancySpecialization(BaseApiSchema[service_schemas.VacancySpecialization]):
    specialization: str

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacancySpecialization
    ) -> "VacancySpecialization":
        return cls(specialization=service_schema.specialization)


class VacancyRegion(BaseApiSchema[service_schemas.VacancyRegion]):
    region: str

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacancyRegion
    ) -> "VacancyRegion":
        return cls(region=service_schema.region)


class VacancyGender(BaseApiSchema[service_schemas.VacancyGender]):
    gender: str

    @classmethod
    def from_service_schema(
        cls, service_schema: service_schemas.VacancyGender
    ) -> "VacancyGender":
        return cls(gender=service_schema.gender)


class VacancyFilters(BaseApiSchema[service_schemas.VacancyFilters]):
    publication_date_gte: datetime | None = Field(None)
    publication_date_lte: datetime | None = Field(None)
    age_gte: int | None = Field(None)
    age_lte: int | None = Field(None)
    region: list[str] | None = Field(None)
    specialization: list[str] | None = Field(None)
    gender: list[str] | None = Field(None)

    @classmethod
    def to_service_schema(
        cls, service_schema: service_schemas.VacancyFilters
    ) -> "VacancyFilters":
        return cls(**service_schema.model_dump())
