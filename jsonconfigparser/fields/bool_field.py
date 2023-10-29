from fields.base_field import BaseField
from .validation import BaseValidator
from typing import Optional, Union, Iterable


class BoolField(BaseField):
    _ALLOWED_TYPES = [bool]

    def __init__(
        self,
        name: Optional[str] = None,
        default: Optional[bool] = None,
        validate_default: bool = True,
        nullable: bool = False,
        validators: Optional[Union[BaseValidator, Iterable[BaseValidator]]] = None,
    ):
        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            validators=validators,
        )
