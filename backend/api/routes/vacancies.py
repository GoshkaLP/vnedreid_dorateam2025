from typing import Annotated

from fastapi import APIRouter, Query, status

from api.orm.session import get_session
from api.routes.schemas import vacancies as api_schemas
from api.services.vacancies import VacanciesService

router = APIRouter(prefix="/api/vacancies", tags=["vacancies"])


@router.get(
    "/salary_stats",
    response_model=api_schemas.VacancySalaryStats,
    status_code=status.HTTP_200_OK,
    summary="Get information of vacancy salary stats with filters",
)
def get_salary_stats_by_specialization(
    filters: Annotated[api_schemas.VacancyFilters, Query()],
):
    with get_session() as session:
        result = VacanciesService(session).get_salary_stats_by_specialization(
            filters=filters
        )
        return api_schemas.VacancySalaryStats.from_service_schema(result)


@router.get(
    "/count",
    response_model=api_schemas.VacanciesCount,
    status_code=status.HTTP_200_OK,
    summary="Get vacancies count with filters",
)
def get_count_vacancies(filters: Annotated[api_schemas.VacancyFilters, Query()]):
    with get_session() as session:
        result = VacanciesService(session).get_count_vacancies(filters=filters)
        return api_schemas.VacanciesCount.from_service_schema(result)


@router.get(
    "/summary_llm",
    response_model=api_schemas.VacanciesSummaryLLM,
    status_code=status.HTTP_200_OK,
    summary="Vacancies summary by LLM model with filters",
)
def get_vacancies_summary(filters: Annotated[api_schemas.VacancyFilters, Query()]):
    with get_session() as session:
        result = VacanciesService(session).get_vacancies_summary_llm(filters=filters)
        return api_schemas.VacanciesSummaryLLM.from_service_schema(result)


@router.get(
    "/salary_bins",
    response_model=list[api_schemas.VacanciesSalaryBins],
    status_code=status.HTTP_200_OK,
    summary="Get salary bins with filters",
)
def get_salary_bins(filters: Annotated[api_schemas.VacancyFilters, Query()]):
    with get_session() as session:
        result = VacanciesService(session).get_salary_bins(filters=filters)
        return [
            api_schemas.VacanciesSalaryBins.from_service_schema(row) for row in result
        ]
