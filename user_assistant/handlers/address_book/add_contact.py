from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.address_book.address_book_record import AddressBookRecord
from user_assistant.storages.storage import Storage


def input_value(value, class_field):
    while True:
        result = input(f'Enter {value}: ')
        try:
            result = class_field(result)
            return result
        except Exception as error:
            print(error)
            continue


def add_contact(book: AddressBook, storage: Type[Storage]):

    name = input_value('name', Name)
    date = input_value('date birthday', Date )
    mail = input_value('email', Mail)
    address = input_value('address', Address)
    phone = input_value('phone', Phone)

    record = AddressBookRecord(name= name, birthday= date, mail= mail, address= address,  phones= [phone])
    book.add(record)
    storage.update(book.data.values())

    print(f'Contact {name.value} was added')
