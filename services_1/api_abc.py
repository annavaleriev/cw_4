from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстроктный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self):
        """
        Абстрактный метод для получения вакансий по API
        :return:
        """
        pass

    def add_vacancy(self):
        """
        Абстрактный метод для добавления вакансий
        :return:
        """
        pass

    def select_vacancy(self):
        """
        Абстрактный метод для выбора вакансий
        :return:
        """
        pass
