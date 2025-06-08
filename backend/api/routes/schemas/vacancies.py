from api.routes.schemas.base import (
    BaseApiSchema,
    IdApiSchemaMixin,
    ServiceSchema,
    ApiSchema,
)
from api.services.schemas import vacancies as service_schemas
from pydantic import BaseModel


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
