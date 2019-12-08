# -*- coding: utf-8 -*-

import os
import sys
import getopt
import inspect


###-----------------------------------------------------------------------
def get_pkg_name():
###-----------------------------------------------------------------------
    return __package__


###-----------------------------------------------------------------------
def pkg_name(comm : Common):
###-----------------------------------------------------------------------
    comm.logger('PACKAGE NAME = {0}'.format(get_pkg_name()),1)


###-----------------------------------------------------------------------
class Common(object):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,loglv: int = 1) -> None:
    ###-------------------------------------------------------------------
        self.loglv = loglv
        self.pkg_dir = './sample'
        self.out_dir = './out'


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
class Help(Common):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,args: list) -> None:
    ###-------------------------------------------------------------------
        super().__init__(loglv=1)
        self.cmd = os.path.basename(args[0])
        self.par = args[1:]
        self.image = False


    ###-------------------------------------------------------------------
    def usage(self) -> None:
    ###-------------------------------------------------------------------
        print('USAGE')
        print('  %s [OPTIONS] <TEXT>' %(self.cmd))
        print('')
        print('OPTIONS')
        print('  -u,--usage      show this help message')
        print('  -t,--test       run test')
        sys.exit(0)
        

    ###-------------------------------------------------------------------
    def parser(self) -> bool:
    ###-------------------------------------------------------------------
        try:
            opts, args = getopt.gnu_getopt(self.par, "uitc",
                                           [ "usage",
                                             "loglv=",
                                             "test" ])
                                                             
        except getopt.GetoptError as err:
            self.abort(err,inspect.currentframe())

        self.logger('opts: %s'%(opts),0,inspect.currentframe())
        self.logger('args: %s'%(args),0,inspect.currentframe())

        loglv   = 2
        test    = False

        for opt, arg in opts:
            self.logger('opt: %s'%(opt),0,inspect.currentframe())
            self.logger('arg: %s'%(arg),0,inspect.currentframe())
            if opt in   ( "-u", "--usage"):
                self.usage()
            elif opt in (       "--loglv"):
                loglv = int(arg)
            elif opt in ( "-t", "--test"):
                test = True
            else:
                self.abort("unhandled option",inspect.currentframe())

        if ( len(args) == 1 ):
            cmd = args[0]
            self.logger('cmd: %s'%(cmd),0,inspect.currentframe())
            if cmd in (   'test',        'TEST' ):
                test = True
            else:
                self.abort('invalid command',inspect.currentframe())
                
        return loglv,test