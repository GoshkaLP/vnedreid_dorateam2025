from openai import OpenAI

from api.settings import openrouter_settings
from api.services.schemas import vacancies as schemas


class OpenrouterClient:
    def __init__(self):
        self._token = openrouter_settings.token
        self._client = OpenAI(
            base_url=openrouter_settings.url,
            api_key=self._token,
        )

    def get_summary_salary_stats(self, salary_stats: schemas.VacancySalaryStats) -> str:
        prompt = f"""
            Я HR сотрудник, у меня есть следующие данные о распределении зарплаты в формате {salary_stats.model_dump_json()}.
            
            Мне нужно описать это распределение зарплат и сделать выводы. Так же мне нужно сформировать конкурентное относительно рынка предложение о зарплате.
            
            Сгенерируй ответ в следующем формате: описание распределения зарплат, описание конкурентного предложения о зарплате и вывод. Ответ нужен в 3 абзаца по 2 предложения, цифровые значения выдели жирным, выводы - курсивом.
            
            Ответ должен быть не больше 300 символов.
        """
        completion = self._client.chat.completions.create(
            extra_body={},
            model=openrouter_settings.model,
            messages=[{"role": "user", "content": prompt}],
        )
        try:
            return completion.choices[0].message.content
        except Exception:
            return "Ошибка получения ответа от LLM модели"


openrouter_client = OpenrouterClient()
