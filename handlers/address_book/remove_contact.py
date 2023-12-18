from class_fields.name import Name
from handlers.address_book.add_contact import input_value


def remove_contact(book):
    name = input_value('name', Name)

    book.delete(str(name))
    print(f'Contact {name} removed')