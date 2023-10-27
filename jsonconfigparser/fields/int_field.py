from fields.number_field import NumberField
from validators import BasicValidator
from jsonconfigparser import exceptions
from typing import Optional, Union, Iterable
from jsonconfigparser.section import Section


class IntField(NumberField):
    def __init__(
            self,
            name: Optional[str] = None,
            default: Optional[int] = None,
            validate_default: bool = True,
            nullable: bool = False,
            gt: Optional[Union[int, float]] = None,
            ge: Optional[Union[int, float]] = None,
            lt: Optional[Union[int, float]] = None,
            le: Optional[Union[int, float]] = None,
            validators: Optional[Union[BasicValidator, Iterable[BasicValidator]]] = None
    ):
        if default is not None and not isinstance(default, int):
            raise exceptions.InvalidDefaultType(name, f"expected default of type {int}, got {type(default)} instead")

        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            validators=validators
        )

    def value(self) -> Union[int, None]:
        rv = super().value()
        if rv is not None and not isinstance(rv, int):
            raise exceptions.InvalidValueError(
                self.name,
                f"field is expected to contain {int}, contains {type(rv)} instead"
            )
        return rv

    def set_value(self, new_value: int) -> None:
        if not isinstance(new_value, int):
            raise exceptions.InvalidValueError(
                self._name,
                f"field accepts values of type {int}, got {type(new_value)} instead"
            )
        super().set_value(new_value)


__all__ = (
    'IntField'
)
