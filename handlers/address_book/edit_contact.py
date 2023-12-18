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
    while True:
        name = input_value('name', Name)
        record = book.find(str(name))
        if record:
            break
        else:
            print('Input correct name')

    while True:
        field = input(f'Input field for change, c - end :')
        if field != 'c':
            if field in FIELDS_CLASS.keys():
                volume = input_value(field, FIELDS_CLASS[field])
                if field == 'birthday':
                    record.edit_birthday(volume)
                elif field == 'email':
                    record.edit_email(volume)
                elif field == 'address':
                    record.edit_address(volume)
                elif field == 'name':
                    record.edit_name(volume)
                elif field == 'phone':
                    while True:
                        phone_action = input(f'remove/edit/add :')
                        if phone_action == 'remove':
                            record.remove_phone(volume)
                            break
                        elif phone_action == 'add':
                            record.add_phone(volume)
                            break
                        elif phone_action == 'edit':                 
                            old_phone = input_value('old phone number', Phone)
                            record.edit_phone(str(old_phone), str(volume)) 
                            break
                        print('Incorrect value')


                print(f'Fields  {field} changed')
            else:
                print('Incorrect value')  
                 
        else:
            break
       
    print(f'Contact {name} changed')
    storage.update(book.data.values())
