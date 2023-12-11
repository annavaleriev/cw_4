from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def get_response(self):
        pass

    @abstractmethod
    def get_vacancies_by_page(self):
        pass

    @abstractmethod
    def get_count_pages(self):
        pass

    @abstractmethod
    def get_all_vacancies(self):
        pass
