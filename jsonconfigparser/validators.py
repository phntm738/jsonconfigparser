from typing import Any, Optional, Union


class BasicValidator:
    def validate(self, value: Any) -> bool:
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self.__class__.__name__


class StringLengthValidator(BasicValidator):
    def __init__(self, min_length: Optional[int] = None, max_length: Optional[int] = None):
        # TODO: validate values
        self._min_length = min_length
        self._max_length = max_length

    def validate(self, value: str) -> bool:
        if self._min_length is not None:
            if len(value) < self._min_length:
                return False
        if self._max_length is not None:
            if len(value) > self._max_length:
                return False
        return True

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}[min: {self._min_length}, max: {self._max_length}]"


class NumberComparisonValidator(BasicValidator):
    def __init__(self,
                 gt: Optional[Union[int, float]] = None,
                 ge: Optional[Union[int, float]] = None,
                 lt: Optional[Union[int, float]] = None,
                 le: Optional[Union[int, float]] = None):
        # TODO: validate values
        self._gt = gt
        self._ge = ge
        self._lt = lt
        self._le = le

    def validate(self, value: Union[int, float]) -> bool:
        if self._gt is not None:
            if value <= self._gt:
                return False
        if self._ge is not None:
            if value < self._ge:
                return False
        if self._lt is not None:
            if value >= self._lt:
                return False
        if self._le is not None:
            if value > self._le:
                return False
        return True

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}[gt: {self._gt}, ge: {self._ge}, lt: {self._lt}, le: {self._le}]"
