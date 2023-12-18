from typing import Type

from address_book.address_book import AddressBook
from class_fields.name import Name
from class_fields.phone import Phone
from class_fields.date import Date
from class_fields.address import Address
from class_fields.mail import Mail
from handlers.address_book.add_contact import input_value
from storages.storage import Storage

FIELDS_CLASS = {'birthday': Date, 'email': Mail, 'address': Address, 'phone': Phone, 'name': Name}

def edit_contact(book: AddressBook, storage: Type[Storage]):
    name = input_value('name', Name)
    record = book.find(str(name))
    while True:
        field = input(f'Input field for change, n- end :')
        if field != 'n':
            if field in FIELDS_CLASS.keys():
                volume = input_value(field, FIELDS_CLASS[field])
                if field == 'date birthday':
                    record.edit_birthday(volume)
                elif field == 'email':
                    record.edit_email(volume)
                elif field == 'address':
                    record.edit_address(volume)
                elif field == 'name':
                    record.edit_name(volume)               
                     
                print(f'Field {field} changed')
        else:
                break
       
        print(f'Contact {name} changed')
        storage.update(book.data.values())
