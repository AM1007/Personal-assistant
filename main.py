from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from data.global_declarations import session, exit_procedure, parse_input, show_help
from data.classes import AddressBook, NoteBook

from data.address_book_functions import (   upcoming_birthdays, add_email_in_rec, edit_email_in_rec, del_email_in_rec, 
                                            birthday_record, del_birthday, address_record, del_address, 
                                            add_record, edit_record, del_record, add_phone_in_rec, edit_phone_in_rec, del_phone_in_rec,
                                            find_in_records  )

from data.notebook_functions import find_in_notes, find_in_tags, sort_by_tags, add_note, edit_note, del_note, add_tag, del_tag


def main():

    print('Welcome to the assistant bot!')
    print('Type "help" to see all commands list and descriptions')

    # Завантаження AddressBook з файлу 'abook.dat'. Створення нової порожньої Адресної Книги в разі, якщо файл відсутній
    try:
        book = AddressBook().read_from_file()
    except:
        book = AddressBook()

    # Завантаження NoteBook з файлу 'nbook.dat'. Створення нового порожнього Блокноту в разі, якщо файл відсутній
    try:
        nbook = NoteBook().read_from_file()
    except:
        nbook = NoteBook()
    
    while True:
        user_input = session.prompt("Enter a command: ", auto_suggest=AutoSuggestFromHistory(), complete_while_typing=False)
        if user_input:
            command, *args = parse_input(user_input)
            
            if command in ['close', 'exit']:
                exit_procedure(book, nbook)
                break

            elif command == 'hello':
                print('How can I help you?')

            elif command == 'add':
                add_record(book, args)

            elif command == 'edit':
                edit_record(book, args)

            elif command == 'del':
                del_record(book, args)

            elif command == 'add-phone':
                add_phone_in_rec(book, args)
            
            elif command == 'edit-phone':
                edit_phone_in_rec(book, args)

            elif command == 'del-phone':
                del_phone_in_rec(book, args)

            elif command == 'add-email':
                add_email_in_rec(book, args)
            
            elif command == 'edit-email':
                edit_email_in_rec(book, args)

            elif command == 'del-email':
                del_email_in_rec(book, args)

            elif command == 'birthday':
                birthday_record(book, args)

            elif command == 'del-birthday':
                del_birthday(book, args)

            elif command == 'address':
                address_record(book, args)

            elif command == 'del-address':
                del_address(book, args)

            elif command == 'find':
                find_in_records(book, args)

            elif command == 'find-notes':
                find_in_notes(nbook, args)

            elif command == 'find-tag':
                find_in_tags(nbook, args)

            elif command == 'sort-tag':
                sort_by_tags(nbook, args)

            elif command == 'help':
                show_help()

            elif command == 'note':
                add_note(nbook, args)

            elif command == 'edit-note':
                edit_note(nbook, args)

            elif command == 'del-note':
                del_note(nbook, args)

            elif command == 'add-tag':
                add_tag(nbook, args)

            elif command == 'del-tag':
                del_tag(nbook, args)

            elif command == 'all-notes':
                for _, note in nbook.data.items():
                    print(note)

            elif command == 'next-birthdays':
                birthdays = upcoming_birthdays(book, args)
                if birthdays:
                    for contact in birthdays:
                        print(contact)
                
            elif command == 'all':
                for _, record in book.data.items():
                    print(record)
            else:
                print('Error: Invalid command.')

if __name__ == '__main__':
    main()
