from passlib.context import CryptContext

from api.clients.openrouterai import openrouter_client
from api.orm import models
from api.repo.vacancies import VacanciesRepo
from api.services.base import BaseService
from api.services.schemas import vacancies as schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class VacanciesService(BaseService[models.Vacancies, schemas.Vacancies, VacanciesRepo]):
    model = models.Vacancies
    service_schema = schemas.Vacancies
    repo = VacanciesRepo

    # TODO add payload for filters
    def get_salary_stats_by_specialization(
        self, filters: schemas.VacancyFilters
    ) -> schemas.VacancySalaryStats:
        data = self.repo(self.session).get_salary_stats_by_specialization(
            filters=filters
        )
        return schemas.VacancySalaryStats(
            min_salary=data[0],
            q1_salary=data[1],
            median_salary=data[2],
            mean_salary=data[3],
            q3_salary=data[4],
            max_salary=data[5],
        )

    def get_count_vacancies(
        self, filters: schemas.VacancyFilters
    ) -> schemas.VacanciesCount:
        return schemas.VacanciesCount(
            count=self.repo(self.session).get_count_vacancies(filters=filters)
        )

    def get_vacancies_summary_llm(
        self, filters: schemas.VacancyFilters
    ) -> schemas.VacanciesSummaryLLM:
        stats = self.get_salary_stats_by_specialization(filters=filters)
        llm_response = openrouter_client.get_summary_salary_stats(salary_stats=stats)
        return schemas.VacanciesSummaryLLM(response=llm_response)

    def get_salary_bins(
        self, filters: schemas.VacancyFilters
    ) -> list[schemas.VacanciesSalaryBins]:
        bins = 30
        data = self.repo(self.session).get_salary_bins(bins=bins, filters=filters)
        results = []
        for bin_index, count, min_salary, max_salary in data[:-1]:
            step = (max_salary - min_salary) / bins
            start = min_salary + (bin_index - 1) * step
            end = start + step
            results.append(
                schemas.VacanciesSalaryBins(
                    salary_range=f"{int(start)}–{int(end)}", count=count
                )
            )
        return results

    def get_specializations(self) -> list[schemas.VacancySpecialization]:
        data = self.repo(self.session).get_specializations()
        return [schemas.VacancySpecialization(specialization=row) for row in data]

    def get_regions(self) -> list[schemas.VacancyRegion]:
        data = self.repo(self.session).get_regions()
        return [schemas.VacancyRegion(region=row) for row in data]

    def get_genders(self) -> list[schemas.VacancyGender]:
        data = self.repo(self.session).get_specializations()
        return [schemas.VacancyGender(gender=row) for row in data]
