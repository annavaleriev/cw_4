from services.JsonDataService import JsonDataService
from services.api_hh import HeadHunterAPI
from services.api_sj import SuperJobAPI
from utils import get_vacancy_hh, get_vacancy_sj, get_sorted_vacancies_by_salary, get_filtered_vacancies_by_town, \
    validate_input, show_vacancies_info


class VacancyApp:
    """
    Класс для работы с выбором пользователя по работе с вакансиями
    """
    __option_choice = {
        1: "получить с сайтов",
        2: "работать с сохраненными"
    }

    __job_site_choice = {
        1: "HeadHunter",
        2: "Superjob",
        3: "оба сайта"
    }

    welcome_message = ("Добро пожаловать в приложение, которое поможет тебе найти вакансии.\n\n"
                       "Вы хотите получить с сайтов или работать с сохраненными ранее вакансиями?\n")
    wrong_input = "Вы ввели неверную цифру. Вам нужно выбрать один из вариантов ниже.\n"
    choice_site_message = "Выберите сайт, с которого хотите получить вакансии:\n"

    def __init__(self):
        self.json_save = JsonDataService("vacancies.json")
        self.platform = self.get_user_choice(self.__option_choice, self.welcome_message, self.wrong_input)

    @staticmethod
    def get_user_choice(choice_dict, choice_message, choice_text):
        choice = "\n".join([f"{number}: {text}" for number, text in choice_dict.items()])
        print(f"{choice_message}{choice}")
        return validate_input(tuple(choice_dict.keys()), f"{choice_text}{choice}")

    @staticmethod
    def search_vacancies(job_site, keyword):
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
            print("Получено вакансий с HeadHunter по всей России", len(hh_vacancies), "\n")
            list_vacancies_hh = get_vacancy_hh(hh_vacancies)

        if job_site in (2, 3):
            sjb_api = SuperJobAPI(keyword)
            sj_vacancies: list[dict] = sjb_api.get_all_vacancies()
            print("Получено вакансий с SuperJob по всей России", len(sj_vacancies), "\n")
            list_vacancies_sj = get_vacancy_sj(sj_vacancies)
        return list_vacancies_hh + list_vacancies_sj

    def save_and_show_vacancies(self, combined_vacancies):
        """
        Метод, который сохраняет вакансии в файл и выводит информацию по вакансиям
        :param combined_vacancies:
        :return:
        """
        if not combined_vacancies:
            print("По данному запросу вакансий не найдено")
            return

        list_combined_vacancies = [vacancy.to_dict() for vacancy in combined_vacancies]
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
            self.save_and_show_vacancies(combined_vacancies)

        elif self.platform == 2:
            combined_vacancies = self.load_saved_vacancies()

            self.sort_vacancies(combined_vacancies)
            self.filter_vacancies_by_town(combined_vacancies)

            show_vacancies_info(combined_vacancies)

    def load_saved_vacancies(self):
        """
        Метод, который загружает сохраненные вакансии
        :return:
        """
        combined_vacancies = []
        vacancies = self.json_save.read()
        if len(vacancies) == 0:
            print("В файле нет вакансий")

        for vacancy in combined_vacancies:
            combined_vacancies.append(vacancy.to_dict())

        return combined_vacancies

    @staticmethod
    def sort_vacancies(combined_vacancies):
        """
        Метод, который сортирует вакансии по зарплате
        :param combined_vacancies:
        :return:
        """
        print("Вы хотите отсортировать вакансии по зарплате. Напишите Да или Нет")
        need_sorted_by_salary = input().lower()
        if need_sorted_by_salary == "да":
            return get_sorted_vacancies_by_salary(combined_vacancies)
        else:
            print("Будут выведены все вакансии без сортировки по зарплате\n")
            return combined_vacancies

    @staticmethod
    def filter_vacancies_by_town(combined_vacancies):
        """
        Метод, который фильтрует вакансии по городу
        :param combined_vacancies:
        :return:
        """
        print("Введите город для фильтрации вакансии или нажмите enter для поиска во всех городах ")
        town: str = input().lower()
        if town:
            return get_filtered_vacancies_by_town(combined_vacancies, town)
        else:
            print("Будут выведены все вакансии без фильтрации по городу\n")
            return combined_vacancies


if __name__ == "__main__":
    vacancy_app = VacancyApp()
    vacancy_app.platform_choice()
