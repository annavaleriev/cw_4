import requests

from services_1.api_abc import API
from settings import URL_SJ, SJ_API_KEY


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self, keyword, count):
        self.url = URL_SJ
        self.keyword = keyword
        self.count = count
        # self.page = page

    def get_vacancies(self):
        list_vacancy = []
        headers = {"X-Api-App-Id": SJ_API_KEY}  # method_name
        params = {
            "keyword": self.keyword,
            "count": self.count
            # "page": self.page
        }

        response = requests.get(self.url, params, headers=headers).json()

        for information in response["objects"]:
            name = information.get["profession"]
            salary_from = information.get["payment_from"]
            salary_to = information.get["payment_to"]
            experience = information.get["candidat"]  # требования
            description = information.get["work"]  # описание вакансии
            url = information.get["link"]

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