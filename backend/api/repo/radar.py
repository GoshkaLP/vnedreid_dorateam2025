from typing import Any

from sqlalchemy import case, func, select, sql

from api.orm import models
from api.repo.base import BaseRepo
from api.services.schemas import radar as schemas


class RadarRepo(BaseRepo[models.Radar]):
    model = models.Radar

    def _apply_resume_filters(
        self, stmt: sql.Select, filters: schemas.RadarFilters
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

    def get_company_benifits(self, filters: schemas.RadarFilters) -> list[tuple[Any]]:
        stmt = select(
            self.model.company,
            func.sum(case((self.model.medical_insurance == True, 1), else_=0)).label(
                "medical_insurance"
            ),
            func.sum(case((self.model.meal == True, 1), else_=0)).label("meal"),
            func.sum(case((self.model.gym == True, 1), else_=0)).label("gym"),
            func.sum(case((self.model.flexible_schedule == True, 1), else_=0)).label(
                "flexible_schedule"
            ),
            func.sum(case((self.model.training == True, 1), else_=0)).label("training"),
        ).group_by(self.model.company)

        stmt = self._apply_resume_filters(stmt=stmt, filters=filters)
        return self.session.execute(stmt).all()
