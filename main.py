from pathlib import Path

from user_assistant import commands as COMMANDS
from user_assistant.handlers.address_book.add_contact import add_contact
from user_assistant.handlers.address_book.remove_contact import remove_contact
from user_assistant.handlers.address_book.edit_contact import edit_contact
from user_assistant.handlers.address_book.find_contact import find_contact
from user_assistant.handlers.address_book.show_birthday import show_birthday
from user_assistant.handlers.address_book.show_all_contacts import show_all_contacts
from user_assistant.handlers.address_book.search_contact import search_contact
from user_assistant.handlers.sort_file.sort_file import sort_files
from user_assistant.handlers.do_exit import do_exit

from user_assistant.address_book.address_book import AddressBook
from user_assistant.storages.csv_storage import CSVStorage
from user_assistant.serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer

from user_assistant.notes.notes import Notes
from user_assistant.serializers.notes.notes_csv_serializer import NotesCSVSerializer
from user_assistant.handlers.notes.add_note import add_note
from user_assistant.handlers.notes.find_note import find_note
from user_assistant.handlers.notes.remove_note import remove_note

from user_assistant.handlers.notes.search_notes_by_author import search_notes_by_author
from user_assistant.handlers.notes.search_notes_by_tag import search_notes_by_tag
from user_assistant.handlers.notes.edit_note import edit_note
from user_assistant.handlers.notes.sort_by_tags import sort_by_tags
from user_assistant.handlers.notes.sort_by_author import sort_by_author


from user_assistant.handlers.greeting import greeting
from user_assistant.handlers.notes.show_all_notes import show_all_notes

from user_assistant.console.console import Console

STORAGE_PATH = Path('.') / Path('user_assistant') / Path('databases')

ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail']
NOTE_FIELDS = ['author', 'text', 'tags', 'id', 'created_at']

address_book_storage = CSVStorage(STORAGE_PATH, 'address_book.csv', AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)
book = AddressBook(address_book_storage.get())

notes_storage = CSVStorage(STORAGE_PATH, 'notes.csv', NotesCSVSerializer, NOTE_FIELDS)
notes = Notes(notes_storage.get())

prompts = list(map(lambda name: getattr(COMMANDS, name), filter(lambda name: not name.startswith('__'), dir(COMMANDS))))


def main():
    greeting()

    while True:

        user_input = Console.input('Enter command: ', prompts).casefold().strip()

        if user_input == COMMANDS.ADD_CONTACT:
            add_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.REMOVE_CONTACT:
            remove_contact(book, address_book_storage)
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

        if user_input == COMMANDS.SHOW_ALL_CONTACTS:
            show_all_contacts(book)
            continue

        if user_input == COMMANDS.SEARCH_CONTACT:
            search_contact(book)
            continue

        if user_input == COMMANDS.SORT_FILES:
            sort_files()
            continue

        if user_input in (COMMANDS.EXIT, COMMANDS.CLOSE):
            do_exit()
            break

        if user_input == COMMANDS.ADD_NOTE:
            add_note(notes, notes_storage)
            continue

        if user_input == COMMANDS.FIND_NOTE:
            find_note(notes)
            continue

        if user_input == COMMANDS.SHOW_ALL_NOTES:
            show_all_notes(notes)
            continue

        if user_input == COMMANDS.REMOVE_NOTE:
            remove_note(notes, notes_storage)
            continue


        if user_input == COMMANDS.SEARCH_BY_TAG:
            search_notes_by_tag(notes)
            continue
        
        if user_input == COMMANDS.SEARCH_BY_AUTHOR:
            search_notes_by_author(notes)
            continue
            

        if user_input == COMMANDS.EDIT_NOTE:
            edit_note(notes, notes_storage)
            continue

        if user_input == COMMANDS.SORT_BY_TAGS:
            sort_by_tags(notes)
            continue

        if user_input == COMMANDS.SORT_BY_AUTHOR:
            sort_by_author(notes)
            continue



if __name__ == '__main__':
    main()
