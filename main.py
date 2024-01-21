from services.JSONSaver import WorkWithJson
from services.api_hh import HeadHunterAPI
from services.api_sj import SuperJobAPI
from services.vacancy import Vacancy
from utils import get_vacancy_hh, get_vacancy_sj, get_sorted_vacancies_by_salary, get_filtered_vacancies_by_town, \
    validate_input, show_vacancies_info


def user_interaction():
    json_save = WorkWithJson("vacancies.json")
    print(
        "Добро пожаловать в приложение, которое поможет тебе найти вакансии.\n\n"
        "Вы хотите получить с сайтов или работать с сохраненными ранее вакансиями?\n"
        "1 - получить с сайтов\n"
        "2 - работать с сохраненными\n")

    choice_text = ("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
                   "1 - получить с сайтов\n"
                   "2 - работать с сохраненными\n")
    platform = validate_input((1, 2), choice_text)

    if platform == 1:
        print("Выберите сайт, с которого хотите получить вакансии:\n1 - HeadHunter\n2 - Superjob\n3 - оба сайта\n")

        choice_text = ("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
                       "Выберите сайт, с которого хотите получить вакансии:\n1 - HeadHunter\n2 "
                       "- Superjob\n3 - оба сайта\n")
        job_site = validate_input((1, 2, 3), choice_text)

        keyword = input("\nТеперь напишите ключевое слово для поиска вакансий: ").lower()

        print("\nПожалуйста, подождите, мы ищем для вас вакансии. Это займет не больше минуты\n")

        list_vacancies_hh: list = []
        list_vacancies_sj: list = []

        if job_site in (1, 3):
            hh_api = HeadHunterAPI(keyword)
            hh_vacancies = hh_api.get_all_vacancies()
            print("Получено вакансий с HeadHunter по всей России", len(hh_vacancies), "\n")
            list_vacancies_hh = get_vacancy_hh(hh_vacancies)

        elif job_site in (2, 3):
            sjb_api = SuperJobAPI(keyword)
            sj_vacancies = sjb_api.get_all_vacancies()
            print("Получено вакансий с SuperJob по всей России", len(sj_vacancies), "\n")
            list_vacancies_sj = get_vacancy_sj(sj_vacancies)

        combined_vacancies = list_vacancies_hh + list_vacancies_sj
        if not combined_vacancies:
            print("По данному запросу вакансий не найдено")
            return
        list_combined_vacancies = []
        for vacancy in combined_vacancies:
            list_combined_vacancies.append(vacancy.to_dict())

        json_save.json_saver(list_combined_vacancies)
        show_vacancies_info(combined_vacancies)

    elif platform == 2:
        combined_vacancies = []
        vacancies = json_save.json_read()
        if len(vacancies) == 0:
            print("В файле нет вакансий")

        for vacancy in vacancies:
            combined_vacancies.append(Vacancy(**vacancy))

        print("Вы хотите отсортировать вакансии по зарплате. Напишите Да или Нет")
        need_sorted_by_salary = input().lower()
        if need_sorted_by_salary == "да":
            combined_vacancies = get_sorted_vacancies_by_salary(combined_vacancies)
        elif need_sorted_by_salary == "нет":
            print("Будут выведены все вакансии без сортировки по зарплате\n")
        else:
            print("Некорректный ввод. Будут выведены все вакансии без сортировки по зарплате\n")
        print("Введите город для фильтрации вакансии или нажмите enter для поиска во всех городах ")
        town = input().lower()
        if town:
            combined_vacancies = get_filtered_vacancies_by_town(combined_vacancies, town)

        show_vacancies_info(combined_vacancies)


user_interaction()
