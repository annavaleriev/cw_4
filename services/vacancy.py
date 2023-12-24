class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ("title", "salary", "salary_from", "salary_to", "experience", "responsibility",
                 "url", "area", "employment", "currency")

    def __init__(self, title: str, salary: int, salary_from: int,  salary_to: int, experience: str,
                 responsibility: str, url: str, area: str, employment: str, currency: str):
        self.title = title
        self.salary = salary  # зарплата без вилки
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.experience = experience  # требования
        self.responsibility = responsibility  # описание вакансии
        self.url = url
        self.area = area
        self.employment = employment  # тип занятости
        self.currency = currency

    # тут везде фигня с зарплатой её нужно считать как-то. Гдк то нет зп, где-то нет от или до

    @staticmethod
    def get_salary_hh(salary): # мне не нравится salary)...почему он тут я забыла
        """
        Метод, который работант с заработной платой, чтобы можно было её вывести корректно
        :param salary:
        :return:заработную плату для пользователя
        """
        if salary is None:
            return "Зарплата по договорённости"
        else:
            if salary ["from"] is None:  # Или нужно вот так, я запуталась salary ["salary"]["from"]
                return f" до {salary['to']}"
            elif salary ["to"] is None:
                return f" от {salary['from']}"
            else:
                return f"от {salary['from']} до {salary['to']}"

    @classmethod
    def get_exemplars_hh(cls, all_vacancies):
        """
        Метод, который инициализирует экземпляры класса
        :param all_vacancies:список с вакаесиями
        :return:список с экземплярами класса
        """
        list_of_exemplars = [] #сюда сложу все экземпляры класса
        for vacancy in all_vacancies["items"]: # all_vacancies это список со всеми вакансиями
            exemplar_hh = Vacancy(vacancy["name"], #title
                                  cls.get_salary_hh(vacancy["salary"]),
                                  # vacancy["salary"]["from"], #salary_from
                                  # vacancy["salary"]["to"], # salary_to
                                  vacancy["experience"]["name"],# experience
                                  vacancy["snippet"]["responsibility"], #responsibility
                                  vacancy["alternate_url"], #url
                                  vacancy["address"]["city"], #area
                                  vacancy["employment"]["name"], #employment
                                  vacancy["salary"]["currency"], #currency
                                  )
            list_of_exemplars.append(exemplar_hh)
        return list_of_exemplars

    @staticmethod
    def get_salary_sj(salary): # мне не нравится salary)...почему он тут я забыла
        if salary["payment_from"] is None and salary["payment_to"] is None:
            return "Зарплата по договорённости"
        elif salary["payment_from"] is None:
            return f" до {salary['payment_to']}"
        elif salary["payment_to"] is None:
            return f" от {salary['payment_from']}"
        else:
            return f"от {salary['payment_from']} до {salary['payment_to']}"

    @classmethod
    def get_exemplars_sj(cls, all_vacancies):
        list_of_exemplars = []
        for vacancy in all_vacancies["objects"]:
            try:
                exemplar_sj = Vacancy(vacancy["profession"],  #title готово
                                      cls.get_salary_sj(vacancy), # тут   него нет этого параметра как у HH
                                      # vacancy["salary"]["from"], #salary_from
                                      # vacancy["salary"]["to"], # salary_to
                                      vacancy["candidat"],  # experience , не уверена тк нашла только в описании
                                      vacancy["work"],  # responsibility Готово
                                      vacancy["link"],  # url готово
                                      vacancy["town"]["title"],  # area готово
                                      vacancy["place_of_work"]["title"],  # employment готово
                                      vacancy["currency"],  # currency готово
                                      )
            except KeyError:
                continue
            list_of_exemplars.append(exemplar_sj)
        return exemplar_sj

    def __str__(self) -> str:
        """
        Выводит сообщение для пользователя по вакансии
        :return:строку с данными по вакансии
        """
        return (f"{self.title}\n"
                f"{self.salary_from} - {self.salary_to}\n" # а что делаеть если нет этих значений? а что вообще делать если зп не указано, я вообще это где-то проверяю?
                f"{self.salary}\n" # может это выводить только без вилки?
                f"{self.experience}\n"
                f"{self.experience}\n"
                f"{self.url}\n"
                f"{self.area}\n"
                f"{self.employment}\n"
                f"{self.currency}\n\n"
                f"******************************************************************\n\n"
                )


    # def salary(self):
    #     pass  # тут как-то надо одну зп посчитать
    #
    # def get_vacancies_by_salary(self):
    #     pass
    #
    # # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
    # # такой вывод
    #
    # def delete_vacancy(self):
    #     pass
    #
    # # json_saver.delete_vacancy(vacancy)
    # #  у меня есть ещё методы в  class API
    #
    # @staticmethod
    # def get_top_vacancy(list_vacancy, top_n):
    #     """
    #     Метод, который возвращается пользователю топ вакансий
    #     :param list_vacancy:
    #     :param top_n:
    #     :return:
    #     """
    #     return list_vacancy[:top_n]
    # # list_vacancy - это  в классах сайтов, а top_n должен ввести пользовтаель где-то
    #
    # def get_sorted_vacancy_salary(self, list_vacancy):
    #     """
    #     Снвчвла большая зарплата
    #     :param list_vacancy:
    #     :return:
    #     """
    #
    #     list_vacancy.sort(key=lambda vacancy: vacancy.salary_from, reverse=True)
    #     list_vacancy.sort(key=lambda vacancy: vacancy.salary_to, reverse=True)
    #     # list_vacancy.sort(key=lambda vacancy: vacancy.currency, reverse=True)
    #
    #     # а если нет зп?
    #
    # # def sort_operations(self, executed_operations: list[dict]) -> list[dict]:
    # #     """
    # #      сортирует список операций по дате
    # #     :return: список операций "EXECUTED" отсортированный с конца
    # #     """
    # #     return sorted(executed_operations, key=lambda operation: operation.get("date"), reverse=True)
    #
    # def __gt__(self, other):  # True False наверное возвращает
    #     """
    #     Метод, который сравнивает заработные платы какая больше
    #     :param other:
    #     :return:
    #     """
    #     return self.salary > other.salary
    #
    # def __lt__(self, other):
    #     """
    #     Метод, который сравнивает заработные платы какая меньше
    #     :param other:
    #     :return:
    #     """
    #     return self.salary < other.salary
    #

    # def __repr__(self):
    #     pass
