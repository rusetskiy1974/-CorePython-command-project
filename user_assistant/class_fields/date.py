from datetime import datetime

from .field import Field
from user_assistant.validations import date_validation

class Date(Field):
    DATE_FORMAT = '%d.%m.%Y'

    def __str__(self):
        return self.value.strftime(self.DATE_FORMAT)

    @staticmethod
    def validate(value: str):
        result = date_validation(value)

        if result is None:
            raise ValueError('The date is incorrect')


    @Field.value.setter
    def value(self, value: str):
        self.validate(value)
        self._Field__value = datetime.strptime(value, self.DATE_FORMAT).date()
