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
