from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from data.classes import AddressBook, NoteBook

# You need to install the external package in the terminal first: pip install prompt_toolkit
commands = WordCompleter([
    "close", "exit", "hello", "add", "edit", "del", "address", "del-address",
    "add-phone", "edit-phone", "del-phone", "all", 
    "add-email", "edit-email", "del-email", "find",
    "birthday", "del-birthday", "next-birthdays", "note", "help", "sort-tag",
    "edit-note", "all-notes", "del-note", "add-tag", "del-tag", "find-notes", "find-tag"], ignore_case=True)
session = PromptSession(completer=commands)

def exit_procedure(book:AddressBook, nbook:NoteBook):
    """
    Saving AddressBook to file
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
    """
    book.save_to_file()
    nbook.save_to_file()
    print('Good bye!')

# input commands from terminal
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# help
def show_help():
    commands = [['Command', 'Parameters', 'Description'],
                   ['all', '', 'list all information about users'],
                   ['add', '[Name]', 'create new user [Name] in adress book'], 
                   ['edit', '[Contact_id] [new_Name]', 'edit name of [Contact_id] to [new_Name]'],
                   ['del', '[Contact_id]', 'remove user [Contact_id] from adress book'],
                   ['add-phone', '[Contact_id] [Phone]', 'add to user [Contact_id] a [Phone]'],
                   ['edit-phone', '[Contact_id] [Phone] [new_Phone]', 'replace for user [Contact_id] a [Phone] by [new_Phone]'],
                   ['del-phone', '[Name] [Phone]', 'remove phone [Phone] from user [Name]'],
                   ['add-email', '[Contact_id] [Email]', 'add to user [Contact_id] an [Email]'],
                   ['edit-email', '[Contact_id] [Email] [new_Email]', 'replace for user [Contact_id] an [Email] by [new_Email]'],
                   ['del-email', '[Contact_id] [Email]', 'remove email [Email] from user [Contact_id]'],
                   ['address', '[Contact_id] [Address]', 'set for user [Name] an address [Address]'],
                   ['del-address', '[Contact_id]', 'remove address from [Contact_id]'],
                   ['birthday', '[Contact_id] [Birthday]', 'set for user [Contact_id] a birthday at [Birthday]'],
                   ['del-birthday', '[Contact_id]', 'remove birthday from [Contact_id]'],
                   ['find', '[search]', 'list [search] data in Name, Phones, Address, Emails, Birthdays. [search] must be 2 symbols min'],
                   ['next-birthdays', '[int]', 'shows upcoming birthdays if exist in period from today till [int] days'],
                   ['note', '', 'Add a note to Note Book'],
                   ['all-notes', '', 'list all notes'],
                   ['edit-note', '[Note_id] [Note]', 'edit text of [Note_id] Note'],
                   ['del-note', '[Note_id]', 'Remove [Note_id] note from Note Book'],
                   ['add-tag', '[Note_id] [Tag]', 'add [Tag] to note [Note_id]'],
                   ['del-tag', '[Note_id] [Tag]', 'remove [Tag] from note [Note_id]'],
                   ['find-notes', '[searchstring]', 'list all Notes with [searchstring] data in note and tags.[searchstring] must be 2 symbols minimum'],
                   ['find-tags', '[searchstring]', 'list all Notes with [searchstring] data in tags.[searchstring] must be 2 symbols minimum'],
                   ['sort-tag', '', 'list all Notes sorted by number of tags'],
                   ['close, exit', '', 'exit the bot'],
                   ['help', '', 'list all bot commands']]
    dashes = "{0:<14} + {1:<32} + {2:^12} \n".format("-" * 14, "-" * 32, "-" * 12)
    help_string = ''

    for i in commands:
        help_string += f'{i[0]:^14} | {i[1]:^32} | {i[2]:^12} \n'
        #help_string += dashes
    
    print(help_string)