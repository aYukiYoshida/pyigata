# -*- coding: utf-8 -*-

import pandas as _pd
import numpy as _np

from ..util.common import inspect
from ..util.common import os
from ..util.common import Common, PKG_DIR, OUT_DIR, DAT_DIR
from ..util.common import Union as _union


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


    ###-------------------------------------------------------------------
    def readTestData(self, context: str = 'dummy') -> _pd.DataFrame:
    ###-------------------------------------------------------------------
        self.logger('START',0,inspect.currentframe())
        self.logger('READ TEST DATA',1)
                
        test_data_csv = os.path.join(DAT_DIR,self.TEST_DATA[context])
        self.logger('  FILE: %s'%(test_data_csv),1)
        
        data_frame = _pd.read_csv(test_data_csv)
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
