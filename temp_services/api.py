from abc import ABC, abstractmethod
from configparser import ParsingError

import requests

from settings import URL_HH, URL_SJ, SJ_API_KEY


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def get_vacancy(self, keyword):
        """
        Абстрактный метод для получения вакансий по API
        :return:
        """
        pass


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self):
        self.url = URL_HH
        # self.keyword = keyword
        # self.area = area
        # self.url = URL_HH
        # self.params = {
        #     "text": self.keyword,
        #     "area": self.area,
        #     "per_page": 50
        #     # "salary": salary
        #     # "employment":
        # }

    def get_vacancy(self, keyword):
        params = {
            "text": keyword,
            "per_page": 50
        }
        """
        Метод для получения вакансий с HeadHunter
        :return:
        """
        # return requests.get(self.url, self.params)
        response = requests.get(self.url, params)
        if response.status_code != 200:
            raise ParsingError(f"Невозможно найти вакансию")
        # return response.json()
        return response.json()["items"]


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self):
        self.url = URL_SJ
        self.api_key = SJ_API_KEY

    def get_vacancy(self, keyword):
        """
        Метод для получения вакансий с SuperJob
        :return:
        """
        params = {
            "keyword": keyword,
            "count": 50
        }
        headers = {"X-Api-App-Id": SJ_API_KEY}
        # return requests.get(self.url, self.params, headers=headers)
        response = requests.get(self.url, params, headers=headers)
        if response.status_code != 200:
            raise ParsingError(f"Невозможно найти вакансию")
        # return response.json()
        return response.json()["objects"]
