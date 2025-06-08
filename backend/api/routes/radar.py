from typing import Annotated

from fastapi import APIRouter, Query, status

from api.orm.session import get_session
from api.routes.schemas import benifits as api_schemas
from api.services.radar import RadarService

router = APIRouter(prefix="/api/benifits", tags=["benifits"])


@router.get(
    "/radar",
    response_model=list[api_schemas.BenifitsCompany],
    status_code=status.HTTP_200_OK,
    summary="Get company benifits with filters",
)
def get_benifits_by_company(filters: Annotated[api_schemas.RadarFilters, Query()]):
    with get_session() as session:
        result = RadarService(session).get_company_benifits(filters=filters)
        return [api_schemas.BenifitsCompany.from_service_schema(row) for row in result]
