from services.JSONSaver import JSONSave
from services.api_hh import HeadHunterAPI
from services.api_sj import SuperJobAPI


def user_interaction():
    print(
        "Добро пожаловать в приложение, которое поможет тебе найти вакансии.\n\n"
        "Выберите сайт, с которого хотите получить вакансии:\n1 - HH\n2 - SJ\n3 - оба сайта\n")

    platform = int(input("Введите цифру: "))

    print("\nТеперь напишите ключевое слово для поиска вакансий: ")
    keyword = input().lower()

    print("\nПожалуйста, подождите, мы ищем для вас вакансии.")

    if platform in (1, 3):
        hh_api = HeadHunterAPI(keyword)
        hh_vacancies = hh_api.get_all_vacancies()
    elif platform in (2, 3):
        superjob_api = SuperJobAPI(keyword)
        superjob_vacancies = superjob_api.get_all_vacancies()
    else:
        print("Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
              "Выберите сайт, с которого хотите получить вакансии:\n1 - HH\n2 - SJ\n3 - оба сайта")
        return

    json_save = JSONSave()
    json_save.json_saver("jfjfjfj.json", hh_vacancies)


user_interaction()
