import requests

from services_1.api_abc import API
from settings import URL_HH


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword): # а зачем мне коунт? тогда его нужно вводить
        self.url = URL_HH
        self.keyword = keyword

    def get_vacancies_by_page(self, page=0):
        params = {
            "text": self.keyword,
            "per_page": 100,
            "page": page
        }
        dhdhhd = requests.get(self.url, params).json()
        return dhdhhd

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
test.get_all_vacancies()
print()

        #
        # for information in response["item"]:
        #     name = information.get("name")  # название вакансии
        #     salary = information.get("salary")  # ззарплата
        #     if salary is None:
        #         salary_from = 0
        #         salary_to = 0
        #     else:
        #         salary_from = salary.get("from")
        #         if salary_from is None:
        #             salary_from = 0
        #         salary_to = salary.get("to")
        #         if salary_to is None:
        #             salary_to = 0
        #
        #     experience = information.get("experience")["name"]  # требования
        #     description = information.get("snipppet")["requirement"]  # описание вакансии
        #     url = information.get("alternate_url")  # ссылка
        #     # area = # проверить, там какая-то фигня с городом, цифры какие-то
        #     # employment =
        #     # currency = # что делать если не рубли
        #
        #     vacancy = {
        #         "name": name,
        #         "salary_from": salary_from,
        #         "salary_to": salary_to,
        #         "experience ": experience,
        #         "description": description,
        #         "url": url
        #     }
        #
        #     list_vacancy.append(vacancy)
        # return list_vacancy

        # # self.area = area
        # # self.employment = employment  # тип занятости
        # self.currency = currency