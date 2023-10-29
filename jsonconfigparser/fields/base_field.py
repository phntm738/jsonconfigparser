from typing import Optional, Any, Union, Iterable, ClassVar
from .validation import BaseValidator
from jsonconfigparser.exceptions import field_errors as errors


class BaseField:
    _ALLOWED_TYPES: ClassVar[list[type]] = []

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._validators = []
        return obj

    def __init__(
        self,
        name: Optional[str] = None,
        default: Optional[Any] = None,
        validate_default: bool = True,
        nullable: bool = False,
        validators: Optional[Union[BaseValidator, Iterable[BaseValidator]]] = None,
    ):
        self._name = name
        self._value = None
        self._nullable = nullable

        if default is not None and not self._type_allowed(default):
            raise errors.InvalidDefaultTypeError
        self._default = default

        if validators is not None:
            if not isinstance(validators, Iterable):
                self._validators.append(validators)
            else:
                self._validators += list(validators)

        if validate_default and default is not None:
            try:
                self._validate(self._default)
            except errors.InvalidValueError as e:
                raise errors.InvalidDefaultError(f"Invalid default value. {e}")

    def _validate(self, value: Any):
        for validator in self._validators:
            if not validator.validate(value):
                raise errors.InvalidValueError(
                    f"Validation failed on validator {validator.name}"
                )

    def _type_allowed(self, value: Any) -> bool:
        if not self._ALLOWED_TYPES:
            return True
        return type(value) in self._ALLOWED_TYPES

    @staticmethod
    def _name_required(func):
        def wrapper(self, *args, **kwargs):
            if self._name is None:
                raise errors.NoNameError(
                    f"Name required to execute '{func.__name__}' method"
                )
            return func(self, *args, **kwargs)

        return wrapper

    @property
    def name(self) -> Optional[str]:
        if not isinstance(self._name, str):
            raise errors.InvalidNameTypeError(
                f"Field's name is expected to be {str}, is {type(self._name)} instead"
            )
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise errors.InvalidNameTypeError(
                f"Expected type {str} for field '{self.name}', got {type(new_name)} instead"
            )
        self._name = new_name

    @_name_required
    def value(self) -> Any:
        if self._value is None:
            self._value = self._default
        if self._value is None and not self._nullable:
            raise errors.NoValueError(
                f"Field '{self.name}' is non-nullable and does not contain any value"
            )
        if self._value is not None and not self._type_allowed(self._value):
            raise errors.InvalidValueTypeError(
                f"Field '{self.name}' expected to contain value of type(s) {self._ALLOWED_TYPES}, contains type {type(self._value)} instead"
            )
        return self._value

    @_name_required
    def set_value(self, new_value: Any) -> None:
        if not self._type_allowed(new_value):
            raise errors.InvalidValueTypeError(
                f"Field '{self.name}' accepts values of type(s) {self._ALLOWED_TYPES}, got type {type(new_value)} instead"
            )
        try:
            self._validate(new_value)
        except errors.InvalidValueError as e:
            raise errors.InvalidValueError(
                f"Invalid value for field '{self.name}'. {e}"
            )
        self._value = new_value
