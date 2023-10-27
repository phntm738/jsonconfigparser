import typing
import os
import jsonconfigparser.exceptions as exceptions
import json


class JConfig:
    def __init__(self):
        pass

    def read(self, path: str) -> None:
        if not os.path.exists(path):
            raise exceptions.InvalidPathError(f"Path: ({path}) does not exist")
        if not path.endswith(".json"):
            raise exceptions.InvalidFileFormatError

        with open(path) as config_file:
            self.readf(config_file)

    def readf(self, fp: typing.TextIO) -> None:
        try:
            conf_dict: dict = json.load(fp)
            if type(conf_dict) != dict:
                raise exceptions.ConfigFormatError

        except json.JSONDecodeError as e:
            raise exceptions.DecodingError(str(e))
