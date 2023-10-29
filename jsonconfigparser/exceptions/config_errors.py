from .base import JConfParserError


class ConfigError(JConfParserError):
    """
    Base class for all JConfig-level exceptions
    """

    pass


class InvalidPathError(ConfigError):
    pass


class InvalidFileFormatError(ConfigError):
    def __str__(self) -> str:
        return ".json file expected"


class DecodingError(ConfigError):
    pass


class ConfigFormatError(ConfigError):
    def __str__(self) -> str:
        return "JSON object (key-value pairs) expected"
