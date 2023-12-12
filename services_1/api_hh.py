from typing import Any

import requests

from services_1.api_abc import API
from settings import URL_HH


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword: str):
        self.__url: str = URL_HH
        self.__keyword: str = keyword
        self.params: dict[str, int] = {
            "text": self.__keyword,
            "per_page": 100,
            "page": 0
        }

    def url(self):
        return self.__url

    def keyword(self):
        return self.__keyword

    def get_response(self) -> dict[str, Any]:
        """
        Метод для получения вакансия с сайта HeadHunter
        :return: словарь со списком вакансий в формате json
        """
        return requests.get(self.__url, self.params).json()

    def get_vacancies_by_page(self) -> dict[str, Any]:  # Вроде какая-то лишняя фигня, спрросить у УВ зачем это
        """

        :return:
        """
        return self.get_response()

    def get_count_pages(self) -> int:
        """
        Метод для получения общего кол-ва найденных страниц
        :return: число страниц с вакансиями
        """
        pages = self.get_response()["pages"]
        return pages

    def get_all_vacancies(self) -> list[dict]:
        """
        Метод, для получения списка вакансий по нужным критериям
        :return: список со словарями по всем найденным вакансиям
        """
        pages: int = self.get_count_pages()
        all_vacancies: list = []
        for page in range(pages):
            vacancies_by_page = self.get_vacancies_by_page()["items"]
            all_vacancies.extend(vacancies_by_page)
        return all_vacancies


test = HeadHunterAPI("молоток")
print(test.get_all_vacancies())
# print()
