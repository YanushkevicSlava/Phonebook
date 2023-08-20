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

    def input_person_info(self) -> None:
        """Функция ввода данных по отдельному контакту."""

        # ввод данных контакта и проверка вводимых данных на соответствие стандартам.
        while True:
            self.surname = input("Введите фамилию: ").capitalize()
            if self.surname.isalpha():
                break
            else:
                print("Фамилия должна состоять из букв! Проверьте правильность ввода!")
        while True:
            self.first_name = input("Введите имя: ").capitalize()
            if self.first_name.isalpha():
                break
            else:
                print("Имя должно состоять из букв! Проверьте правильность ввода!")
        while True:
            self.second_name = input("Введите Отчество: ").capitalize()
            if self.second_name.isalpha():
                break
            else:
                print("Отчество должно состоять из букв! Проверьте правильность ввода!")
        self.organization = input("Введите название организации: ")
        while True:
            self.work_number = input("Введите рабочий телефон: ")
            if self.work_number.isdigit() and len(self.work_number) == 5:
                break
            else:
                print("Рабочий номер должен состоять из цифр и быть длинной в 5 цифр! Проверьте правильность ввода!")
        while True:
            self.mobile_number = input("Введите личный телефон(сотовый): ")
            if self.mobile_number.isdigit() and len(self.mobile_number) == 7:
                break
            else:
                print("Мобильный номер должен состоять из цифр и быть длинной в 7 цифр!"
                      " Проверьте правильность ввода!")

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.second_name} {self.organization}" \
               f" {self.work_number} {self.mobile_number}" + "\n"


class Contacts:
    """Класс действий с контактоми"""

    def found_contact(self) -> str:
        """Поиск нужного контакта"""

        person_data = (input("Введите ФИО контакта через пробел: ")).title().split()
        with open("phone_numbers.txt", "r", encoding="utf-8") as file:
            answer = False
            for line in file:
                fio = line.split()
                if fio[:3] == person_data:
                    answer = True
                    print(f"Вот контакт, который вы искали: {line}")
                    return line

            if answer is False:
                print("Такого контакта не существует! Проверьте правильность ввода!")

    def create_new_contact(self) -> None:
        """Создание нового контакта"""

        data = PersonInfo()
        data.input_person_info()
        # запись нового контакта в файл.
        with open("phone_numbers.txt", "a", encoding="utf-8") as file:
            file.write(f"{data.surname} {data.first_name} {data.second_name} орг.:{data.organization};"
                       f" рабочий телефон:{data.work_number};"
                       f" личный телефон(сотовый):{data.mobile_number};" + "\n")
            print("Новый контакт добавлен!")

    def show_contacts(self) -> None:
        """Отображение всех существующих контактов"""

        # вывод списка контактов.
        with open("phone_numbers.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line)

    def delete_contact(self) -> None:
        """Удаление нужного контакта"""

        cont = Contacts()
        # поиск удаляемого контакта.
        found_line = str(cont.found_contact()).strip()

        # удаление контакта.
        with open("phone_numbers.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open("phone_numbers.txt", "w", encoding="utf-8") as file:
            for line in lines:
                if line.strip() != found_line:
                    file.write(line)
                else:
                    print("Контакт был удалён!")

    def edit_contact(self) -> None:
        """Находит нужный контакт заменяет данные на необходимые"""

        contact = Contacts()

        while True:
            # поиск необходиемого контакта.
            found_line = str(contact.found_contact()).strip()
            if len(found_line) > 30:
                # ввод новых данных о контакте.
                edited_information = str(input("Введите изменённые данные о контакте через пробел: ")).strip()

                # перезапись контакта.
                with open("phone_numbers.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()

                with open("phone_numbers.txt", "w", encoding="utf-8") as f:
                    for line in lines:
                        if line.strip() == found_line:
                            f.write(f"{edited_information}" + "\n")
                        else:
                            f.write(line)
                    break


class Main:
    """Класс предоставляющий выполнение операций по телефонной книге"""

    def menu(self) -> None:
        """Основное меню"""

        contact = Contacts()

        while True:
            # список существующих режимов.
            print("Для выбора режима введите необходимое значение:")
            print("--- 1 для вывода всех контактов на экран;")
            print("--- 2 для довавления нового контакта в справочник;")
            print("--- 3 для поиска необходимого контакта;")
            print("--- 4 для удаление контакта;")
            print("--- 5 для редактирования необходимого контакта;")
            print("--- 6 для выхода из программы;")
            # выбор режима.
            mode_selection = input("Введите номер режима: ")
            if mode_selection == "1":
                print("Вот все существующие контакты на данный момент: ")
                contact.show_contacts()
            elif mode_selection == "2":
                print("Вы находитесь в режиме добавления нового контакта.")
                contact.create_new_contact()
            elif mode_selection == "3":
                print("Вы находитесь в режиме поиска контакта.")
                contact.found_contact()
            elif mode_selection == "4":
                print("Вы находитесь в режиме удаления контакта.")
                contact.delete_contact()
            elif mode_selection == "5":
                print("Вы находитесь в режиме редактирования контакта.")
                contact.edit_contact()
            elif mode_selection == "6":
                print("Спасибо, что пользуетесь нашей телефонной книгой! До свидания!")
                break
            else:
                print("Такой команды не существует! Попробуйте ещё!")


if __name__ == "__main__":
    run = Main()
    run.menu()
