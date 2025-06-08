from typing import Any

from sqlalchemy import func, literal_column, select, sql
from sqlalchemy.orm import aliased

from api.orm import models
from api.repo.base import BaseRepo
from api.services.schemas import vacancies as schemas


class VacanciesRepo(BaseRepo[models.Vacancies]):
    model = models.Vacancies

    def _apply_vacancy_filters(
        self, stmt: sql.Select, filters: schemas.VacancyFilters
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

    def get_salary_stats_by_specialization(
        self, filters: schemas.VacancyFilters
    ) -> tuple[Any]:
        stmt = (
            select(
                func.min(self.model.salary_amount).label("min_salary"),
                func.percentile_cont(0.25)
                .within_group(self.model.salary_amount)
                .label("q1_salary"),
                func.percentile_cont(0.5)
                .within_group(self.model.salary_amount)
                .label("median_salary"),
                func.avg(self.model.salary_amount).label("mean_salary"),
                func.percentile_cont(0.75)
                .within_group(self.model.salary_amount)
                .label("q3_salary"),
                func.max(self.model.salary_amount).label("max_salary"),
            )
            .where(self.model.salary_specified == True)
            .where(self.model.salary_amount != None)
        )
        stmt = self._apply_vacancy_filters(stmt=stmt, filters=filters)

        return self.session.execute(stmt).first()

    def get_count_vacancies(self, filters: schemas.VacancyFilters) -> int:
        stmt = select(func.count()).select_from(self.model)
        stmt = self._apply_vacancy_filters(stmt=stmt, filters=filters)
        return self.session.execute(stmt).scalar()

    def get_salary_bins(
        self, bins: int, filters: schemas.VacancyFilters
    ) -> list[tuple[Any]]:
        stats_cte = (
            select(
                func.min(self.model.salary_amount).label("min_salary"),
                func.max(self.model.salary_amount).label("max_salary"),
            )
            .where(self.model.salary_specified == True)
            .where(self.model.salary_amount != None)
            .cte("stats")
        )

        stats = aliased(stats_cte)

        stmt = (
            select(
                func.width_bucket(
                    self.model.salary_amount,
                    stats.c.min_salary,
                    stats.c.max_salary,
                    bins,
                ).label("salary_bin"),
                func.count().label("count"),
                stats.c.min_salary,
                stats.c.max_salary,
            )
            .select_from(self.model)
            .join(stats, literal_column("1=1"))
            .where(self.model.salary_specified == True)
            .where(self.model.salary_amount != None)
            .group_by("salary_bin", stats.c.min_salary, stats.c.max_salary)
            .order_by("salary_bin")
        )
        stmt = self._apply_vacancy_filters(stmt=stmt, filters=filters)

        return self.session.execute(stmt).all()

    def get_specializations(self) -> list[str]:
        stmt = select(self.model.specialization).distinct()
        return self.session.execute(stmt).scalars().all()

    def get_regions(self) -> list[str]:
        stmt = select(self.model.region).distinct()
        return self.session.execute(stmt).scalars().all()

    def get_genders(self) -> list[str]:
        stmt = select(self.model.gender).distinct()
        return self.session.execute(stmt).scalars().all()
