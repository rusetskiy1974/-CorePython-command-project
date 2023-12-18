from pathlib import Path

import commands
from handlers.address_book.add_contact import add_contact
from handlers.address_book.remove_contact import remove_contact
from handlers.address_book.edit_contact import edit_contact
from handlers.address_book.find_contact import find_contact
from handlers.address_book.show_birthday import show_birthday
from address_book.address_book import AddressBook
from handlers.sort_file.sort_file import sort_files

book = AddressBook()


def main():
    while True:
        user_input = input('Enter command: ').casefold()

        if user_input == commands.ADD_CONTACT:
            add_contact(book)
            continue

        if user_input == commands.REMOVE_CONTACT:
            remove_contact(book)
            continue

        if user_input == commands.EDIT_CONTACT:
            edit_contact()
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


if __name__ == '__main__':
    main()
