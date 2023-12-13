import json
from abc import ABC, abstractmethod


class JsonOperations(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    @abstractmethod
    def add_vacancy(self,vacancy):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass


class WorkWithJson(JsonOperations):
    """
    Класс,который добавляет и читает вакансии
    """
    def __init__(self):
        self.file = "list_vacancies,json"

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансси в файл
        :param vacancy:
        :return:
        """
        # with open (self.file, "a", encoding="utf-8") as file:
#         #     file.write(json.dump(vacancy, indent=2, ensure_ascii=False))
        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(vacancy,file,  indent=2, ensure_ascii=False)


    def get_vacancy(self):
        with open(self.file, "r", encoding="utf-8" ) as file:



