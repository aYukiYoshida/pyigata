# -*- coding: utf-8 -*-
import logging
import sys
from enum import IntEnum


class LogLevel(IntEnum):
    CRITICAL = 5
    ERROR = 4
    WARNING = 3
    INFO = 2
    DEBUG = 1
    NOTSET = 0


def get_logger(name: str, level: int = 2) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.getLevelName(LogLevel(level).name.upper()))
    if not logger.hasHandlers():
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt=r"%Y-%m-%dT%H:%M:%S%z")
        # INFO以下のログを標準出力する
        stdout_handler = logging.StreamHandler(stream=sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)
        stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)
        logger.addHandler(stdout_handler)
        # WARNING以上のログを標準エラー出力する
        stderr_handler = logging.StreamHandler(stream=sys.stderr)
        stderr_handler.setLevel(logging.WARNING)
        stderr_handler.setFormatter(formatter)
        logger.addHandler(stderr_handler)
    return logger


__all__ = ["get_logger"]
