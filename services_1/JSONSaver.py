import json


class JSONSaver:
    """
    Класс для работы с файлами json
    """
    def __init__(self, path):
        self.path = path  # тут путь к файлу...и какой это путь?
        # Сохранение информации о вакансиях в файл
        # json_saver = JSONSaver()
        # json_saver.add_vacancy(vacancy)
        # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
        # json_saver.delete_vacancy(vacancy)

    def json_saver(self, list_vacancy):
        """
        Запись в файл вакансий
        :param list_vacancy:
        :return:
        """

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(list_vacancy, file, indent=2, ensure_ascii=False)

    def json_read(self):
        """
        Открывает файл на чтение
        :return:
        """
        with open(self.path, "r", encoding="utf-8") as file:
            json.load(file)




