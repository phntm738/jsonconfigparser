from typing import Optional, Any, Union, Iterable
from jsonconfigparser.validators import BasicValidator
from jsonconfigparser import exceptions


class BasicField:
    def __init__(
            self,
            name: Optional[str] = None,
            default: Optional[Any] = None,
            validate_default: bool = True,
            nullable: bool = False,
            validators: Optional[Union[BasicValidator, Iterable[BasicValidator]]] = None
    ):
        self._name = name
        self._value = None
        self._default = default
        self._nullable = nullable

        self._init_validators_list()

        if validators is not None:
            if not isinstance(validators, Iterable):
                self._validators.append(validators)
            else:
                self._validators += list(validators)

        if validate_default and default is not None:
            try:
                self._validate(self._default)
            except exceptions.ValidationFailedError as e:
                raise exceptions.DefaultValueValidationFailedError(self.name, e.msg)

    def _init_validators_list(self):
        if not hasattr(self, '_validators') or not isinstance(self._validators, list):
            self._validators = []

    def _validate(self, value: Any):
        for validator in self._validators:
            if not validator.validate(value):
                raise exceptions.ValidationFailedError(self.name, validator.name)

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise exceptions.InvalidNameError(msg=f"Expected type {str} got {type(new_name)} instead")
        self._name = new_name

    def value(self) -> Any:
        if self._value is None:
            self._value = self._default
        if self._value is None and not self._nullable:
            raise exceptions.NoValueError(self.name)
        return self._value

    def set_value(self, new_value: Any) -> None:
        self._validate(new_value)
        self._value = new_value


__all__ = (
    'BasicField',
)
