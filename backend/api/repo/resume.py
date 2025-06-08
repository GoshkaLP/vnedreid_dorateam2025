from sqlalchemy import func, select, sql

from api.orm import models
from api.repo.base import BaseRepo
from api.services.schemas import resume as schemas


class ResumeRepo(BaseRepo[models.Resume]):
    model = models.Resume

    def _apply_resume_filters(
        self, stmt: sql.Select, filters: schemas.ResumeFilters
    ) -> sql.Select:
        if filters.region:
            stmt = stmt.where(self.model.region.in_(filters.region))
        if filters.specialization:
            stmt = stmt.where(self.model.specialization.in_(filters.specialization))
        if filters.gender:
            stmt = stmt.where(self.model.gender.in_(filters.gender))
        if filters.publication_date_gte:
            stmt = stmt.where(self.model.vacancy_date >= filters.publication_date_gte)
        if filters.publication_date_lte:
            stmt = stmt.where(self.model.vacancy_date <= filters.publication_date_lte)
        if filters.age_gte:
            stmt = stmt.where(self.model.age >= filters.age_gte)
        if filters.age_lte:
            stmt = stmt.where(self.model.age <= filters.age_lte)
        return stmt

    def get_count_resume(self, filters: schemas.ResumeFilters) -> int:
        stmt = select(func.count()).select_from(self.model)
        stmt = self._apply_resume_filters(stmt=stmt, filters=filters)
        return self.session.execute(stmt).scalar()
