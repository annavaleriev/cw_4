from services.vacancy import Vacancy


def validate_field(field: dict, sub_field: str, default_returning_value):
    """
    Метод, который проверяет, есть ли указанное поле в словаре.
    :param field: словарь с данными о вакансии
    :param sub_field: название поля
    :param default_returning_value: значение по умолчанию
    """
    if field is None or field.get(sub_field) is None:
        return default_returning_value
    return field[sub_field]

    # if isinstance(field, dict) and field.get(sub_field) is None:
    #     return field[sub_field]
    # return default_returning_value


def get_vacancy_hh(all_vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод, который создает список объектов Vacancy на основе данных о вакансиях.
    :param all_vacancies:список со словарями с вакансиями с HeadHunter
    :return: список с экземплярами  класса Vacancy
    """
    list_vacancy: list[Vacancy] = []
    for vacancy in all_vacancies:
        list_vacancy.append(
            Vacancy(
                title=vacancy["name"],
                salary_from=validate_field(vacancy["salary"], "from", 0),
                salary_to=validate_field(vacancy["salary"], "to", 0),
                # experience=validate_field(vacancy["experience"], "name", None),
                experience=vacancy["snippet"]["requirement"],
                responsibility=validate_field(vacancy["snippet"], "responsibility", None),
                url=vacancy["alternate_url"],
                area=validate_field(vacancy["address"], "city", ""),
                employment=validate_field(vacancy["employment"], "name", None),
                currency=validate_field(vacancy["salary"], "currency", None)
            )
        )
    return list_vacancy


def get_vacancy_sj(all_vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод, который создает список объектов Vacancy на основе данных о вакансиях.
    :param all_vacancies: список со словарями с вакансиями с SuperJob
    :return: список с экземплярами  класса Vacancy
    """
    list_vacancy: list[Vacancy] = []
    for vacancy in all_vacancies:
        list_vacancy.append(
            Vacancy(
                title=vacancy["profession"],
                salary_from=vacancy["payment_from"],
                salary_to=vacancy["payment_to"],
                experience=vacancy["candidat"],
                # responsibility=vacancy["work"],
                responsibility=validate_field(vacancy["work"], "title", ""),
                url=vacancy["link"],
                area=validate_field(vacancy["town"], "title", ""),
                employment=validate_field(vacancy["place_of_work"], "title", None),
                currency=vacancy["currency"]
            )
        )
    return list_vacancy


def get_sorted_vacancies_by_salary(list_vacancies: list[dict]) -> list[dict]:
    """
    Метод, который сортирует вакансии по зарплате
    :param list_vacancies: список с вакансиями
    :return: список с отсортированными вакансиями по заработной плате
    """
    list_vacancies.sort(reverse=True)
    return list_vacancies


def get_filtered_vacancies_by_town(list_vacancies: list[dict], town: str) -> list[dict]:
    """
    Метод, который фильтрует вакансии по городу
    :param list_vacancies:
    :param town: город
    :return: список с отфильтрованными вакансиями по городу
    """
    return list(filter(lambda vacancy: town in vacancy.area.lower(), list_vacancies))

