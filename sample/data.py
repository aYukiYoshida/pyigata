# -*- coding: utf-8 -*-

import pandas as _pd
import numpy as _np
from sklearn.preprocessing import _LabelEncoder

from .core import inspect
from .core import os
from .core import Common
from .core import Union as _union


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
    def readTestData(self, context: str = 'dummy') -> _pd.DataFrame:
    ###-------------------------------------------------------------------
        self.logger('START',0,inspect.currentframe())
        self.logger('READ TEST DATA',1)
                
        test_data_csv = os.path.join(self.data_dir,self.TEST_DATA[context])
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


###-----------------------------------------------------------------------
def convert_categorical_to_onehot(array:_union[_np.ndarray,_pd.Series,_pd.DataFrame], classes_number:int=None) -> _np.ndarray:
###-----------------------------------------------------------------------
    if type(array) is _pd.Series or type(array) is _pd.DataFrame:
        array = array.values
    if classes_number is None:
        classes_number = _np.unique(array)

    return _np.squeeze(_np.eye(classes_number)[array.reshape(-1)])


###-----------------------------------------------------------------------
def convert_categorical_to_label(array:_union[_np.ndarray,_pd.Series], classes_number:int) -> _np.ndarray:
###-----------------------------------------------------------------------
    le = _LabelEncoder()
    return le.fit_transform(array)