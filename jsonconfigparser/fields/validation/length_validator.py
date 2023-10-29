from typing import Optional
from collections.abc import Sized
from .base_validator import BaseValidator
from jsonconfigparser.exceptions import validator_errors as errors


class LengthValidator(BaseValidator):
    def __init__(
        self, min_length: Optional[int] = None, max_length: Optional[int] = None
    ):
        if min_length is not None:
            if not isinstance(min_length, int):
                raise errors.InvalidArgumentError(
                    f"Min_length value is supposed to be type {int}, is type {type(min_length)} instead"
                )
            if min_length < 0:
                raise errors.InvalidArgumentError("Min_length value is less than 0")

        if max_length is not None:
            if not isinstance(max_length, int):
                raise errors.InvalidArgumentError(
                    f"Max_length value is supposed to be type {int}, is type {type(max_length)} instead"
                )
            if max_length < 1:
                raise errors.InvalidArgumentError("Max_length value is less than 1")

        if min_length is not None and max_length is not None:
            if min_length > max_length:
                raise errors.InvalidArgumentError(
                    "Min_length and max_length contradict each other"
                )

        self._min_length = min_length
        self._max_length = max_length

    def validate(self, value: Sized) -> bool:
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
