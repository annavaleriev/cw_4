from typing import Any

import requests

from services.api_abc import API
from settings import URL_SJ, SJ_API_KEY, COUNT_VACANCIES_BY_PAGE


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self, keyword: str) -> None:
        self.__keyword: str = keyword
        self.__headers: dict = {"X-Api-App-Id": SJ_API_KEY}
        self.__params: dict = {
            "keyword": self.__keyword,
            "count": COUNT_VACANCIES_BY_PAGE,
            "page": 0,
            "town": 4 # TODO: потом город убрать
        }

    @property
    def url(self) -> str:
        """
        Property для url
        :return: url в виде строки
        """
        return URL_SJ

    def get_response_by_page(self, page: int = 0) -> dict[str, Any]:
        """
        Метод для получения вакансия с сайта SuperJob
        :param page: номер страницы для получения данных
        :return: словарь со списком вакансий в формате json
        """
        self.__params["page"]: dict = page
        return requests.get(self.url, self.__params, headers=self.__headers).json()

    def get_all_vacancies(self) -> list[dict]:
        """
        Метод, для получения списка вакансий по нужным критериям
        :return: список со словарями по всем найденным вакансиям
        """
        all_vacancies: list = []
        page: int = 0
        while True:
            response = self.get_response_by_page(page)
            all_vacancies.extend(response["objects"])
            if not response["more"]:
                break
            page += 1
        return all_vacancies

# test = SuperJobAPI("менеджер")
# # uuu = test.get_all_vacancies()
# # print(uuu)
