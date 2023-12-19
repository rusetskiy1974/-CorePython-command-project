from datetime import datetime

from user_assistant.class_fields.text import Text
from user_assistant.class_fields.author import Author
from user_assistant.class_fields.tag import Tag
from user_assistant.class_fields.date_time import DateTime
from user_assistant.class_fields.id import ID


class NoteRecord:
    def __init__(self, author: Author, text: Text, tags: [Tag]):
        self.author = author
        self.text = text
        self.tags = tags
        self.id = ID()
        self.created_at = DateTime(datetime.now())

    def __str__(self):
        return f"Note author: {self.author.value}, text: {self.text.value}, tags: {'; '.join(p.value for p in self.tags)}, created_at: {self.created_at}, id: ${self.id.value}"

    def __repr__(self):
        return f"Note author: {self.author.value}, text: {self.text.value}, tags: {'; '.join(p.value for p in self.tags)}, created_at: {self.created_at}, id: ${self.id.value}"

    def str_tags(self):
        return list(map(lambda tag: tag.value,self.tags))

    def update_text(self, new_text: Text):
        self.text = new_text

    def update_author(self, new_author: Author):
        self.author = new_author

    def add_tag(self, new_tag: Tag):
        self.tags.append(new_tag)

    def remove_tag(self, tag: Tag):
        self.tags.remove(tag)


         