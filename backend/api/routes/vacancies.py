from typing import Annotated
from api.utils.token_validator import TokenValidator
from api.utils.dto import TokenData
from fastapi import APIRouter, status, Security, Depends
import uuid
from api.orm.session import get_session
from api.services.vacancies import VacanciesService
from api.routes.schemas import vacancies as api_schemas
from api.utils.token_validator import TokenValidator
from api import choices

router = APIRouter(prefix="/api/vacancies", tags=["vacancies"])


@router.get(
    "/salary_stats",
    response_model=api_schemas.VacancySalaryStats,
    status_code=status.HTTP_200_OK,
    summary="Get information of vacancy salary stats with filters",
)
def get_salary_stats_by_specialization():
    with get_session() as session:
        result = VacanciesService(session).get_salary_stats_by_specialization()
        return api_schemas.VacancySalaryStats.from_service_schema(result)


@router.get(
    "/count",
    response_model=api_schemas.VacanciesCount,
    status_code=status.HTTP_200_OK,
    summary="Get vacancies count with filters",
)
def get_count_vacancies():
    with get_session() as session:
        result = VacanciesService(session).get_count_vacancies()
        return api_schemas.VacanciesCount.from_service_schema(result)


@router.get(
    "/summary_llm",
    response_model=api_schemas.VacanciesSummaryLLM,
    status_code=status.HTTP_200_OK,
    summary="Vacancies summary by LLM model with filters",
)
def get_vacancies_summary():
    with get_session() as session:
        result = VacanciesService(session).get_vacancies_summary_llm()
        return api_schemas.VacanciesSummaryLLM.from_service_schema(result)


@router.get(
    "/salary_bins",
    response_model=list[api_schemas.VacanciesSalaryBins],
    status_code=status.HTTP_200_OK,
    summary="Get salary bins with filters",
)
def get_salary_bins():
    with get_session() as session:
        result = VacanciesService(session).get_salary_bins()
        return [
            api_schemas.VacanciesSalaryBins.from_service_schema(row) for row in result
        ]
