import json
import os


class JsonDataService:
    """
    Класс для работы с файлами json
    """
    def __init__(self, filename):
        self.filename = filename

    def saver(self, all_vacancies) -> None:
        """
        Метод, который записывает в файл вакансии
        :param all_vacancies: список с вакансиями
        :return: None
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)

    def read(self) -> dict:
        """
        Открывает файл на чтение
        :return: файл с вакансиями в формате json
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def json_delete(self) -> None:
        """
        Метод, который удаляет файл
        :return: None
        """
        os.remove(self.filename)
