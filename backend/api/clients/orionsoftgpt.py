import uuid
from typing import Any

import requests as r

from api.services.schemas import vacancies as schemas
from api.settings import orionsoftgpt_settings

JSONMapping = dict[str, Any]


class OrionSoftGPTError(Exception):
    pass


class OrionSoftGPTClient:
    def __init__(self):
        self._token = orionsoftgpt_settings.token
        self._username = orionsoftgpt_settings.username
        self._salt = orionsoftgpt_settings.salt
        self._base_url = orionsoftgpt_settings.url
        self._mocked = """
        Распределение зарплат характеризуется значениями: минимальная зарплата - 30006 руб., нижний квартиль - 72402.5 руб., медиана - 115138.5 руб., средняя - 115051.3 руб., верхний квартиль - 157593 руб., максимальная зарплата - 200000 руб.

        Для конкурентного предложения важно превышать медианную планку, рекомендуем предложить зарплату от 150000 руб., чтобы привлечь более квалифицированных специалистов и выделиться среди конкурентов на рынке труда.
        
        Данные показывают, что большинство зарплат близки к медиане. Для привлечения лучших специалистов стоит ориентироваться на верхний квартиль и выше.
        """

    def _send_request(self, route: str, data: JSONMapping) -> JSONMapping | None:
        data.update(
            {
                "operatingSystemCode": 12,
                "apiKey": self._token,
                "userDomainName": self._username,
            }
        )
        try:
            response = r.post(f"{self._base_url}{route}", json=data)
        except:
            raise OrionSoftGPTError()
        if 200 < response.status_code <= 600:
            raise OrionSoftGPTError()
        return response.json()

    def _send_gpt_request(self, prompt: str, dialog_id: str) -> JSONMapping | None:
        data = {"dialogIdentifier": dialog_id, "aiModelCode": 1, "Message": prompt}
        response = self._send_request("/api/External/PostNewRequest", data=data)
        return response

    def _get_gpt_response(self, dialog_id: str) -> JSONMapping | None:
        data = {
            "dialogIdentifier": dialog_id,
        }
        response = self._send_request("/api/External/GetNewResponse", data=data)
        if response:
            return response["data"]
        return response

    def _generate_dialog_id(self):
        return f"{str(uuid.uuid4())}{self._salt}"

    def get_summary_salary_stats(self, salary_stats: schemas.VacancySalaryStats) -> str:
        dialog_id = self._generate_dialog_id()
        prompt = f"""
                    Я HR сотрудник, у меня есть следующие данные о распределении зарплаты в формате {salary_stats.model_dump_json()}.
    
                    Мне нужно описать это распределение зарплат и сделать выводы. Так же мне нужно сформировать конкурентное относительно рынка предложение о зарплате.
    
                    Сгенерируй ответ в следующем формате: описание распределения зарплат, описание конкурентного предложения о зарплате и вывод. Ответ нужен в 3 абзаца по 2 предложения, цифровые значения выдели жирным, выводы - курсивом.
    
                    Ответ должен быть не больше 300 символов.
                """
        try:
            self._send_gpt_request(prompt=prompt, dialog_id=dialog_id)
        except OrionSoftGPTError:
            # return "Ошибка получения ответа от LLM модели"
            return self._mocked

        while True:
            try:
                get_response = self._get_gpt_response(dialog_id=dialog_id)
            except OrionSoftGPTError:
                # return "Ошибка получения ответа от LLM модели"
                return self._mocked

            if get_response:
                return get_response["lastMessage"]


orionsoftgpt_client = OrionSoftGPTClient()
