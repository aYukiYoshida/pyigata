# -*- coding: utf-8 -*-

import os
import sys
import inspect
from typing import Union, List, Dict, Tuple


###-----------------------------------------------------------------------
### GLOBAL VARIABLES
###-----------------------------------------------------------------------
ROOT_DIR = './'
PKG_DIR = os.path.join(ROOT_DIR, 'src')
OUT_DIR = os.path.join(ROOT_DIR, 'out')
DAT_DIR = os.path.join(ROOT_DIR, 'data')


###-----------------------------------------------------------------------
class Log(object):
###-----------------------------------------------------------------------
    STATUS = {
        0 : 'DEBUG',
        1 : 'INFO',
        2 : 'WARNING',
        3 : 'ERROR' }


    ###-------------------------------------------------------------------
    def __init__(self,loglv: Union[int, str] = 1) -> None:
    ###-------------------------------------------------------------------
        if type(loglv) is str:
            try:
                loglv = list(self.STATUS.values()).index(loglv.upper())
            except ValueError:
                raise ValueError(f'loglv should be set to an integer between 0 and 3 or a one of '+', '.join(self.STATUS.values())+'.')
        self.loglv: int = loglv


    ###-------------------------------------------------------------------
    def logger(self,string: str,level: int, frame=None) -> None:
    ###-------------------------------------------------------------------
        if not frame == None:
            function_name = inspect.getframeinfo(frame)[2]
            console_msg = f'[{self.STATUS[level]}] {function_name} : {str(string)}'
        else:
            console_msg = f'[{self.STATUS[level]}] {str(string)}'
        if (level >= self.loglv):
            print(console_msg)


    ###-------------------------------------------------------------------
    def debug(self,string: str, frame=None) -> None:
    ###-------------------------------------------------------------------
        self.logger(string,0,frame)


    ###-------------------------------------------------------------------
    def info(self,string: str, frame=None) -> None:
    ###-------------------------------------------------------------------
        self.logger(string,1,frame)


    ###-------------------------------------------------------------------
    def warning(self,string: str, frame=None) -> None:
    ###-------------------------------------------------------------------
        self.logger(string,2,frame)


    ###-------------------------------------------------------------------
    def error(self,string: str, frame=None) -> None:
    ###-------------------------------------------------------------------
        self.logger(string,3,frame)


###-----------------------------------------------------------------------
class Common(Log):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,loglv: Union[int, str] = 1) -> None:
    ###-------------------------------------------------------------------
        super().__init__(loglv)


    ###-------------------------------------------------------------------
    def abort(self,string: str,frame=None) -> None:
    ###------------------------------------------------------------------
        self.error(string,frame)
        sys.exit(1)


###-----------------------------------------------------------------------
def get_pkg_name():
###-----------------------------------------------------------------------
    return __package__


###-----------------------------------------------------------------------
def pkg_name(comm : Common):
###-----------------------------------------------------------------------
    comm.logger('PACKAGE NAME = {0}'.format(get_pkg_name()),1)


###-----------------------------------------------------------------------
def is_env_notebook():
###-----------------------------------------------------------------------
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

