import json

from services.vacancy import Vacancy


class JsonDataService:
    """
    Класс для работы с файлами json
    """
    def __init__(self, filename: str):
        self.filename = filename

    def saver(self, all_vacancies: list[dict]) -> None:
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

    def delete_by_salary(self, avg_salary: int) -> None:
        """
        Метод, который удаляет вакансии из файла по заработной плате
        :return: None
        """
        vacancies: dict = self.read()
        vacancies_instances: list[Vacancy] = [Vacancy(**vacancy) for vacancy in vacancies]
        allowed_vacancies: list[Vacancy] = list(filter(lambda vac: vac.avg_salary >= avg_salary, vacancies_instances))
        vacancies_for_write: list[dict] = list(map(lambda vac: vac.to_dict(), allowed_vacancies))
        self.saver(vacancies_for_write)
