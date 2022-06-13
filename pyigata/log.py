# -*- coding: utf-8 -*-

import inspect
from enum import Enum, IntEnum
from typing import Union

from pyigata.color import StringColor


class LogLevel(IntEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

    @property
    def color(self):
        return LogStringColor[f"{self.name}"].value


class LogStringColor(Enum):
    DEBUG = StringColor.GREEN
    INFO = StringColor.DEFAULT
    WARNING = StringColor.YELLOW
    ERROR = StringColor.RED


class Log(object):
    __RESET_COLOR = StringColor.RESET

    def __init__(self, level: int = 1) -> None:
        try:
            self._level = LogLevel(level)
        except ValueError:
            raise ValueError("level should be set to an integer between 0 and 3.")

    @property
    def level(self):
        return self._level

    def logger(self, string: str, log_level: Union[int, LogLevel], frame=None) -> None:
        if isinstance(log_level, int):
            log_level = LogLevel(log_level)
        if frame:
            function_name = inspect.getframeinfo(frame)[2]
            console_msg = f"[{log_level.name}] {function_name} : {str(string)}"
        else:
            console_msg = f"[{log_level.name}] {str(string)}"
        if log_level >= self.level:
            print(f"{log_level.color}{console_msg}{self.__RESET_COLOR}")

    def debug(self, string: str, frame=None) -> None:
        self.logger(string, LogLevel.DEBUG, frame)

    def info(self, string: str, frame=None) -> None:
        self.logger(string, LogLevel.INFO, frame)

    def warning(self, string: str, frame=None) -> None:
        self.logger(string, LogLevel.WARNING, frame)

    def error(self, string: str, frame=None) -> None:
        self.logger(string, LogLevel.ERROR, frame)
