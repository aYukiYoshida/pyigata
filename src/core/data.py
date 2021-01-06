# -*- coding: utf-8 -*-

import pandas as pd

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
    def __init__(self,log_level: int = 1) -> None:
    ###-------------------------------------------------------------------
        super().__init__(log_level)


###-----------------------------------------------------------------------
class Reader(Manager):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,log_level: int):
    ###-------------------------------------------------------------------
        super().__init__(log_level)


    ###-------------------------------------------------------------------
    def read_test_data(self, context: str = 'dummy') -> pd.DataFrame:
    ###-------------------------------------------------------------------
        self.debug('START',inspect.currentframe())
        self.info('READ TEST DATA')

        test_data_csv = os.path.join(DAT_DIR,self.TEST_DATA[context])
        self.info('  FILE: %s'%(test_data_csv))

        data_frame = pd.read_csv(test_data_csv)
        self.info('  SIZE OF TEST DATA: %d'%(data_frame.index.size))

        self.debug('END',inspect.currentframe())
        return data_frame


###-----------------------------------------------------------------------
class Editor(Manager):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def __init__(self,log_level: int):
    ###-------------------------------------------------------------------
        super().__init__(log_level)
