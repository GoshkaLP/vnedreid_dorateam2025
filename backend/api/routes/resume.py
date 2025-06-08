from typing import Annotated

from fastapi import APIRouter, Query, status

from api.orm.session import get_session
from api.routes.schemas import resume as api_schemas
from api.services.resume import ResumeService

router = APIRouter(prefix="/api/resume", tags=["resume"])


@router.get(
    "/count",
    response_model=api_schemas.ResumeCount,
    status_code=status.HTTP_200_OK,
    summary="Get resume count with filters",
)
def get_count_resume(filters: Annotated[api_schemas.ResumeFilters, Query()]):
    with get_session() as session:
        result = ResumeService(session).get_count_resume(filters=filters)
        return api_schemas.ResumeCount.from_service_schema(result)
