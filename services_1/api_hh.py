import requests

from services_1.api_abc import API
from settings import URL_HH


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword):
        self.url = URL_HH
        self.keyword = keyword

    def get_vacancies_by_page(self, page=0):
        params = {
            "text": self.keyword,
            "per_page": 100,
            "page": page
        }
        response = requests.get(self.url, params).json()
        return response

    def get_count_pages(self):
        params = {
            "text": self.keyword,
            "per_page": 100,
            "page": 0
        }
        response = requests.get(self.url, params).json()
        pages = response["pages"]
        return pages

    def get_all_vacancies(self):
        pages = self.get_count_pages()
        all_vacancies = []
        for page in range(pages):
            vacancies_by_page = self.get_vacancies_by_page(page)["items"]
            all_vacancies.extend(vacancies_by_page)
        return all_vacancies


test = HeadHunterAPI("эскорт")
print(test.get_all_vacancies())
# print()
