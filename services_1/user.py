from services_1.api_hh import HeadHunterAPI
from services_1.api_sj import SuperJobAPI


def user_input():
    keyword = input("Введите клёчевое слово для поиска вакансия: ").lower() # проверку сделать какую-то на буквы
    count = int(input("Сколько вакансий вам показать? ")) # это вообще мне нужно?

    hh_vacancy = HeadHunterAPI(keyword, count)
    superjob_vacancy = SuperJobAPI(keyword, count)

    print(" ")



