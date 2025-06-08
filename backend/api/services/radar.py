from passlib.context import CryptContext

from api.orm import models
from api.repo.radar import RadarRepo
from api.services.base import BaseService
from api.services.schemas import radar as schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class RadarService(BaseService[models.Radar, schemas.Radar, RadarRepo]):
    model = models.Radar
    service_schema = schemas.Radar
    repo = RadarRepo

    def get_company_benifits(
        self, filters: schemas.RadarFilters
    ) -> list[schemas.BenifitsCompany]:
        data = self.repo(self.session).get_company_benifits(filters=filters)
        return [
            schemas.BenifitsCompany(company=row[0], benifits=list(row[1:]))
            for row in data
        ]
