from services.JsonDataService import JsonDataService
from services.api_hh import HeadHunterAPI
from services.api_sj import SuperJobAPI
from services.vacancy import Vacancy

from utils import get_vacancy_hh, get_vacancy_sj, get_sorted_vacancies_by_salary, get_filtered_vacancies_by_town, \
    validate_input, show_vacancies_info


class VacancyApp:
    """
    Класс для работы с выбором пользователя по работе с вакансиями
    """
    __option_choice: dict = {
        1: "получить с сайтов",
        2: "работать с сохранёнными ранее вакансиями",
        3: "удалить из файла ранее сохранённые вакансии по заработной плате"
    }

    __job_site_choice: dict = {
        1: "HeadHunter",
        2: "Superjob",
        3: "оба сайта"
    }

    welcome_message: str = ("Добро пожаловать в приложение, которое поможет тебе найти вакансии.\n\n"
                            "Вы хотите получить с сайтов или работать с сохраненными ранее вакансиями?\n")
    wrong_input: str = "Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
    choice_site_message: str = "Выберите сайт, с которого хотите получить вакансии:\n"

    def __init__(self):
        self.json_save = JsonDataService("vacancies.json")
        self.platform: int = self.get_user_choice(self.__option_choice, self.welcome_message, self.wrong_input)

    @staticmethod
    def get_user_choice(choice_dict: dict, choice_message: str, choice_text: str) -> int:
        """
        Метод, который получает выбор пользователя и выдаёт нужное сообщение
        :param choice_dict: словари с вариантами выбора
        :param choice_message: варианты выбора сообщения
        :param choice_text: варианты выбора текст
        :return: циаовое число с выбором пользователя
        """
        choice: str = "\n".join([f"{number}: {text}" for number, text in choice_dict.items()])
        print(f"{choice_message}{choice}")
        return validate_input(tuple(choice_dict.keys()), f"{choice_text}{choice}")

    @staticmethod
    def search_vacancies(job_site: int, keyword: str) -> list:
        """
        Метод, который запускает получение вакансий с сайтов
        :param job_site: сайт, с которого нужно получить вакансии
        :param keyword: ключевое слово для поиска вакансий
        :return: список с вакансиями
        """
        list_vacancies_hh: list = []
        list_vacancies_sj: list = []

        if job_site in (1, 3):
            hh_api = HeadHunterAPI(keyword)
            hh_vacancies: list[dict] = hh_api.get_all_vacancies()
            print("Получено вакансий с HeadHunter", len(hh_vacancies), "\n")
            list_vacancies_hh = get_vacancy_hh(hh_vacancies)

        if job_site in (2, 3):
            sjb_api = SuperJobAPI(keyword)
            sj_vacancies: list[dict] = sjb_api.get_all_vacancies()
            print("Получено вакансий с SuperJob", len(sj_vacancies), "\n")
            list_vacancies_sj = get_vacancy_sj(sj_vacancies)
        return list_vacancies_hh + list_vacancies_sj

    def save_and_show_vacancies(self, combined_vacancies: list) -> None:
        """
        Метод, который сохраняет вакансии в файл и выводит информацию по вакансиям
        :param combined_vacancies:
        :return:None
        """
        if not combined_vacancies:
            print("По данному запросу вакансий не найдено")
            return

        list_combined_vacancies: list[dict] = [vacancy.to_dict() for vacancy in combined_vacancies]
        self.json_save.saver(list_combined_vacancies)
        show_vacancies_info(combined_vacancies)

    def check_empty_file(self) -> None:
        """
        Обратотка случая, когда в файле нет вакансий
        :return: None
        """
        print("В файле нет вакансий.\nПолучите сначала вакансии с сайта и выберите первый пункт меню.\n")
        self.platform = self.get_user_choice(
            self.__option_choice,
            self.welcome_message,
            self.wrong_input
        )
        if self.platform == 1:
            self.platform_choice()
        else:
            print("Этот пункт меню недоступен, так как в файле нет вакансий")
        return

    def platform_choice(self) -> None:
        """
        Метод, который выбирает способ для работы с вакансиями
        :return: None
        """
        if self.platform == 1:
            job_site: int = self.get_user_choice(
                self.__job_site_choice,
                self.choice_site_message,
                self.wrong_input + self.choice_site_message
            )
            keyword: str = input("\nТеперь напишите ключевое слово для поиска вакансий: ").lower()

            print("\nПожалуйста, подождите, мы ищем для вас вакансии. Это займет не больше минуты\n")

            combined_vacancies: list[dict] = self.search_vacancies(job_site, keyword)
            sort_vacancies: list[dict] = self.sort_vacancies(combined_vacancies)
            filter_vacancies_by_town: list[Vacancy] = self.filter_vacancies_by_town(sort_vacancies)
            self.save_and_show_vacancies(filter_vacancies_by_town)

        elif self.platform == 2:
            all_file_vacancies: dict = self.json_save.read()
            if len(all_file_vacancies) == 0:
                self.check_empty_file()
                return

            vacancies_instances: list[Vacancy] = [Vacancy(**vacancy) for vacancy in all_file_vacancies]
            sorted_vacancies: list[Vacancy] = self.sort_vacancies(vacancies_instances)
            filter_vacancies_by_town: list[Vacancy] = self.filter_vacancies_by_town(sorted_vacancies)
            show_vacancies_info(filter_vacancies_by_town)

        elif self.platform == 3:
            while True:
                salary = input("Введите вакансии ниже какой заработной платы хотите удалить: \n")
                if salary.isdigit():
                    salary = int(salary)
                    break
                print("Вы ввели не число")

            self.json_save.delete_by_salary(salary)
            all_file_vacancies: dict = self.json_save.read()
            if len(all_file_vacancies) == 0:
                self.check_empty_file()
                return
            print("Оставшиеся вакансии после удаления вакансий\n")
            vacancies_instances: list[Vacancy] = [Vacancy(**vacancy) for vacancy in all_file_vacancies]
            show_vacancies_info(vacancies_instances)

    @staticmethod
    def sort_vacancies(combined_vacancies: list) -> list:
        """
        Метод, который сортирует вакансии по зарплате
        :param combined_vacancies: список с вакансиями
        :return: отсортированный список по зарплате в зависимости от выбора пользователя
        """
        print("Вы хотите отсортировать вакансии по зарплате. Напишите Да или Нет")
        need_sorted_by_salary: str = input().lower()
        if need_sorted_by_salary == "да":
            return get_sorted_vacancies_by_salary(combined_vacancies)
        else:
            print("Будут выведены все вакансии без сортировки по зарплате\n")
            return combined_vacancies

    @staticmethod
    def filter_vacancies_by_town(combined_vacancies: list) -> list:
        """
        Метод, который фильтрует вакансии по городу
        :param combined_vacancies:cписок с вакансиями
        :return: отфильтрованный список по городу с вакансиями в зависимости от выбора пользователя
        """
        print("Введите город для фильтрации вакансии или нажмите enter для поиска во всех городах ")
        town: str = input().lower()
        if town:
            return get_filtered_vacancies_by_town(combined_vacancies, town)
        else:
            print("Будут выведены все вакансии без фильтрации по городу\n")
            return combined_vacancies
