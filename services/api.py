from abc import ABC, abstractmethod
from configparser import ParsingError

import requests

from settings import URL_HH, URL_SJ, SJ_KEY


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def get_vacancy(self):
        """
        Абстрактный метод для получения вакансий по API
        :return:
        """
        pass


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, keyword="", area=""):
        self.keyword = keyword
        self.area = area
        self.url = URL_HH
        self.params = {
            "text": self.keyword,
            "area": self.area,
            "per_page": 50
            # "salary": salary
            # "employment":
        }

    def get_vacancy(self):
        """
        Метод для получения вакансий с HeadHunter
        :return:
        """
        # return requests.get(self.url, self.params)
        response = requests.get(self.url, self.params)
        if response.status_code != 200:
            raise ParsingError(f"Невозможно найти вакансию")
        # return response.json()
        return response


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self, keyword=""):
        self.url = URL_SJ
        self.params = {
            "text": keyword,
            "count": 50
        }

    def get_vacancy(self):
        """
        Метод для получения вакансий с SuperJob
        :return:
        """
        headers = {
            "X-Api-App-Id": SJ_KEY
        }
        # return requests.get(self.url, self.params, headers=headers)
        response = requests.get(self.url, self.params, headers=headers)
        if response.status_code != 200:
            raise ParsingError(f"Невозможно найти вакансию")
        # return response.json()
        return response

# test = HeadHunterAPI()
# print(HeadHunterAPI.get_vacancy())
# # test_1 = SuperJobAPI()
# # print(SuperJobAPI.get_vacancy())
