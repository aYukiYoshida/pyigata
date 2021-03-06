# -*- coding: utf-8 -*-

import os
import sys
import inspect
from typing import Union, List, Dict, Tuple
from enum import Enum, IntEnum

###-----------------------------------------------------------------------
### GLOBAL VARIABLES
###-----------------------------------------------------------------------
ROOT_DIR = './'
PKG_DIR = os.path.join(ROOT_DIR, 'src')
OUT_DIR = os.path.join(ROOT_DIR, 'out')
DAT_DIR = os.path.join(ROOT_DIR, 'data')


class StringColor(object):
	BLACK          = '\033[30m' #(文字)黒
	RED            = '\033[31m' #(文字)赤
	GREEN          = '\033[32m' #(文字)緑
	YELLOW         = '\033[33m' #(文字)黄
	BLUE           = '\033[34m' #(文字)青
	MAGENTA        = '\033[35m' #(文字)マゼンタ
	CYAN           = '\033[36m' #(文字)シアン
	WHITE          = '\033[37m' #(文字)白
	COLOR_DEFAULT  = '\033[39m' #文字色をデフォルトに戻す
	BOLD           = '\033[1m'  #太字
	UNDERLINE      = '\033[4m'  #下線
	INVISIBLE      = '\033[08m' #不可視
	REVERSE        = '\033[07m' #文字色と背景色を反転
	BG_BLACK       = '\033[40m' #(背景)黒
	BG_RED         = '\033[41m' #(背景)赤
	BG_GREEN       = '\033[42m' #(背景)緑
	BG_YELLOW      = '\033[43m' #(背景)黄
	BG_BLUE        = '\033[44m' #(背景)青
	BG_MAGENTA     = '\033[45m' #(背景)マゼンタ
	BG_CYAN        = '\033[46m' #(背景)シアン
	BG_WHITE       = '\033[47m' #(背景)白
	BG_DEFAULT     = '\033[49m' #背景色をデフォルトに戻す
	RESET          = '\033[0m'  #全てリセット


class LogLevel(IntEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

    @property
    def color(self):
        return LogStringColor[f'{self.name}'].value

class LogStringColor(Enum):
    DEBUG = StringColor.GREEN
    INFO = StringColor.COLOR_DEFAULT
    WARNING = StringColor.YELLOW
    ERROR = StringColor.RED

class Log(object):
    __RESET_COLOR = StringColor.RESET

    def __init__(self, level:int=1) -> None:
        try:
            self._level = LogLevel(level)
        except ValueError:
            raise ValueError('level should be set to an integer between 0 and 3.')

    @property
    def level(self):
        return self._level

    def logger(self, string:str, log_level:Union[int, LogLevel], frame=None) -> None:
        if isinstance(log_level, int):
            log_level = LogLevel(log_level)
        if not frame is None:
            function_name = inspect.getframeinfo(frame)[2]
            console_msg = f'[{log_level.name}] {function_name} : {str(string)}'
        else:
            console_msg = f'[{log_level.name}] {str(string)}'
        if (log_level >= self.level):
            
            print(f'{log_level.color}{console_msg}{self.__RESET_COLOR}')


    def debug(self,string:str, frame=None) -> None:
        self.logger(string, LogLevel.DEBUG, frame)


    def info(self,string:str, frame=None) -> None:
        self.logger(string, LogLevel.INFO, frame)


    def warning(self,string:str, frame=None) -> None:
        self.logger(string, LogLevel.WARNING, frame)


    def error(self,string:str, frame=None) -> None:
        self.logger(string, LogLevel.ERROR, frame)


class Common(Log):
    def __init__(self, log_level:int=1) -> None:
        super().__init__(log_level)


    def abort(self,string: str,frame=None) -> None:
        self.error(string,frame)
        sys.exit(1)


def get_pkg_name():
    return __package__


def pkg_name(comm : Common):
    comm.logger('PACKAGE NAME = {0}'.format(get_pkg_name()),1)


def is_env_notebook():
    '''Determine wheather is the environment Jupyter Notebook'''
    try:
        env_name = get_ipython().__class__.__name__
    except NameError:
        return False

    if env_name == 'TerminalInteractiveShell':
        # IPython shell
        return False
    else:
        # Jupyter Notebook
        return True

