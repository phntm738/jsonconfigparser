from .base import JConfParserError


class ValidatorError(JConfParserError):
    """
    Base class for all Validator-level errors
    """

    pass


class InvalidArgumentError(ValidatorError):
    """
    An argument has wrong type or invalid value
    """

    pass
