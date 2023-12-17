from class_fields.name import Name
from class_fields.phone import Phone
from class_fields.date import Date
from class_fields.address import Address
from class_fields.mail import Mail
from address_book.address_book_record import AddressBookRecord


def input_value(value, clas): #Функція введення та валідації даних контакту 
    while True:
        print ('Enter', value,'>>>', end=' ' )
        result = input()
        try:
            result = clas(result)
            return result
        except:
            continue


def add_contact(book):  # Функція формування даних контакту

    name = input_value('name', Name)
    date = input_value('date birthday', Date )
    mail = input_value('email', Mail)
    address = input_value('address', Address)
    phone = input_value('phone', Phone)
    record = AddressBookRecord(name= name, birthday= date, mail= mail, address= address,  phones= [phone])
    book.add(record)

    print ('Contact added')



    



# add_contact()    
        


     