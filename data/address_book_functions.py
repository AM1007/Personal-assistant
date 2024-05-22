import datetime
from data.classes import AddressBook, Birthday, DateFormatError

def upcoming_birthdays(book, args):
    """
    Повернення списку контактів з адресної книги, чиї дні народження наближаються.

    :param book: Об'єкт адресної книги, де зберігаються дані контактів.

    :param args: Аргументи функції. args[0] визначає кількість днів, які враховуються для наближаючих днів народження.

    :return: Список контактів, чиї дні народження наближаються та відповідають критеріям.


    Функція перевіряє всі контакти в книзі та визначає, чи наближається день народження кожного контакту в межах
    зазначеної кількості днів, яка передається як перший елемент у `args`. Якщо день народження контакту наближається,
    його додають до списку `birthday_contacts`. Контакти, чиї дні народження вже пройшли або ще не скоро, не включаються в результат.


    Наприклад, якщо `args[0]` дорівнює 7, функція поверне список контактів, чиї дні народження наближаються
    протягом наступних 7 днів.
    """
    today = datetime.date.today()
    birthday_contacts = []
    this_year = today.year
    try:
        for _, record in book.data.items():
            if record.birthday is not None:
                days_until_birthday = (record.birthday.value.replace(year=this_year) - today).days
                if days_until_birthday < 0:
                    days_until_birthday = (record.birthday.value.replace(year=this_year + 1) - today).days
                if 0 <= days_until_birthday <= int(args[0]):
                    birthday_contacts.append(record)

        if birthday_contacts:
            return birthday_contacts
        else:
            print('There are no upcoming birthdays')
            return False
    except IndexError:
        print('Command should be followed by "number of days" parameter')
    except ValueError:
        print('"number of days" parameter should be integer')

def birthday_record(book:AddressBook, args:list):
    """
    Додавання дня народження для запису в адресну книгу
    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить інформацію про контакти.
        user_id (int): Ідентифікатор користувача в адресній книзі.
        birthday (Birthday): День народження користувача. 
    """
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.birthday = Birthday(args[1])
                print('Birthday added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except DateFormatError:
            print('Error: Date format must be: DD.MM.YYYY')
    else:
        print('Error: Invalid command format.')

def del_birthday(book:AddressBook, args:list):
    """
    Видалення дня народження з запису в адресній книзі
    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить інформацію про контакти.
        user_id (int): Ідентифікатор користувача в адресній книзі.
    """
    if len(args) ==1:
        if int(args[0]) in book.data:
            rec = book.data[int(args[0])]
            rec.birthday = None
            print('Birthday deleted sucessfully.')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')