from datetime import date

from api.services.schemas.base import (
    BaseServiceSchema,
    IdCreatedDeletedServiceSchemaMixin,
)
import uuid


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
