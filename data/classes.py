from collections import UserDict
import pickle

class AddressBook(UserDict):
    def __init__(self):
        """
        Ініціалізія AddressBook із лічильником ID користувачів та словником даних.
        """
        self.user_id_counter = 0
        self.data = UserDict()

    # Завантажити адресну книгу з файлу
    def read_from_file(self):
        """
        Зчитатування даних з файлу та повернення екземпляру AddressBook.
        """
        with open('data\\abook.dat', 'rb') as fh:
            return pickle.load(fh)

    # Зберегти адресну книгу у файл
    def save_to_file(self):
        """
        Збереження екземпляру AddressBook у файл.
        """
        with open('data\\abook.dat', 'wb') as fh:
            pickle.dump(self, fh)
    
    def add_record(self, record):
        """
        Додавання нового запису до AddressBook.

        Args:
            record: Запис, який потрібно додати до AddressBook.
        """
        self.data[self.user_id_counter] = record
        self.user_id_counter += 1
    
    def edit_record(self, args):
        """
        Редагування ім'я запису в AddressBook.
        Args:
            args (list): Список, що містить ID запису та нове ім'я.
        """
        self.data[int(args[0])].name.value = args[1]

    def del_record(self, args):
        """
        Видалення запису з AddressBook.

        Args:
            args (list): Список, що містить ID запису, який потрібно видалити.
        """
        self.data.pop(int(args[0]))
