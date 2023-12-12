from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def get_response(self):
        """
        Метод для получения вакансия с сайта HeadHunter
        :return: словарь со списком вакансий в формате json
        """
        pass

    @abstractmethod
    def get_vacancies_by_page(self):
        pass

    @abstractmethod
    def get_count_pages(self):
        """
        Метод для получения общего кол-ва найденных страниц
        :return: число страниц с вакансиями
        """
        pass

    @abstractmethod
    def get_all_vacancies(self):
        """
        Метод, для получения списка вакансий по нужным критериям
        :return: список со словарями по всем найденным вакансиям
        """
        pass
