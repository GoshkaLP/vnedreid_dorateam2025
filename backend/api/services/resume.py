from passlib.context import CryptContext

from api.orm import models
from api.repo.resume import ResumeRepo
from api.services.base import BaseService
from api.services.schemas import resume as schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ResumeService(BaseService[models.Resume, schemas.Resume, ResumeRepo]):
    model = models.Resume
    service_schema = schemas.Resume
    repo = ResumeRepo

    def get_count_resume(self, filters: schemas.ResumeFilters) -> schemas.ResumeCount:
        return schemas.ResumeCount(
            count=self.repo(self.session).get_count_resume(filters=filters)
        )
