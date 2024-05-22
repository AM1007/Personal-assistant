from data.classes import NoteBook, Note, PhoneNotFindError

def add_note(nbook: NoteBook, args:list):
    """
    Створити новий запис у нотатнику
    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про нотатки.
        Note (str): Нотатка
    """
    if len(args) >=1:
        nbook.add_record(Note(nbook, (' '.join(args))))
        print('Нотатка успішно створена.')
    else:
        print('Помилка: Неправильний формат команди.')

def edit_note(nbook: NoteBook, args:list):
    """
    Редагувати нотатку в нотатнику
    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про нотатки.
        note id (int): ID нотатки в нотатнику
        Note (str): новий текст нотатки 
    """
    if len(args) >=2:
        if int(args[0]) in nbook.data:
            nbook.edit_record(args)
            print('Запис успішно відредаговано')
        else:
            print(f'ID нотатки {args[0]} не знайдено')
    else:
        print('Помилка: Неправильний формат команди.')

def del_note(nbook: NoteBook, args: list):
    """
    Видалити нотатку в нотатнику
    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про нотатки.
        note id (int): ID нотатки в нотатнику
    """
    if len(args) == 1:
        if int(args[0]) in nbook.data:
            nbook.del_note(args)
            print('Нотатка успішно видалена')
        else:
            print(f'ID нотатки {args[0]} не знайдено')
    else:
        print('Помилка: Неправильний формат команди.')