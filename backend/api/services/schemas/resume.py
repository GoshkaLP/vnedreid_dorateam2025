from datetime import date, datetime

from pydantic import BaseModel

from api.services.schemas.base import (
    BaseServiceSchema,
    IdCreatedDeletedServiceSchemaMixin,
)


class Resume(BaseServiceSchema, IdCreatedDeletedServiceSchemaMixin):
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


class ResumeCount(BaseServiceSchema):
    count: int | None = None


class ResumeFilters(BaseModel):
    publication_date_gte: datetime | None
    publication_date_lte: datetime | None
    age_gte: int | None
    age_lte: int | None
    region: list[str] | None
    specialization: list[str] | None
    gender: list[str] | None
