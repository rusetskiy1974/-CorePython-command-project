from .field import Field
from datetime import datetime
import math

class ID(Field):
    def __init__(self):
        super().__init__(f'{id(self)}_{math.floor(datetime.timestamp(datetime.now()))}')