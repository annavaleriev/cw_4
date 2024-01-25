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
        2: "работать с сохраненными",
        3: "удалить ранее сохраненные вакансии"
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
        choice: str = "\n".join([f"{number}: {text}" for number, text in choice_dict.items()])
        print(f"{choice_message}{choice}")
        return validate_input(tuple(choice_dict.keys()), f"{choice_text}{choice}")

    @staticmethod
    def search_vacancies(job_site: int, keyword: str) -> list:
        """
        Метод, который получает вакансии с сайтов
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

    def platform_choice(self):
        """
        Метод, который выбирает способ для работы с вакансиями
        :return:
        """
        if self.platform == 1:
            job_site = self.get_user_choice(
                self.__job_site_choice,
                self.choice_site_message,
                self.wrong_input + self.choice_site_message
            )
            keyword = input("\nТеперь напишите ключевое слово для поиска вакансий: ").lower()

            print("\nПожалуйста, подождите, мы ищем для вас вакансии. Это займет не больше минуты\n")

            combined_vacancies = self.search_vacancies(job_site, keyword)
            sort_vacancies = self.sort_vacancies(combined_vacancies)
            filter_vacancies_by_town = self.filter_vacancies_by_town(sort_vacancies)
            self.save_and_show_vacancies(filter_vacancies_by_town)

        elif self.platform == 2:
            combined_vacancies = self.load_saved_vacancies()
            sort_vacancies = self.sort_vacancies(combined_vacancies)
            filter_vacancies_by_town = self.filter_vacancies_by_town(sort_vacancies)
            show_vacancies_info(filter_vacancies_by_town)

        elif self.platform == 3:
            self.json_save.delete()
            print("Вакансии удалены из файла")

            # print("Вы хотите удалить все вакансии и очистить список или по заработной плате или городу?\n"
            #       "Напишите Все или Зарплата или Город")
            # choice: str = input().lower()
            # if choice == "все":
            #     self.json_save.delete()
            #     print("Вакансии удалены из файла")
            # elif choice == "зарплата":
            #     combined_vacancies = self.load_saved_vacancies()
            #     sort_vacancies = self.sort_vacancies(combined_vacancies)
            #     self.save_and_show_vacancies(sort_vacancies)
            # elif choice == "город":
            #     combined_vacancies = self.load_saved_vacancies()
            #     filter_vacancies_by_town = self.filter_vacancies_by_town(combined_vacancies)
            #     self.save_and_show_vacancies(filter_vacancies_by_town)

            # combined_vacancies = self.load_saved_vacancies()
            #
            # self.sort_vacancies(combined_vacancies)
            # self.filter_vacancies_by_town(combined_vacancies)
            #
            # show_vacancies_info(combined_vacancies)

    def load_saved_vacancies(self) -> list:
        """
        Метод, который загружает сохраненные вакансии
        :return: список с вакансиями
        """
        combined_vacancies: list = []
        vacancies: dict = self.json_save.read()
        if len(vacancies) == 0:
            print("В файле нет вакансий")

        for vacancy in vacancies:  # vacancies:
            combined_vacancies.append(vacancy.to_dict())

        return combined_vacancies

    # def load_saved_vacancies(self) -> list:
    #     """
    #     Метод, который загружает сохраненные вакансии
    #     :return: список с вакансиями
    #     """
    #     combined_vacancies: list = []
    #     vacancies: dict = self.json_save.read()
    #     if len(vacancies) == 0:
    #         print("В файле нет вакансий")
    #
    #     for vacancy in vacancies:  # vacancies:
    #         combined_vacancies.append(vacancy.to_class())
    #
    #     return combined_vacancies

    # def load_saved_vacancies(self) -> list:
    #     """
    #     Метод, который загружает сохраненные вакансии
    #     :return: список с вакансиями
    #     """
    #     combined_vacancies: list = []
    #     vacancies: dict = self.json_save.read()
    #     if len(vacancies) == 0:
    #         print("В файле нет вакансий")
    #
    #     for vacancy_key, vacancy_data in vacancies.items():
    #         combined_vacancies.append(vacancy_data.to_class())
    #
    #     return combined_vacancies
    # def load_saved_vacancies(self, combined_vacancies) -> list:
    #     """
    #     Метод, который загружает сохраненные вакансии
    #     :return: список с вакансиями
    #     """
    #     list_combined_vacancies: list = [vacancy.to_dict() for vacancy in combined_vacancies]
    #     vacancies: dict = self.json_save.read()
    #     if len(vacancies) == 0:
    #         print("В файле нет вакансий")
    #
    #     for vacancy in vacancies:  # vacancies
    #         list_combined_vacancies.append(vacancy.to_dict())
    #
    #     return list_combined_vacancies
    #
    # def load_saved_vacancies(self) -> list:
    #     """
    #     Метод, который загружает сохраненные вакансии
    #     :return: список с вакансиями
    #     """
    #     combined_vacancies: list = []
    #     vacancies: dict = self.json_save.read()
    #     if len(vacancies) == 0:
    #         print("В файле нет вакансий")
    #
    #     for vacancy_data in vacancies:
    #         vacancy = Vacancy.create_fron_dict(vacancy_data)
    #         vacancy_dict = vacancy.to_dict()
    #         combined_vacancies.append(vacancy_dict)
    #
    #     return combined_vacancies

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
