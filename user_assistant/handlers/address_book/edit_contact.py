from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.handlers.address_book.add_contact import input_value
from user_assistant.storages.storage import Storage

FIELDS_CLASS = {'name': Name, 'birthday': Date, 'email': Mail, 'address': Address, 'phone': Phone}

def edit_contact(book: AddressBook, storage: Type[Storage]):
    while True:
        name = input_value(f'contact name: ', Name)
        record = book.find(str(name))
        if record:
            break
        else:
            print('Input existing name')

    for field in FIELDS_CLASS.keys():  
        # if input(f'Chang {field} Y/y :') in ['Y','y']:  
            volume = input_value(f'new {field}', FIELDS_CLASS[field], True)
            if field == 'birthday' and volume:
                record.edit_birthday(volume)
            elif field == 'email' and volume:
                record.edit_email(volume)
            elif field == 'address' and volume:
                record.edit_address(volume)
            elif field == 'name' and volume:
                record.edit_name(volume)
            elif field == 'phone':
                while True:
                    phone_action = input(f'remove(r)/edit(e)/add(a) :')
                    if phone_action == 'r':
                        record.remove_phone(volume)
                        break
                    elif phone_action == 'a':
                        record.add_phone(volume)
                        break
                    elif phone_action == 'e':                 
                        old_phone = input_value('old phone number', Phone)
                        record.edit_phone(str(old_phone), str(volume)) 
                        break
                    print('Incorrect value')
      
    print(f'Contact {name} changed')
    storage.update(book.data.values())