from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def get_vacancies_by_page(self, page):
        """
        Абстрактный метод для получения вакансий по API
        :return:
        """
        pass

    @abstractmethod
    def get_count_pages(self):
        pass

    @abstractmethod
    def get_all_vacancies(self):
        pass