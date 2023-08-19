class PersonInfo:
    """Базовый класс инвормации о контакте"""
    def __init__(self, surname=None, first_name=None, second_name=None, organization=None, work_number=None,
                 mobile_number=None):

        self.surname = surname
        self.first_name = first_name
        self.second_name = second_name
        self.organization = organization
        self.work_number = work_number
        self.mobile_number = mobile_number

    def input_person_info(self):
        """Функция ввода данных по отдельному контакту."""

        # ввод данных контакта
        self.surname = input("Введите фамилию: ").capitalize()
        self.first_name = input("Введите имя: ").capitalize()
        self.second_name = input("Введите Отчество: ").capitalize()
        self.organization = input("Введите название организации: ").capitalize()
        self.work_number = input("Введите рабочий телефон: ")
        self.mobile_number = input("Введите личный телефон(сотовый): ")

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.second_name} {self.organization}" \
               f" {self.work_number} {self.mobile_number}" + "\n"


class Contacts:
    """Класс действий с контактоми"""
    def found_contact(self):
        """Поиск нужного контакта"""
        person_data = input("Введите ФИО контакта через пробел: ")
        with open("phone_numbers.txt", "r") as file:
            answer = False
            for line in file:
                if str(line).find(str(person_data)) >= 0:
                    answer = True
                    print(f"Вот контакт, который вы искали: {line}")
                    return line

            if answer is False:
                print("Такого контакта не существует! Проверьте правильность ввода!")

    def create_new_contact(self):
        """Создание нового контакта"""

        data = PersonInfo()
        data.input_person_info()
        # запись нового контакта в файл
        with open("phone_numbers.txt", "a") as file:
                file.write(f"{data.surname} {data.first_name} {data.second_name} {data.organization}"
                           f" {data.work_number} {data.mobile_number}" + "\n")

    def show_contacts(self):
        """Отображение всех существующих контактов"""

        with open("phone_numbers.txt", "r") as file:
            for line in file:
                print(line)

    def delete_contact(self):
        """Удаление нужного контакта"""

        lin = Contacts()
        # поиск удаляемого контакта
        found_line = str(lin.found_contact()).strip()

        # удаление контакта
        with open("phone_numbers.txt", "r") as file:
            lines = file.readlines()

        with open("phone_numbers.txt", "w") as file:
            for line in lines:
                if line.strip() != found_line:
                    file.write(line)


c = Contacts()
# c.create_new_contact()
# c.found_contact()
c.delete_contact()
# c.show_contacts()
