from pathlib import Path

import commands
from handlers.address_book.add_contact import add_contact
from handlers.address_book.remove_contact import remove_contact
from handlers.address_book.edit_contact import edit_contact
from handlers.address_book.find_contact import find_contact
from handlers.address_book.show_birthday import show_birthday
from handlers.sort_file.sort_file import sort_files
from handlers.do_exit import do_exit

from address_book.address_book import AddressBook
from storages.csv_storage import CSVStorage
from serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer


PATH = Path('databases') / Path('address_book.csv')
ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail']

address_book_storage = CSVStorage(PATH, AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)
book = AddressBook(address_book_storage.get() if PATH.exists() else [])


def main():
    while True:
        user_input = input('Enter command: ').casefold()

        if user_input == commands.ADD_CONTACT:
            add_contact(book, address_book_storage)
            continue

        if user_input == commands.REMOVE_CONTACT:
            remove_contact(book, address_book_storage)
            continue

        if user_input == commands.EDIT_CONTACT:
            edit_contact(book, address_book_storage)
            continue

        if user_input == commands.FIND_CONTACT:
            find_contact()
            continue

        if user_input == commands.SHOW_BIRTHDAY:
            show_birthday(book)
            continue

        if user_input == commands.SORT_FILES:
            sort_files()
            continue

        if user_input == commands.EXIT or user_input == commands.CLOSE:
            do_exit()
            break


if __name__ == '__main__':
    main()
