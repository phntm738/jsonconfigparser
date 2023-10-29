from .base import JConfParserError


class FieldError(JConfParserError):
    """
    Base class for all Field-level exceptions
    """

    pass


class InvalidDefaultTypeError(FieldError):
    """
    Field's default value's type is not allowed for that field
    """

    pass


class InvalidDefaultError(FieldError):
    """
    Field's default value fails validation
    """

    pass


class InvalidArgumentError(FieldError):
    """
    An argument has wrong type or invalid value
    """

    pass


class NoValueError(FieldError):
    """
    Non-nullable field does not contain a value
    """

    pass


class InvalidValueTypeError(FieldError):
    """
    Existing or new value's type is not allowed for that field
    """

    pass


class InvalidValueError(FieldError):
    """
    New value for field fails validation
    """

    pass


class NoNameError(FieldError):
    """
    Field does not have a name
    """

    pass


class InvalidNameTypeError(FieldError):
    """
    Existing or new name's type is not str
    """

    pass
