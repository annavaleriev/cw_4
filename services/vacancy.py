class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, salary_from: int, salary_to: int, salary: int, experience: str, description: str,
                 url: str, area: str, employment: str, currency: str):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary = salary  # зарплата без вилки
        self.experience = experience  # требования
        self.description = description  # описание вакансии
        self.url = url
        self.area = area
        self.employment = employment  # тип занятости
        self.currency = currency

    def salary(self):
        pass  # тут как-то надо одну зп посчитать

    def get_vacancies_by_salary(self):
        pass

    # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
    # такой вывод

    def delete_vacancy(self):
        pass

    # json_saver.delete_vacancy(vacancy)
    #  у меня есть ещё методы в  class API

    @staticmethod
    def get_top_vacancy(list_vacancy, top_n):
        """
        Метод, который возвращается пользователю топ вакансий
        :param list_vacancy:
        :param top_n:
        :return:
        """
        return list_vacancy[:top_n]
    # list_vacancy - это  в классах сайтов, а top_n должен ввести пользовтаель где-то

    def get_sorted_vacancy_salary(self, list_vacancy):
        """
        Снвчвла большая зарплата
        :param list_vacancy:
        :return:
        """

        list_vacancy.sort(key=lambda vacancy: vacancy.salary_from, reverse=True)
        list_vacancy.sort(key=lambda vacancy: vacancy.salary_to, reverse=True)
        # list_vacancy.sort(key=lambda vacancy: vacancy.currency, reverse=True)

        # а если нет зп?

    # def sort_operations(self, executed_operations: list[dict]) -> list[dict]:
    #     """
    #      сортирует список операций по дате
    #     :return: список операций "EXECUTED" отсортированный с конца
    #     """
    #     return sorted(executed_operations, key=lambda operation: operation.get("date"), reverse=True)

    def __gt__(self, other):  # True False наверное возвращает
        """
        Метод, который сравнивает заработные платы какая больше
        :param other:
        :return:
        """
        return self.salary > other.salary

    def __lt__(self, other):
        """
        Метод, который сравнивает заработные платы какая меньше
        :param other:
        :return:
        """
        return self.salary < other.salary

    def __str__(self) -> str:
        """
        Выводит сообщение для пользователя по вакансии
        :return:строку с данными по вакансии
        """
        return (f"{self.name}\n"
                f"{self.salary_from} - {self.salary_to}\n" # а что делаеть если нет этих значений? а что вообще делать если зп не указано, я вообще это где-то проверяю? 
                f"{self.salary}\n" # может это выводить только без вилки? 
                f"{self.experience}\n"
                f"{self.description}\n"
                f"{self.url}\n"
                f"{self.area}\n"
                f"{self.employment}\n"
                f"{self.currency}\n\n"
                f"******************************************************************\n\n"
                )

    def __repr__(self):
        pass
