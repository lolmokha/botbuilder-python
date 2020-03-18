import os
from configparser import ConfigParser

from .configuration import Configuration


class ConfigParserConfiguration(Configuration):
    """
    An implementation of Configuration that uses ConfigParser to store properties.

    If the value isn't in the settings file, the environment is checked for a value with the
    same name.
    """

    def __init__(self, path: str = "appsettings.properties"):
        self.config = ConfigParser()
        self.config.read(path)

    def get(self, key: str) -> str:
        # For a bot, the [bot] section is used.
        value = self.config.get("bot", key)
        if not value:
            value = os.environ.get(key)
        return value