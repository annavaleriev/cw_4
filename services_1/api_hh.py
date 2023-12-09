import requests

from services_1.api_abc import API
from settings import URL_HH


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword, count):
        self.url = URL_HH
        self.keyword = keyword
        self.count = count
        # self.page = page

    def get_vacancy(self):
        list_vacancy = []
        params = {
            "text": self.keyword,
            "per_page": self.count
        }
        response = requests.get(self.url, params).json()

        for information in response["item"]:
            name = information.get("name")  # название вакансии
            salary = information.get("salary")  # ззарплата
            if salary is None:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = salary.get("from")
                if salary_from is None:
                    salary_from = 0
                salary_to = salary.get("to")
                if salary_to is None:
                    salary_to = 0

            experience = information.get("experience")["name"]  # требования
            description = information.get("snipppet")["requirement"]  # описание вакансии
            url = information.get("alternate_url")  # ссылка

            vacancy = {
                "name": name,
                "salary_from": salary_from,
                "salary_to": salary_to,
                "experience ": experience,
                "description": description,
                "url": url
            }

            list_vacancy.append(vacancy)
        return list_vacancy

        # # self.area = area
        # # self.employment = employment  # тип занятости
        # self.currency = currency