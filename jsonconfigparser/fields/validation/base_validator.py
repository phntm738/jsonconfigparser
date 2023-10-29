from typing import Any


class BaseValidator:
    def validate(self, value: Any) -> bool:
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self.__class__.__name__
