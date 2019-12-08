# -*- coding: utf-8 -*-

import os
import inspect
import pandas as pd

from .core import Common


###-----------------------------------------------------------------------
class Manager(Common):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    ### CLASS VARIABLES
    ###-------------------------------------------------------------------
    TEST_DATA = { 'dummy' : 'dummy.csv' }


    ###-------------------------------------------------------------------
    def __init__(self,loglv: int = 1) -> None:
    ###-------------------------------------------------------------------
        super().__init__(loglv)


###-----------------------------------------------------------------------
class Reader(Manager):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,loglv: int):
    ###-------------------------------------------------------------------
        super().__init__(loglv)
        root_dir = os.path.dirname(self.pkg_dir)
        self.data_dir = os.path.join(root_dir,'data')


    ###-------------------------------------------------------------------
    def readTestData(self, context: str = 'dummy') -> pd.DataFrame:
    ###-------------------------------------------------------------------
        self.logger('START',0,inspect.currentframe())
        self.logger('READ TEST DATA',1)
                
        test_data_csv = os.path.join(self.data_dir,self.TEST_DATA[context])
        self.logger('  FILE: %s'%(test_data_csv),1)
        
        data_frame = pd.read_csv(test_data_csv)
        self.logger('  SIZE OF TEST DATA: %d'%(data_frame.index.size),1)

        self.logger('END',0,inspect.currentframe())
        return data_frame


###-----------------------------------------------------------------------
class Editor(Manager):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,loglv: int):
    ###-------------------------------------------------------------------
        super().__init__(loglv)