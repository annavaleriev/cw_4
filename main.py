from services.JSONSaver import WorkWithJson
from services.api_hh import HeadHunterAPI
from services.api_sj import SuperJobAPI
from services.vacancy import Vacancy
from utils import get_vacancy_hh, get_vacancy_sj, get_sorted_vacancies_by_salary, get_filtered_vacancies_by_town


def user_interaction():
    json_save = WorkWithJson()
    print(
        "Добро пожаловать в приложение, которое поможет тебе найти вакансии.\n\n"
        "Вы хотите получить с сайтов или работать с сохраненными ранее вакансиями?\n"
        "1 - получить с сайтов\n"
        "2 - работать с сохраненными\n")
    while True:
        try:
            platform = int(input("Введите цифру: "))
            if platform in (1, 2):
                break
            else:
                print("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
                      "1 - получить с сайтов\n"
                      "2 - работать с сохраненными\n")
        except ValueError:
            print("Вы ввели слово. Вам нужно выбрать число от 1 до 2.\n")
    if platform == 1:

        print("Выберите сайт, с которого хотите получить вакансии:\n1 - HeadHunter\n2 - Superjob\n3 - оба сайта\n")

        while True:
            try:
                job_site = int(input("Введите цифру: "))
                if job_site in (1, 2, 3):
                    break
                else:
                    print("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
                          "Выберите сайт, с которого хотите получить вакансии:\n1 - HeadHunter\n2 "
                          "- Superjob\n3 - оба сайта\n")
            except ValueError:
                print("Вы ввели слово. Вам нужно выбрать число от 1 до 3.\n")

        print("\nТеперь напишите ключевое слово для поиска вакансий: ")
        keyword = input().lower()

        print("\nПожалуйста, подождите, мы ищем для вас вакансии. Это займет не больше минуты\n")

        list_vacancies_hh: list = []
        list_vacancies_sj: list = []

        if job_site in (1, 3):
            hh_api = HeadHunterAPI(keyword)
            hh_vacancies = hh_api.get_all_vacancies()
            print("Получено вакансий с HeadHunter по всей России", len(hh_vacancies), "\n")
            list_vacancies_hh = get_vacancy_hh(hh_vacancies)

        if job_site in (2, 3):
            sjb_api = SuperJobAPI(keyword)
            sj_vacancies = sjb_api.get_all_vacancies()
            print("Получено вакансий с SuperJob по всей России", len(sj_vacancies), "\n")
            list_vacancies_sj = get_vacancy_sj(sj_vacancies)
            # if not list_vacancies_sj:
            #     print("По данному запросу вакансий не найдено")
            # else:
            #     print("Получено вакансий с SuperJob по всей России", len(sj_vacancies), "\n")
            #     list_vacancies_sj = get_vacancy_sj(sj_vacancies)
            # if isinstance(list_vacancies_sj, str):
            #     print(list_vacancies_sj)
            # if not list_vacancies_sj:
            #     print("По данному запросу вакансий не найдено")



            # print(test_sj)

        combined_vacancies: list[Vacancy] = list_vacancies_hh + list_vacancies_sj
        list_combined_vacancies = []
        for vacancy in combined_vacancies:
            list_combined_vacancies.append(vacancy.save_vacancy_to_dict())
        if not combined_vacancies:
            print("По данному запросу вакансий не найдено")
            return

        json_save.json_saver("vacancies.json", list_combined_vacancies)
        for vacancy in combined_vacancies:
            print(vacancy)

    elif platform == 2:
        combined_vacancies = []
        vacancies = json_save.json_read("vacancies.json")
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

        for vacancy in combined_vacancies:
            print(vacancy)

        # hh_vacancy = Vacancy
        # hh_exemplars = hh_vacancy.get_exemplars_hh(hh_vacancies)
        # # hh_exemplars = Vacancy.get_exemplars_hh(hh_vacancies)
        # for vacancy in hh_exemplars: # идём по списку с экземплярами и выводим
        #     print(str(vacancy))


# elif platform in (2, 3):
#     superjob_api = SuperJobAPI(keyword)
#     superjob_vacancies = superjob_api.get_all_vacancies()
#     # sj_exemplars = Vacancy.get_exemplars_sj(superjob_vacancies)
# else:
#     print("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
#           "Выберите сайт, с которого хотите получить вакансии:\n1 - HH\n2 - SJ\n3 - оба сайта")
#     return

# json_save = JSONSave()
# # json_save.json_saver("вакансии.json", hh_vacancies)
# json_save.json_saver("вакансии.json",  hh_exemplars)


user_interaction()

# all_exemplars = hh_exemplars + sj_exemplars  а это мне куда засунуть?
