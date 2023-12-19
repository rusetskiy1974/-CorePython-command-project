import re


def date_validation(date: str):
    return re.match(r'\d{2}\.\d{2}\.\d{4}', date)
