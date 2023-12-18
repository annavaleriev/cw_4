from typing import Any

import requests

from services.api_abc import API
from settings import URL_SJ, SJ_API_KEY, COUNT_VACANCIES_BY_PAGE


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self, keyword: str):
        self.__keyword: str = keyword

    @property
    def url(self):
        return URL_SJ

    def get_response_by_page(self, page: int = 0) -> dict[str, Any]:
        """
        Метод для получения вакансия с сайта SuperJob
        :param page: номер страницы для получения данных
        :return: словарь со списком вакансий в формате json
        """
        headers: dict = {"X-Api-App-Id": SJ_API_KEY}  # method_name
        params: dict[str, Any] = {
            "keyword": self.__keyword,
            "count": COUNT_VACANCIES_BY_PAGE,
            "page": page,
            "town": 4
        }
        return requests.get(self.url, params, headers=headers).json()

    # def get_all_vacancies(self) -> list[dict]:
    #     """
    #     Метод, для получения списка вакансий по нужным критериям
    #     :return: список со словарями по всем найденным вакансиям
    #     """
    #     all_vacancies: list = []  # создаем пустой список, туда запишем потом словари с вакансиями
    #     response: dict[str, Any] = self.get_response_by_page() # получаем вакансии с сатй с указанной страницы,
    #     в нашем случае с 0
    #     all_vacancies.extend(response["objects"]) # добавляет найденные словари( 1 словарь = 1 вакансия) в список
    #     # с вакансиями. Всего 100 шт с одной страницы
    #     # all_vacancies.extend(self.get_response_by_page()["objects"])
    #     page: int = 1 # принудительно делаем страницу 1, чтобы с неё пошел отсчет дальше
    #     while response["more"]:
    #         response = self.get_response_by_page(page)
    #         all_vacancies.extend(response["objects"])
    #         page += 1
    #     return all_vacancies

    def get_all_vacancies(self) -> list[dict]:
        """
        Метод, для получения списка вакансий по нужным критериям
        :return: список со словарями по всем найденным вакансиям
        """
        all_vacancies: list = []
        page: int = 0  # как избавится от того, чтобы говорить, что страница 0
        while True:
            response = self.get_response_by_page(page)
            all_vacancies.extend(response["objects"])
            if not response["more"]:
                break
            page += 1
        return all_vacancies


test = SuperJobAPI("менеджер")
uuu = test.get_all_vacancies()
print(uuu)
