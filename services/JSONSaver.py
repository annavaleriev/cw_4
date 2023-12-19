import json

from services.api_abc import API


class JSONSaver(API):
    """
    Класс для работы с файлами json
    """

    def json_saver(self, filename):
        """
        Запись в файл вакансий
        :param filename:
        :return:
        """
        all_vacancies = self.get_all_vacancies()

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)

    @staticmethod
    def json_read(filename):
        """
        Открывает файл на чтение
        :return:
        """
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

# import json
#
#
# class JSONSaver:
#     """
#     Класс для работы с файлами json
#     """
#
#     def __init__(self, test):
#         self.test = test
#
#     def json_saver(self, filename):
#         """
#         Запись в файл вакансий
#         :param filename:
#         :return:
#         """
#         all_vacancies = self.test.get_all_vacancies()
#
#         with open(filename, "w", encoding="utf-8") as file:
#             json.dump(all_vacancies, file, indent=2, ensure_ascii=False)
#
#     @staticmethod
#     def json_read(filename):
#         """
#         Открывает файл на чтение
#         :return:
#         """
#         with open(filename, "r", encoding="utf-8") as file:
#             data = json.load(file)
#         return data
