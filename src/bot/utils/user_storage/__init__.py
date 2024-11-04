from typing import Hashable, Any

from .base import BaseUserStorage
from src.pattern import Singleton


class UserMemoryStorage(metaclass=Singleton):

    __storage = {}

    def __init__(self):
        ...

    def get(self, key: Hashable) -> Any:
        return self.__storage.get(key)

    def set(self, key: Hashable, value: Any) -> None:
        self.__storage[key] = value
