import requests

from services_1.api_abc import API
from settings import URL_HH


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword):
        self.__url = URL_HH
        self.__keyword = keyword
        self.params = {
            "text": self.__keyword,
            "per_page": 100,
            "page": 0
        }

    @property
    def url(self):
        return self.__url

    @property
    def keyword(self):
        return self.__keyword

    def get_response(self):
        return requests.get(self.__url, self.params).json()

    def get_vacancies_by_page(self):
        return self.get_response()

    def get_count_pages(self):
        pages = self.get_response()["pages"]
        return pages

    def get_all_vacancies(self):
        pages = self.get_count_pages()
        all_vacancies = []
        for page in range(pages):
            vacancies_by_page = self.get_vacancies_by_page()["items"]
            all_vacancies.extend(vacancies_by_page)
        return all_vacancies


test = HeadHunterAPI("пупс")
print(test.get_all_vacancies())
# print()
