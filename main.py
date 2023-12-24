from services.JSONSaver import JSONSave
from services.api_hh import HeadHunterAPI
from services.api_sj import SuperJobAPI
from services.vacancy import Vacancy


def user_interaction():
    print(
        "Добро пожаловать в приложение, которое поможет тебе найти вакансии.\n\n"
        "Выберите сайт, с которого хотите получить вакансии:\n1 - HH\n2 - SJ\n3 - оба сайта\n")

    platform = int(input("Введите цифру: "))

    print("\nТеперь напишите ключевое слово для поиска вакансий: ")
    keyword = input().lower()

    print("\nПожалуйста, подождите, мы ищем для вас вакансии.")

    hh_vacancies = []
    superjob_vacancies = []

    if platform in (1, 3):
        hh_api = HeadHunterAPI(keyword)
        hh_vacancies.extend(hh_api.get_all_vacancies())
        # hh_vacancy = Vacancy
        # hh_exemplars = hh_vacancy.get_exemplars_hh(hh_vacancies)
        hh_exemplars = Vacancy.get_exemplars_hh(hh_vacancies)
        for vacancy in hh_exemplars: # идём по списку с экземплярами и выводим
            print(str(vacancy))

    elif platform in (2, 3):
        superjob_api = SuperJobAPI(keyword)
        superjob_vacancies.extend(superjob_api.get_all_vacancies())
        sj_exemplars = Vacancy.get_exemplars_sj(superjob_vacancies)
    else:
        print("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
              "Выберите сайт, с которого хотите получить вакансии:\n1 - HH\n2 - SJ\n3 - оба сайта")
        return

    json_save = JSONSave()
    # json_save.json_saver("вакансии.json", hh_vacancies)
    json_save.json_saver("вакансии.json",  hh_exemplars)


user_interaction()

# all_exemplars = hh_exemplars + sj_exemplars  а это мне куда засунуть?