from typing import Optional
from .base_validator import BaseValidator
from jsonconfigparser.exceptions import validator_errors as errors


class ComparisonValidator(BaseValidator):
    def __init__(
        self,
        gt: Optional[int | float] = None,
        ge: Optional[int | float] = None,
        lt: Optional[int | float] = None,
        le: Optional[int | float] = None,
    ):
        if gt is not None and type(gt) not in [int, float]:
            raise errors.InvalidArgumentError(
                f"'greater than' value is supposed to be type {int} or {float}, is type {type(gt)} instead"
            )
        if ge is not None and type(ge) not in [int, float]:
            raise errors.InvalidArgumentError(
                f"'greater or equal' value is supposed to be type {int} or {float}, is type {type(ge)} instead"
            )
        if lt is not None and type(lt) not in [int, float]:
            raise errors.InvalidArgumentError(
                f"'less than' value is supposed to be type {int} or {float}, is type {type(lt)} instead"
            )
        if le is not None and type(le) not in [int, float]:
            raise errors.InvalidArgumentError(
                f"'less or equal' value is supposed to be type {int} or {float}, is type {type(le)} instead"
            )

        if gt is not None and ge is not None:
            raise errors.InvalidArgumentError(
                "'greater than' and 'greater or equal' constraints defined at the same time",
            )
        if lt is not None and le is not None:
            raise errors.InvalidArgumentError(
                "'less than' and 'less or equal' constraints defined at the same time",
            )

        if gt is not None:
            if lt is not None and lt <= gt:
                raise errors.InvalidArgumentError(
                    "'greater than' and 'less than' constraints contradict each other",
                )
            if le is not None and le <= gt:
                raise errors.InvalidArgumentError(
                    "'greater than' and 'less or equal' constraints contradict each other",
                )
        if ge is not None:
            if lt is not None and lt <= ge:
                raise errors.InvalidArgumentError(
                    "'greater or equal' and 'less than' constraints contradict each other",
                )
            if le is not None and le < ge:
                raise errors.InvalidArgumentError(
                    "'greater or equal' and 'less or equal' constraints contradict each other",
                )

        self._gt = gt
        self._ge = ge
        self._lt = lt
        self._le = le

    def validate(self, value: int | float) -> bool:
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
