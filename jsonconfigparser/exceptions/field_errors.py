from jsonconfigparser.exceptions.base import JConfParserError
from typing import Optional


class FieldError(JConfParserError):
    """
    Base class for all Field-level exceptions
    """
    def __init__(self, field_name: Optional[str] = None, msg: Optional[str] = None):
        self.field_name = field_name
        self.msg = msg
        super().__init__()


class InvalidDefaultType(FieldError):
    def __str__(self):
        if self.field_name is not None:
            return f"Invalid default type for field '{self.field_name}': {self.msg}"
        return f"Invalid default type for field: {self.msg}"


class InvalidParametersError(FieldError):
    def __str__(self) -> str:
        if self.field_name is not None:
            return f"Invalid parameters for field '{self.field_name}': {self.msg}"
        return f"Invalid parameters for field: {self.msg}"


class NoValueError(FieldError):
    def __str__(self) -> str:
        if self.field_name is not None:
            return f"No value was set for field '{self.field_name}'"
        return "No value was set for required field"


class InvalidValueError(FieldError):
    def __str__(self) -> str:
        if self.field_name is not None:
            return f"Invalid value for field '{self.field_name}': {self.msg}"
        return f"Invalid value for field: {self.msg}"


class InvalidNameError(FieldError):
    def __str__(self) -> str:
        return f"Invalid name for field: {self.msg}"


class ValidationFailedError(FieldError):
    def __str__(self) -> str:
        if self.field_name is not None:
            return f"Value for field '{self.field_name}' failed validation on validator '{self.msg}'"
        return f"Value failed validation on validator '{self.msg}'"


class DefaultValueValidationFailedError(ValidationFailedError):
    def __str(self) -> str:
        if self.field_name is not None:
            return f"Default value for field '{self.field_name}' failed validation on validator '{self.msg}'"
        return f"Default value failed validation on validator '{self.msg}'"
