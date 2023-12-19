from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name


def find_contact(book: AddressBook):
    name = Name(input(f'Enter contact name: '))

    result = book.find(name.value)

    if result is not None:
        return print(result)

    print(f'There is no any contact named: {name}')