class Vacancies:
    """
    # Класс для работы с экземплярами класса
    """

    def __init__(self, name_vacancy: str, salary: int, area: str, employment: str, requirements: str):
        self.name_vacancy = name_vacancy
        self.salary = salary
        self.area = area
        self.employment = employment  # тип занятости
        self.requirements = requirements  # требования
        # self.salary_from = salary_from
        # self.salary_to = salary_to
        # self.currency = currency #а что потопм делать если не рубли...где-то надо это проверять. А зачем мне вообще рубли указывать сразу?

    def __gt__(self, other): #True False наверное возвращает
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
        return (f"{self.name_vacancy}\n"
                f"{self.employment}\n"
                f"{self.area}\n"
                f"{self.requirements}\n"
                f"{self.salary}\n\n"
                )

    def __repr__(self):
        return f"{self.__class__.__name__}" #это мне вообще нужно? забыла что там писать
