from fastapi import APIRouter, status

from api.orm.session import get_session
from api.routes.schemas import vacancies as api_schemas
from api.services.vacancies import VacanciesService

router = APIRouter(prefix="/api/vacancies/filters", tags=["vacancies_filters"])


@router.get(
    "/specializations",
    response_model=list[api_schemas.VacancySpecialization],
    status_code=status.HTTP_200_OK,
    summary="Get list of specializations",
)
def get_specializations():
    with get_session() as session:
        result = VacanciesService(session).get_specializations()
        return [
            api_schemas.VacancySpecialization.from_service_schema(row) for row in result
        ]


@router.get(
    "/regions",
    response_model=list[api_schemas.VacancyRegion],
    status_code=status.HTTP_200_OK,
    summary="Get list of regions",
)
def get_regions():
    with get_session() as session:
        result = VacanciesService(session).get_regions()
        return [api_schemas.VacancyRegion.from_service_schema(row) for row in result]


@router.get(
    "/genders",
    response_model=list[api_schemas.VacancyGender],
    status_code=status.HTTP_200_OK,
    summary="Get list of genders",
)
def get_genders():
    with get_session() as session:
        result = VacanciesService(session).get_genders()
        return [api_schemas.VacancyGender.from_service_schema(row) for row in result]


@router.post(
    "/regions",
    status_code=status.HTTP_200_OK,
    summary="Add new region",
)
def add_region():
    with get_session() as session:
        return VacanciesService(session).add_region()


@router.post(
    "/specializations",
    status_code=status.HTTP_200_OK,
    summary="Add new specialization",
)
def add_specialization():
    with get_session() as session:
        return VacanciesService(session).add_specialization()
