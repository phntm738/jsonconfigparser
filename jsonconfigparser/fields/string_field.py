from fields.base_field import BaseField
from .validation import BaseValidator, LengthValidator
from typing import Optional, Union, Iterable


class StringField(BaseField):
    _ALLOWED_TYPES = [str]

    def __init__(
        self,
        name: Optional[str] = None,
        default: Optional[str] = None,
        validate_default: bool = True,
        nullable: bool = False,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        validators: Optional[Union[BaseValidator, Iterable[BaseValidator]]] = None,
    ):
        if not all([min_length is None, max_length is None]):
            self._validators.append(LengthValidator(min_length, max_length))

        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            validators=validators,
        )
