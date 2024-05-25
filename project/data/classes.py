from collections import UserDict
import re
import datetime
import pickle
import os

# Обробка помилки телефонного номеру, довжина якого не дорівнює Phone.MAX_PHONE_LEN length
class LenPhoneError(Exception):
    pass

# обробка помилки телефону який містить не цифрові символи
class TypePhoneError(Exception):
    pass

# обробка помилки яка з'являтиметься якщо запис про телефон відсутній
class PhoneNotFindError(Exception):
    pass

# обробка помилки яка з'являтиметься якщо запис відсутній в адресній книзі
class RecordNotFindError(Exception):
    pass

# обробка помилки яка з'являтиметься в разі вводу невірного формату даних
class DateFormatError(Exception):
    pass

class TypeEmailError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Birthday(Field):
    def __init__(self, date=None):
            result = re.findall(r'\d\d.\d\d.\d\d\d\d', date)
            if result != []:
                self.value = datetime.date(year=int(date[6:10]), month=int(date[3:5]), day=int(date[0:2]))
            else:
                raise DateFormatError

    def __str__(self) -> str:
        return 'No Data' if self.value == None else self.value.strftime('%d.%m.%Y')
    
class Phone(Field):
    MAX_PHONE_LEN = 10

    def __init__(self, value):
        self.value = value

class Email(Field):
    def __init__(self, value):
        self.value = value

class Record:
    def __init__(self, name, book, birthday=None):
        self.user_id = book.user_id_counter
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = birthday
        self.address = ''

    # Додавання електронної пошти до запису
    def add_email(self, email):
        filteredemail = re.findall(r"[A-Za-z,0-9]{1}[a-z,A-Z,.,_,0-9]{0,}@[a-zA-Z]+[.]{1}[a-z,A-Z,.]{2,}", email)
        if len(filteredemail) > 0 and email[-1] not in ['.',',','/','\\']:
            new_email = True
            for e in self.emails:
                if e.value == filteredemail[0]:
                    new_email = False
            if new_email:
                self.emails.append(Email(filteredemail[0]))
                return True
        else:
            raise TypeEmailError

    # Видалення електронної пошти із запису
    def remove_email(self, email):
        find_email = False
        for e in self.emails:
            if e.value == email:
                find_email = True
                email_to_remove = e
        if find_email:
            self.emails.remove(email_to_remove)
        else:
            raise PhoneNotFindError

    # Редагування електронної пошти в записі
    def edit_email(self, email_old, email_new):
        find_email = False
        for e in self.emails:
            if e.value == email_old:
                find_email = True
                email_to_remove = e
        if find_email:
            if self.add_email(email_new):
                self.emails.remove(email_to_remove)
        else:
            raise PhoneNotFindError


    # Додавання телефоного номеру до запису
    def add_phone(self, phone):
        if len(phone) != Phone.MAX_PHONE_LEN:
            raise LenPhoneError
        elif not phone.isdigit():
            raise TypePhoneError
        else:
            new_phone = True
            for p in self.phones:
                if p.value == phone:
                    new_phone = False
            if new_phone:
                self.phones.append(Phone(phone))
        
    # Видалення телефоного номеру від запису
    def remove_phone(self, phone):
        find_phone = False
        for p in self.phones:
            if p.value == phone:
                find_phone = True
                phone_to_remove = p
        if find_phone:
            self.phones.remove(phone_to_remove)
        else:
            raise PhoneNotFindError

    # Заміна одного телефонного номера на інший
    def edit_phone(self, phone_old, phone_new):
        if len(phone_new) != Phone.MAX_PHONE_LEN:
            raise LenPhoneError
        elif not phone_new.isdigit():
            raise TypePhoneError
        else:
            sucsess = False
            for phone in self.phones:
                if phone.value == phone_old:
                    phone.value = phone_new
                    sucsess = True
            if not sucsess:
                raise PhoneNotFindError

    # Створення рядку для використання його для пошуку
    def searchstring(self):
        phones_line = f"{' '.join(p.value for p in self.phones)}" if self.phones else ""
        birthday_line = f"{self.birthday.__str__()}" if self.birthday else ""
        emails_line = f"{' '.join(p.value for p in self.emails)}" if self.emails else ""
        address_line = f"{self.address}" if self.address else ""
        res = f"{self.user_id} {self.name.value} " + phones_line + birthday_line + emails_line + address_line
        return res.lower()

    def __str__(self):
        phones_line = f"; phones: {', '.join(p.value for p in self.phones)}" if self.phones else ""
        birthday_line = f"; birthday: {self.birthday.__str__()}" if self.birthday else ""
        emails_line = f"; emails: {', '.join(p.value for p in self.emails)}" if self.emails else ""
        address_line = f"; adress: {self.address}" if self.address else ""
        res = f"Contact id: {self.user_id}, name: {self.name.value}" + phones_line + birthday_line + emails_line + address_line
        return res

class AddressBook(UserDict):
    # Визначимо атрибут data_folder усередині класу
    data_folder = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        """
        Ініціалізія AddressBook із лічильником ID користувачів та словником даних
        """
        self.user_id_counter = 0
        self.data: dict[int, Record] = UserDict()

    # Завантаження Адресної Книги з файлу
    def read_from_file(self):
        """
        Зчитатування даних з файлу та повернення екземпляру AddressBook
        """
        file_path = os.path.join(AddressBook.data_folder, 'abook.dat')
        with open(file_path, 'rb') as fh:
            return pickle.load(fh)

    # Зберегти Адресної Книги у файл
    def save_to_file(self):
        """
        Збереження екземпляру AddressBook у файл
        """
        file_path = os.path.join(AddressBook.data_folder, 'abook.dat')
        with open(file_path, 'wb') as fh:
            pickle.dump(self, fh)
    
    def add_record(self, record: Record):
        """
        Додавання нового запису до AddressBook

        Args:
            record: Запис, який потрібно додати до AddressBook
        """
        self.data[self.user_id_counter] = record
        self.user_id_counter += 1
    
    def edit_record(self, args):
        """
        Редагування ім'я запису в AddressBook

        Args:
            args (list): Список, що містить ID запису та нове ім'я
        """
        self.data[int(args[0])].name = Name(args[1])

    def del_record(self, args):
        """
        Видалення запису з AddressBook

        Args:
            args (list): Список, що містить ID запису, який потрібно видалити
        """
        self.data.pop(int(args[0]))

    def add_phone(self, args):
        """
        Додавання телефонного номеру контакту
        """
        self.data[int(args[0])].add_phone(args[1])

    def edit_phone(self, args):
        """
        Заміна телефонного номеру контакту
        """
        self.data[int(args[0])].edit_phone(args[1], args[1])   

    def del_phone(self, args):
        """
        Видалення телефонного номеру контакту
        """
        self.data[int(args[0])].remove_phone(args[1])   


# class Нотатки користувача
class Note:
    def __init__(self, nbook, content):
        """
        Ініціалізація об'єкта Note з контентом, тегами та датою створення.

        Args:
            content (str): Зміст нотатки
            tags (list): Список тегів, пов'язаних із нотаткою
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
    
    # Видалення тегу із запису
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
    # Визначимо атрибут data_folder усередині класу
    data_folder = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        """
        Ініціалізація Блокнота з лічильником ID користувача та словником даних.
        """
        self.note_id_counter = 0
        self.data = UserDict()
        self.max_tags_len = 5 + 2


    def add_record(self,note):
        """
        Додавання нової нотатки до Блокнота.

            Args:
            note: Запис, який потрібно додати до блокнота.
        """
        self.data[self.note_id_counter] = note
        self.note_id_counter += 1


    def read_from_file(self):
        """
        Зчитування даних з файлу та повернення екземпляра Адресної Книги.
        """
        file_path = os.path.join(NoteBook.data_folder, 'nbook.dat')
        with open(file_path, 'rb') as fh:
            return pickle.load(fh)


    def save_to_file(self):
        """
        Збереження екземпляра Блокнота у файл.
        """
        file_path = os.path.join(NoteBook.data_folder, 'nbook.dat')
        with open(file_path, 'wb') as fh:
            pickle.dump(self, fh)


    def edit_record(self, args):
        """
        Редагування імені запису в Адресній Книзі.

            Args:
            args (list): Список, що містить ID запису та нове ім'я.
        """
        self.data[int(args[0])].content = (' '.join(args[1:]))


    def del_note(self, args):
        """
        Видалення нотатки з Блокнота.

            Args:
            args (list): Список, що містить ID запису для видалення.
        """
        self.data.pop(int(args[0]))