from collections import UserDict
import re
import datetime
import pickle

# Обробка випадку, коли номер телефону не знайдено у записі
class PhoneNotFindError(Exception):
    pass

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


# class нотатки користувача
class Note:
    def __init__(self, nbook, content):
        """
        Ініціалізація об'єкта Note з контентом, тегами та датою створення.

        Args:
            content (str): Зміст нотатки.
            tags (list): Список тегів, пов'язаних із нотаткою.
        """
        self.note_id = nbook.note_id_counter
        self.content = content
        self.tags = list()
        self.creation_date = datetime.datetime.now()
    
    def add_tag(self, tag):
        new_tag = True
        for t in self.tags:
            if t == tag:
                new_tag = False
        if new_tag:
            self.tags.append(tag)
    
    # Видалення тега з запису
    def remove_tag(self, tag):
        find_tag = False
        for t in self.tags:
            if t == tag:
                find_tag = True
        if find_tag:
            self.tags.remove(tag)
        else:
            raise PhoneNotFindError

    def searchstring(self):
        tags_line = f"{' '.join(p for p in self.tags)}" if self.tags else ""
        res = f"{self.content} " + tags_line
        return res.lower()
    
    def search_tag(self):
        res = f"{' '.join(p for p in self.tags)}" if self.tags else ""
        return res.lower()

    def __str__(self):
        #return f"ID: {self.note_id:^3}. DATE: {self.creation_date.strftime('%d.%m.%Y %H:%M')}. NOTE: {self.content} [Tags: {', '.join(self.tags)}]"
        return f"ID: {self.note_id:^3}| Tags: {', '.join(self.tags):>20} | {self.content:<70}"
    
    # NoteBook class
    
class NoteBook(UserDict):
    def __init__(self):
        """
        Ініціалізація блокнота з лічильником ID користувача та словником даних.
        """
        self.note_id_counter = 0
        self.data = UserDict()
        self.max_tags_len = 5 + 2


    def add_record(self,note):
        """
        Додавання нової нотатки до блокнота.
            Args:
            note: Запис, який потрібно додати до блокнота.
        """
        self.data[self.note_id_counter] = note
        self.note_id_counter += 1


    def read_from_file(self):
        """
        Зчитування даних з файлу та повернення екземпляра Адресної книги.
        """
        with open('data\\nbook.dat', 'rb') as fh:
            return pickle.load(fh)


    def save_to_file(self):
        """
        Збереження екземпляра блокнота у файл.
        """
        with open('data\\nbook.dat', 'wb') as fh:
            pickle.dump(self, fh)


    def edit_record(self, args):
        """
        Редагування імені запису в Адресній книзі.
            Args:
            args (list): Список, що містить ID запису та нове ім'я.
        """
        self.data[int(args[0])].content = (' '.join(args[1:]))


    def del_note(self, args):
        """
        Видалення нотатки з блокнота.
            Args:
            args (list): Список, що містить ID запису для видалення.
        """
        self.data.pop(int(args[0]))


