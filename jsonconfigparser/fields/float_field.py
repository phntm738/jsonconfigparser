from fields.base_field import BaseField
from .validation import BaseValidator, ComparisonValidator
from typing import Optional, Union, Iterable


class FloatField(BaseField):
    _ALLOWED_TYPES = [int, float]

    def __init__(
        self,
        name: Optional[str] = None,
        default: Optional[Union[int, float]] = None,
        validate_default: bool = True,
        nullable: bool = False,
        gt: Optional[Union[int, float]] = None,
        ge: Optional[Union[int, float]] = None,
        lt: Optional[Union[int, float]] = None,
        le: Optional[Union[int, float]] = None,
        validators: Optional[Union[BaseValidator, Iterable[BaseValidator]]] = None,
    ):
        if not all([gt is None, ge is None, lt is None, le is None]):
            self._validators.append(ComparisonValidator(gt, ge, lt, le))

        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            validators=validators,
        )
