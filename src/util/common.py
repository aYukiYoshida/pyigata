# -*- coding: utf-8 -*-

import os
import sys
import inspect
from typing import Union
from box import Box


###-----------------------------------------------------------------------
### GLOBAL VARIABLES
###-----------------------------------------------------------------------
PKG_DIR = './src'
OUT_DIR = './out'


###-----------------------------------------------------------------------
class Common(object):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,loglv: int = 1) -> None:
    ###-------------------------------------------------------------------
        self.loglv = loglv
        self.pkg_dir = PKG_DIR
        self.out_dir = OUT_DIR


    ###-------------------------------------------------------------------
    def logger(self,string: str,level: int, frame=None) -> None:
    ###-------------------------------------------------------------------
        status = { 0 : 'DEBUG',
                   1 : 'INFO',
                   2 : 'WARNING',
                   3 : 'ERROR' }
        if not frame == None:
            function_name = inspect.getframeinfo(frame)[2]
            console_msg = '[%s] %s : %s'%(status[level],function_name,str(string))
        else:
            console_msg = '[%s] %s'%(status[level],str(string))
        if (level >= self.loglv):
            print(console_msg)


    ###-------------------------------------------------------------------
    def abort(self,string: str,frame=None) -> None:
    ###------------------------------------------------------------------
        self.logger(string,3,frame)
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

