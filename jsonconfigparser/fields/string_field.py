from fields.basic_field import BasicField
from validators import BasicValidator, StringLengthValidator
from jsonconfigparser import exceptions
from typing import Optional, Union, Iterable


class StringField(BasicField):
    def __init__(
        self,
        name: Optional[str] = None,
        default: Optional[str] = None,
        validate_default: bool = True,
        nullable: bool = False,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        validators: Optional[Union[BasicValidator, Iterable[BasicValidator]]] = None
    ):
        if default is not None and not isinstance(default, str):
            raise exceptions.InvalidDefaultType(name, f"expected default of type {str}, got {type(default)} instead")

        if min_length is not None and min_length < 0:
            raise exceptions.InvalidParametersError(name, "min_length < 0")
        if max_length is not None and max_length <= 0:
            raise exceptions.InvalidParametersError(name, "max_length <= 0")
        if min_length is not None and max_length is not None:
            if min_length > max_length:
                raise exceptions.InvalidParametersError(name, "min_length and max_length contradict each other")

        self._init_validators_list()

        if not all([min_length is None, max_length is None]):
            self._validators.append(StringLengthValidator(min_length, max_length))

        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            validators=validators
        )

    def value(self) -> Union[str, None]:
        rv = super().value()
        if rv is not None and not isinstance(rv, str):
            raise exceptions.InvalidValueError(
                self.name,
                f"field is expected to contain {str}, contains {type(rv)} instead"
            )
        return rv

    def set_value(self, new_value: str) -> None:
        if not isinstance(new_value, str):
            raise exceptions.InvalidValueError(
                self.name,
                f"field accepts values of type {str}, got {type(new_value)} instead"
            )
        super().set_value(new_value)


__all__ = (
    'StringField'
)
