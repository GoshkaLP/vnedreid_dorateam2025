from datetime import date, datetime

from pydantic import BaseModel

from api.services.schemas.base import (
    BaseServiceSchema,
    IdCreatedDeletedServiceSchemaMixin,
)


class Vacancies(BaseServiceSchema, IdCreatedDeletedServiceSchemaMixin):
    vacancy_date: date | None = None
    specialization: str | None = None
    region: str | None = None
    work_experience: str | None = None
    age: int | None = None
    gender: str | None = None
    salary_specified: bool | None = False
    salary_amount: float | None = None
    company: str | None = None
    vacancy_source: str | None = None


class VacancySalaryStats(BaseServiceSchema):
    min_salary: float | None = None
    q1_salary: float | None = None
    median_salary: float | None = None
    mean_salary: float | None = None
    q3_salary: float | None = None
    max_salary: float | None = None


class VacanciesCount(BaseServiceSchema):
    count: int | None = None


class VacanciesSummaryLLM(BaseServiceSchema):
    response: str


class VacanciesSalaryBins(BaseServiceSchema):
    salary_range: str
    count: int


class VacancySpecialization(BaseServiceSchema):
    specialization: str


class VacancyRegion(BaseServiceSchema):
    region: str


class VacancyGender(BaseServiceSchema):
    gender: str


class VacancyFilters(BaseModel):
    publication_date_gte: datetime | None
    publication_date_lte: datetime | None
    age_gte: int | None
    age_lte: int | None
    region: list[str] | None
    specialization: list[str] | None
    gender: list[str] | None
