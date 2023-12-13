import requests

from services.api_abc import API
from settings import URL_SJ, SJ_API_KEY, COUNT_VACANCIES_BY_PAGE


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self, keyword: str):
        self.__keyword = keyword

    @property
    def url(self):
        return URL_SJ

    def get_response_by_page(self, page=0):
        headers = {"X-Api-App-Id": SJ_API_KEY}  # method_name
        params = {
            "keyword": self.__keyword,
            "count": COUNT_VACANCIES_BY_PAGE,
            "page": page,
            "town": 4

        }
        return requests.get(self.url, params, headers=headers).json()

    def get_all_vacancies(self):
        """
        Метод, для получения списка вакансий по нужным критериям
        :return: список со словарями по всем найденным вакансиям
        """
        all_vacancies: list = []
        response = self.get_response_by_page()
        all_vacancies.extend(response["objects"])
        page = 1
        while response["more"]:
            response = self.get_response_by_page(page)
            all_vacancies.extend(response["objects"])
            page += 1
        return all_vacancies


test = SuperJobAPI("менеджер")
uuu = test.get_all_vacancies()
print(uuu)
