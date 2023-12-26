from services.vacancy import Vacancy


def validate_field(field, sub_field, default_returning_value):
    if field is None or field.get(sub_field) is None:
        return default_returning_value
    return field[sub_field]


def get_vacancy_hh(all_vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод, который создает список объектов Vacancy на основе данных о вакансиях.
    :param all_vacancies:список со словарями с вакансиями с HeadHunter
    :return: список с экземплярами  класса Vacancy
    """
    list_vacancy: list = []
    for vacancy in all_vacancies:
        list_vacancy.append(
            Vacancy(
                title=vacancy["name"],
                salary_from=validate_field(vacancy["salary"], "from", 0),
                salary_to=validate_field(vacancy["salary"], "to", 0),
                experience=validate_field(vacancy["experience"], "name", None),
                responsibility=validate_field(vacancy["snippet"], "responsibility", None),
                url=vacancy["alternate_url"],
                area=validate_field(vacancy["address"], "city", None),
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
    list_vacancy: list = []
    for vacancy in all_vacancies:
        list_vacancy.append(
            Vacancy(
                title=vacancy["profession"],
                salary_from=validate_field(vacancy["payment_from"], None, 0),
                salary_to=validate_field(vacancy["payment_to"], None, 0),
                experience=vacancy["candidat"],
                responsibility=vacancy["work"],
                url=vacancy["link"],
                area=validate_field(vacancy["town"], "title", None),
                employment=validate_field(vacancy["place_of_work"], "title", None),
                # currency=vacancy["currency"]
                currency=validate_field(vacancy["currency"], None, None)
            )
        )
    return list_vacancy
