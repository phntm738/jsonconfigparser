from fields.number_field import NumberField
from validators import BasicValidator
from jsonconfigparser import exceptions
from typing import Optional, Union, Iterable
from jsonconfigparser.section import Section


class FloatField(NumberField):
    def __init__(
            self,
            parent: Optional[Section] = None,
            name: Optional[str] = None,
            default: Optional[Union[int, float]] = None,
            validate_default: bool = True,
            nullable: bool = False,
            gt: Optional[Union[int, float]] = None,
            ge: Optional[Union[int, float]] = None,
            lt: Optional[Union[int, float]] = None,
            le: Optional[Union[int, float]] = None,
            validators: Optional[Union[BasicValidator, Iterable[BasicValidator]]] = None
    ):
        if default is not None and isinstance(default, int):
            default = float(default)
        if default is not None and not isinstance(default, float):
            raise exceptions.InvalidDefaultType(
                name,
                f"expected default of type {int} or {float}, got {type(default)} instead"
            )

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

    def value(self) -> Union[float, None]:
        rv = super().value()
        if rv is not None and not isinstance(rv, float):
            raise exceptions.InvalidValueError(
                self.name,
                f"field is expected to contain {float}, contains {type(rv)} instead"
            )
        return rv

    def set_value(self, new_value: Union[int, float]) -> None:
        if isinstance(new_value, int):
            new_value = float(new_value)
        if not isinstance(new_value, float):
            raise exceptions.InvalidValueError(
                self.name,
                f"field accepts values of type {int} or {float}, got {type(new_value)} instead"
            )
        super().set_value(new_value)


__all__ = (
    'FloatField'
)
