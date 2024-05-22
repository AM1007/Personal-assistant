from data.classes import NoteBook, Note, PhoneNotFindError

def add_note(nbook: NoteBook, args:list):
    """
    Створення нового запису в Блокноті

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про нотатки
        Note (str): Нотатка
    """
    if len(args) >=1:
        nbook.add_record(Note(nbook, (' '.join(args))))
        print('Note created sucessfully')
    else:
        print('Error: Invalid command format.')

def edit_note(nbook: NoteBook, args:list):
    """
    Редагування нотатки в Блокноті

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про нотатки
        note id (int): ID нотатки в Блокноті
        Note (str): новий текст Блокноті 
    """
    if len(args) >=2:
        if int(args[0]) in nbook.data:
            nbook.edit_record(args)
            print('Record sucessfully edited')
        else:
            print(f'Note id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def del_note(nbook: NoteBook, args: list):
    """
    Видалення нотатки із Блокноту

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про нотатки
        note id (int): ID нотатки в нотатнику
    """
    if len(args) ==1:
        if int(args[0]) in nbook.data:
            nbook.del_note(args)
            print('Note sucessfully deleted')
        else:
            print(f'Note id {args[0]} not found')
    else:
        print('Error: Invalid command format.')
def add_tag(nbook: NoteBook, args:list):
    """
    Додання тегу до запису з ідентифікатором note_id в Блокнот

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про контакти
        note_id (int): Ідентифікатор нотатки в Блокноті.
        tag (str): Тег для нотатки.
    """
    if len(args) ==2:
        if int(args[0]) in nbook.data:
            rec = nbook.data[int(args[0])]
            rec.add_tag(args[1])
            print('Tag added sucessfully.')
        else:
            print(f'Note id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def del_tag(nbook: NoteBook, args:list):
    """
    Видалення тегу із запису з ідентифікатором note_id з Блокноту

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про контакти
        note_id (int): Ідентифікатор нотатки в Блокноті
        tag (str): Тег для видалення
    """
    if len(args) ==2:
        try:
            rec = nbook.data[int(args[0])]
            rec.remove_tag(args[1])
            print('Tag deleted sucessfully.')
        except KeyError:
            print(f'Note id {args[0]} not found')
        except PhoneNotFindError:
            print('Error: Tag to delete is not found.')
    else:
        print('Error: Invalid command format.')

def find_in_notes(nbook: NoteBook, args:list):
    """
    Пошук нотаток та тегів в Блокноті

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про контакти
        search_string (str): Рядок для пошуку. Має містити принаймні 2 символи
    """
    if len(args) ==1 and len(args[0]) > 1:
        count = 0
        sstring = args[0].lower()
        for _, record in nbook.data.items():
            if record.searchstring().find(sstring) >=0:
                print(record)
                count += 1
        print(f'Search complete. Total {count} records found.')    
    else:
        print('Error: Invalid command format. Search string must be more then 2 symbols')

def find_in_tags(nbook: NoteBook, args:list):
    """
    Пошук тегів у Блокноті

    Args:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про контакти
        search_string (str): Рядок для пошуку. Має містити принаймні 2 символи
    """
    if len(args) ==1 and len(args[0]) > 1:
        count = 0
        sstring = args[0].lower()
        for _, record in nbook.data.items():
            if record.search_tag().find(sstring) >=0:
                print(record)
                count += 1
        print(f'Search complete. Total {count} records found.')    
    else:
        print('Error: Invalid command format. Search string must be more then 2 symbols')

def sort_by_tags(nbook: NoteBook, args:list):
    """
    Вивести всі нотатки, відсортовані за кількістю тегів

    Аргументи:
        nbook (NoteBook): Екземпляр NoteBook, що містить інформацію про контакти
    """
    if len(args) == 0:
        #print(nbook.data.values)
        notes = []
        for _, n in nbook.data.items():
            notes.append(n)
        sorted_notes = sorted(notes, key=lambda note: len(note.tags))
        print("All existing notes (Sorted by Tag):")
        for i, note in enumerate(sorted_notes, 1):
            print(f"ID: {note.note_id:^3}| Number of Tags: [{len(note.tags):^4}]| NOTE: {note.content}")
    else:
        print('Error: Invalid command format.')
