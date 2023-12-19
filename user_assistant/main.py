from pathlib import Path

import user_assistant.commands as COMMANDS
from user_assistant.handlers.address_book.add_contact import add_contact
from user_assistant.handlers.address_book.remove_contact import remove_contact
from user_assistant.handlers.address_book.edit_contact import edit_contact
from user_assistant.handlers.address_book.find_contact import find_contact
from user_assistant.handlers.address_book.show_birthday import show_birthday
from user_assistant.handlers.sort_file.sort_file import sort_files
from user_assistant.handlers.do_exit import do_exit

from user_assistant.address_book.address_book import AddressBook
from user_assistant.storages.csv_storage import CSVStorage
from user_assistant.serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer


PATH = Path('user_assistant') / Path('databases') / Path('address_book.csv')
ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail']

address_book_storage = CSVStorage(PATH, AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)
book = AddressBook(address_book_storage.get() if PATH.exists() else [])


def main():
    while True:
        user_input = input('Enter command: ').casefold()

        if user_input == COMMANDS.ADD_CONTACT:
            add_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.REMOVE_CONTACT:
            remove_contact()
            continue

        if user_input == COMMANDS.EDIT_CONTACT:
            edit_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.FIND_CONTACT:
            find_contact(book)
            continue

        if user_input == COMMANDS.SHOW_BIRTHDAY:
            show_birthday(book)
            continue

        if user_input == COMMANDS.SORT_FILES:
            sort_files()
            continue

        if user_input in (COMMANDS.EXIT, COMMANDS.CLOSE):
            do_exit()
            break


if __name__ == '__main__':
    main()
