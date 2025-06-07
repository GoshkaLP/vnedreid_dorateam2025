from typing import Any

from sqlalchemy import sql, select, func, literal_column
from sqlalchemy.orm import joinedload, aliased

from api.orm import models
from api.repo.base import BaseRepo


class VacanciesRepo(BaseRepo[models.Vacancies]):
    model = models.Vacancies

    # TODO add filters to all methods
    def get_salary_stats_by_specialization(self) -> tuple[Any]:
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

        return self.session.execute(stmt).first()

    def get_count_vacancies(self) -> int:
        stmt = select(func.count()).select_from(self.model)
        return self.session.execute(stmt).scalar()

    def get_salary_bins(self, bins: int) -> list[tuple[Any]]:
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

        return self.session.execute(stmt).all()
