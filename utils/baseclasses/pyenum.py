"""
For future tests it will be good opportunity to use enums for parametrizing
"""
from enum import Enum


class PyEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
