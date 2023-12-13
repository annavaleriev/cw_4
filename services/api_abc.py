from abc import ABC, abstractmethod


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
    def get_response_by_page(self, page):
        """
        Метод для получения вакансия с API
        :param page: номер страницы для получения данных
        :return: словарь со списком вакансий в формате json
        """
        raise NotImplementedError

    @abstractmethod
    def get_all_vacancies(self):
        """
        Метод, для получения списка вакансий по всем страницам
        :return: список со словарями по всем найденным вакансиям
        """
        raise NotImplementedError
