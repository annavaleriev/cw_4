from abc import ABC, abstractmethod
from typing import Any


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def __init__(self, keyword: str):
        self.__keyword: str = keyword

    @property
    @abstractmethod
    def url(self):
        raise NotImplementedError

    @abstractmethod
    def get_response_by_page(self, page: int) -> dict[str, Any]:
        """
        Метод для получения вакансия с API
        :param page: номер страницы для получения данных
        :return: словарь со списком вакансий в формате json
        """
        raise NotImplementedError

    @abstractmethod
    def get_all_vacancies(self) -> dict[str, Any]:
        """
        Метод, для получения списка вакансий по всем страницам
        :return: список со словарями по всем найденным вакансиям
        """
        raise NotImplementedError
