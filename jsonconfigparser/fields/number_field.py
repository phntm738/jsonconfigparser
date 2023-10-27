from fields.basic_field import BasicField
from validators import BasicValidator, NumberComparisonValidator
from jsonconfigparser import exceptions
from typing import Optional, Union, Iterable


class NumberField(BasicField):
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
            validators: Optional[Union[BasicValidator, Iterable[BasicValidator]]] = None
    ):
        if default is not None and not (isinstance(default, int) or isinstance(default, float)):
            raise exceptions.InvalidDefaultType(
                name,
                f"expected default of type {int} or {float}, got {type(default)} instead"
            )

        if gt is not None and ge is not None:
            raise exceptions.InvalidParametersError(
                name,
                "'greater than' and 'greater or equal' constraints defined at the same time"
            )
        if lt is not None and le is not None:
            raise exceptions.InvalidParametersError(
                name,
                "'less than' and 'less or equal' constraints defined at the same time"
            )

        if gt is not None:
            if lt is not None and lt <= gt:
                raise exceptions.InvalidParametersError(
                    name,
                    "'greater than' and 'less than' constraints contradict each other"
                )
            if le is not None and le <= gt:
                raise exceptions.InvalidParametersError(
                    name,
                    "'greater than' and 'less or equal' constraints contradict each other"
                )
        if ge is not None:
            if lt is not None and lt <= ge:
                raise exceptions.InvalidParametersError(
                    name,
                    "'greater or equal' and 'less than' constraints contradict each other"
                )
            if le is not None and le < ge:
                raise exceptions.InvalidParametersError(
                    name,
                    "'greater or equal' and 'less or equal' constraints contradict each other"
                )

        self._init_validators_list()

        if not all([gt is None, ge is None, lt is None, le is None]):
            self._validators.append(NumberComparisonValidator(gt, ge, lt, le))

        super().__init__(
            name=name,
            default=default,
            validate_default=validate_default,
            nullable=nullable,
            validators=validators
        )

    def value(self) -> Union[int, float, None]:
        rv = super().value()
        if rv is not None and not (isinstance(rv, int) or isinstance(rv, float)):
            raise exceptions.InvalidValueError(
                self.name,
                f"field is expected to contain {int} or {float}, contains {type(rv)} instead"
            )
        return rv

    def set_value(self, new_value: Union[int, float]) -> None:
        if not (isinstance(new_value, int) or isinstance(new_value, float)):
            raise exceptions.InvalidValueError(
                self.name,
                f"field accepts values of type {int} or {float}, got {type(new_value)} instead"
            )
        super().set_value(new_value)


__all__ = (
    'NumberField'
)
