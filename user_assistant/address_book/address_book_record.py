from user_assistant.class_fields.phone import Phone
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.mail import Mail
from user_assistant.class_fields.address import Address
from datetime import date



class AddressBookRecord:
    def __init__(self, name: Name, birthday: Date, mail: Mail, address: Address, phones: list[Phone] = [] ):
        self.name = name
        self.birthday = birthday
        self.phones = phones
        self.mail = mail
        self.address = address

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, email: {self.mail}, address: {self.address}, phones: {'; '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, email: {self.mail}, address: {self.address}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

        return self.phones

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda item: item.value != phone, self.phones))

        return self.phones

    def edit_phone(self, old_phone, new_phone):
        idx = self.phones.index(old_phone)
        self.phones[idx].value = new_phone

        return self.phones

    def find_phone(self, phone: str):
        for current_phone in self.phones:
            if current_phone.value == phone:
                return current_phone

        return None
    
    def edit_name(self, new_name: Name):
        self.name = new_name

        return self.name
    
    def edit_birthday(self, new_birthday: Date):
        self.birthday = new_birthday

        return self.birthday

    def edit_email(self, new_email: Mail):
        self.mail = new_email

        return self.mail
    
    def edit_address(self, new_address: Address):
        self.address = new_address

        return self.address

    def days_to_birthday(self):
        today = date.today()
        year = today.year if today <= self.birthday.value.replace(year=today.year) else today.year + 1
        closest_birthday = self.birthday.value.replace(year=year)

        return (closest_birthday - today).days

