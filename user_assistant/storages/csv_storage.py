from csv import DictReader, DictWriter
from pathlib import Path
from typing import Type

from .storage import Storage
from user_assistant.serializers.serializer import Serializer


class CSVStorage(Storage):
    def __init__(self, path: Path, serializer: Type[Serializer], fieldnames: [str]):
        self.path = path
        self.serializer = serializer
        self.fieldnames = fieldnames

    def get(self):
        data = []

        with open(self.path, 'r', newline='') as file:
            reader = DictReader(file, fieldnames=self.fieldnames)

            for row in reader:
                if self.is_header_row(row):
                    continue

                data.append(self.serializer.deserialize(row))

        return data

    def update(self, records):
        print(records)
        with open(self.path, 'w', newline='') as file:
            writer = DictWriter(file, fieldnames=self.fieldnames)
            print('The file must have been created')
            print('writer', writer)
            writer.writeheader()

            for record in records:
                writer.writerow(self.serializer.serialize(record))

    def is_header_row(self, row):
        for field_name in self.fieldnames:

            if row[field_name] != field_name:
                return False

        return True