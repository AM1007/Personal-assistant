import datetime
from data.classes import AddressBook, Birthday, DateFormatError, TypeEmailError, RecordNotFindError, PhoneNotFindError, Record, LenPhoneError, TypePhoneError

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
    Додавання дня народження дo запису в адресну книгу

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить інформацію про контакти
        user_id (int): Ідентифікатор користувача в адресній книзі
        birthday (Birthday): День народження користувача
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
        book (AddressBook): Екземпляр AddressBook, що містить інформацію про контакти
        user_id (int): Ідентифікатор користувача в адресній книзі
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

def address_record(book:AddressBook, args:list):
    """
    Додавання адреси до запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію.
        user id (int): ID користувача в AddressBook
        address (str): Адреса користувача 
    """
    if len(args) >=2:
        if int(args[0]) in book.data:
            rec = book.data[int(args[0])]
            rec.address = ' '.join(s for s in args[1:])
            print('Address added sucessfully.')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command.')

def del_address(book:AddressBook, args:list):
    """
    Видалення адреси із запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію.
        user id (int): ID користувача в AddressBook
    """
    if len(args) ==1:
        if int(args[0]) in book.data:
            rec = book.data[int(args[0])]
            rec.address = ''
            print('Address deleted sucessfully.')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command.')

def add_email_in_rec(book:AddressBook, args:list):
    """
    Додання електронної пошти до запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію
        user id (int): ID користувача в AddressBook
        email (Email): Електронна пошта користувача 
    """
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.add_email(args[1])
                print('Email added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except TypeEmailError:
            print('Error: Wrong email format')
    else:
        print('Error: Invalid command format.')

def edit_email_in_rec(book:AddressBook, args:list):
    """
    Редагування електронної пошти для запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію.
        user id (int): ID користувача в AddressBook
        email (Email): електронна пошта користувача 
    """
    if len(args) ==3:
        try:
            rec = book.data[int(args[0])]
            rec.edit_email(args[1], args[2])
            print('Email changed sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except PhoneNotFindError:
            print('Error: Email to change is not found.')
        except TypeEmailError:
            print('Error: Wrong email format')    
    else:
        print('Error: Invalid command format.')

def del_email_in_rec(book:AddressBook, args:list):
    """
    Видалення електронної пошти із запису AddressBook 

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію.
        user id (int): ID користувача в AddressBook
        email (Email): електронна пошта користувача 
    """
    if len(args) ==2:
        try:
            rec = book.data[int(args[0])]
            rec.remove_email(args[1])
            print('Email deleted sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except PhoneNotFindError:
            print('Error: Email to delete is not found.')
    else:
        print('Error: Invalid command format.')

def add_record(book:AddressBook, args:list):
    """
    Додавання нового запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію.
        name (Name): Ім'я користувача 
    """
    if len(args) ==1:
        book.add_record(Record(args[0], book))
        print('Record created sucessfully')
    else:
        print('Error: Invalid command format.')

def edit_record(book:AddressBook, args:list):
    """
    Редагування ім'я у записі в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію
        user id (int): ID користувача в AddressBook
        name (Name): Нове ім'я користувача 
    """
    if len(args) ==2:
        if int(args[0]) in book.data:
            book.edit_record(args)
            print('Record sucessfully deleted')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def del_record(book:AddressBook, args:list):
    """
    Видалення запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію
        user id (int): ID користувача в AddressBook
    """
    if len(args) ==1:
        if int(args[0]) in book.data:
            book.del_record(args)
            print('Record sucessfully deleted')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def add_phone_in_rec(book:AddressBook, args:list):
    """
    Додавання телефон до запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію
        user id (int): ID користувача в AddressBook
        phone (str): Номер телефону для додавання
    """
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.add_phone(args[1])
                print('Phone added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except LenPhoneError:
            print('Error: Phone must be 10 symbols')
        except TypePhoneError:
            print('Error: Phone must be 10 symbols')
    else:
        print('Error: Invalid command format.')

def edit_phone_in_rec(book:AddressBook, args:list):
    """
    Заміна номеру телефону на новий в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію
        user id (int): ID користувача в AddressBook
        old phone (str): Номер телефону для зміни
        new phone (str): Новий номер телефону
    """
    if len(args) ==3:
        try:
            rec = book.data[int(args[0])]
            rec.edit_phone(args[1], args[2])
            print('Phone changed sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except LenPhoneError:
            print('Error: Phone must be 10 symbols')
        except PhoneNotFindError:
            print('Error: Phone to change is not found.')
        except TypePhoneError:
            print('Error: Phone must consist from digits')
    else:
        print('Error: Invalid command format.')

def del_phone_in_rec(book:AddressBook, args:list):
    """
    Видалення номеру телефону із запису в AddressBook

    Аргументи:
        book (AddressBook): Екземпляр AddressBook, що містить контактну інформацію
        user id (int): ID користувача в AddressBook
        phone (str): Номер телефону для видалення
    """
    if len(args) ==2:
        try:
            rec = book.data[int(args[0])]
            rec.remove_phone(args[1])
            print('Phone deleted sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except PhoneNotFindError:
            print('Error: Phone to delete is not found.')
    else:
        print('Error: Invalid command format.')

def find_in_records(book:AddressBook, args:list):
    """
    Пошук записів в AddressBook

    Аргументи:
        search string (str): Рядок для пошуку в полях адресної книги: Name, Adress, Phones, Emails, Birthday
    """
    if len(args) ==1 and len(args[0]) > 1:
        count = 0
        sstring = args[0].lower()
        for _, record in book.data.items():
            if record.searchstring().find(sstring) >=0:
                print(record)
                count += 1
        print(f'Search complete. Total {count} records found.')    
    else:
        print('Error: Invalid command format. Search string must be more then 2 symbols')