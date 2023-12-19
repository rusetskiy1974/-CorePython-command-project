from collections import UserDict
from .note_record import NoteRecord


class Notes(UserDict):
    def __init__(self, records: list[NoteRecord] = []):
        self.data = {record.id.value: record for record in records}

    def add_note(self, note: NoteRecord):
        self.data[note.id] = note

    def search_by_tags(self, searched_tags: [str]):
        result_notes = [note for note in self.data.values() if set(searched_tags).issubset(note.str_tags())]
        return result_notes

    def sort_by_tags(self):
        sorted_notes = sorted(self.data.values(), key=lambda note: ','.join(note.str_tags()))
        return sorted_notes

    def delete(self, id: str):
        self.data.pop(id, None)

