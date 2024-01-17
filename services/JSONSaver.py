import json
import os


class WorkWithJson:
    """
    Класс для работы с файлами json
    """

    @staticmethod
    def json_saver(filename, all_vacancies) -> None:
        """
        Метод, который записывает в файл вакансии
        :param filename:                          # забыла что тут
        :param all_vacancies: список с вакансиями
        :return: None
        """
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)

    @staticmethod
    def json_read(filename) -> dict:
        """
        Открывает файл на чтение
        :return: файл с вакансиями в формсате json
        """
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    @staticmethod
    def json_delete(filename) -> None:
        """
        Метод, который удаляет файл
        :param filename: название файла
        :return: None
        """
        os.remove(filename)
