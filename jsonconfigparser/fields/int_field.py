from fields.float_field import FloatField
from .validation import BaseValidator
from typing import Optional, Union, Iterable


class IntField(FloatField):
    _ALLOWED_TYPES = [int]

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
        validators: Optional[Union[BaseValidator, Iterable[BaseValidator]]] = None,
    ):
        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            validators=validators,
        )
