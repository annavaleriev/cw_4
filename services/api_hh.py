from typing import Any

import requests

from services.api_abc import API
from settings import URL_HH, COUNT_VACANCIES_BY_PAGE


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword: str) -> None:
        self.__keyword: str = keyword

    @property
    def url(self) -> str:
        """
        Property для url
        :return: url в виде строки
        """
        return URL_HH

    def get_response_by_page(self, page=0) -> dict[str, Any]:
        """
        Метод для получения вакансия с сайта HeadHunter
        :param page: номер страницы для получения данных
        :return: словарь со списком вакансий в формате json
        """
        params: dict[str, Any] = {
            "text": self.__keyword,
            "per_page": COUNT_VACANCIES_BY_PAGE,
            "page": page,
        }
        return requests.get(self.url, params).json()

    def get_count_pages(self) -> int:
        """
        Метод для получения общего кол-ва найденных страниц
        :return: число страниц с вакансиями
        """
        return self.get_response_by_page()["pages"]

    def get_all_vacancies(self) -> list[dict]:
        """
        Метод, для получения списка вакансий по нужным критериям
        :return: список со словарями по всем найденным вакансиям
        """
        pages: int = self.get_count_pages()
        all_vacancies: list = []
        for page in range(pages):
            vacancies_by_page: list[dict] = self.get_response_by_page(page)["items"]
            all_vacancies.extend(vacancies_by_page)
        return all_vacancies
