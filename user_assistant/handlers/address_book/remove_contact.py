from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.handlers.address_book.add_contact import input_value
from user_assistant.storages.storage import Storage

def remove_contact(book: AddressBook, storage: Type[Storage]):
    name = input_value('name', Name)

    book.delete(str(name))
    storage.update(book.data.values())

    print(f'Contact {name} removed')
