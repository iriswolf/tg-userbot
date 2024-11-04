from typing import Any
from abc import ABC, abstractmethod
from collections.abc import Hashable


class BaseUserStorage(ABC):

    @abstractmethod
    def get(self, key: Hashable) -> Any:
        ...

    @abstractmethod
    def set(self, key: Hashable, value: Any) -> None:
        ...