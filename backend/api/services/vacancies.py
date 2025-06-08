from passlib.context import CryptContext

from api.clients.openrouterai import openrouter_client
from api.orm import models
from api.repo.vacancies import VacanciesRepo
from api.services.schemas import vacancies as schemas
from api.services.base import BaseService
from api.repo import exceptions as repo_exc
from api.services import exceptions as service_exc
from api import choices
from api.utils.jwt_tool import jwt_tool

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class VacanciesService(BaseService[models.Vacancies, schemas.Vacancies, VacanciesRepo]):
    model = models.Vacancies
    service_schema = schemas.Vacancies
    repo = VacanciesRepo

    # TODO add payload for filters
    def get_salary_stats_by_specialization(self) -> schemas.VacancySalaryStats:
        data = self.repo(self.session).get_salary_stats_by_specialization()
        return schemas.VacancySalaryStats(
            min_salary=data[0],
            q1_salary=data[1],
            median_salary=data[2],
            mean_salary=data[3],
            q3_salary=data[4],
            max_salary=data[5],
        )

    def get_count_vacancies(self) -> schemas.VacanciesCount:
        return schemas.VacanciesCount(
            count=self.repo(self.session).get_count_vacancies()
        )

    def get_vacancies_summary_llm(self) -> schemas.VacanciesSummaryLLM:
        stats = self.get_salary_stats_by_specialization()
        llm_response = openrouter_client.get_summary_salary_stats(salary_stats=stats)
        return schemas.VacanciesSummaryLLM(response=llm_response)

    def get_salary_bins(self) -> list[schemas.VacanciesSalaryBins]:
        bins = 30
        data = self.repo(self.session).get_salary_bins(bins=bins)
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
