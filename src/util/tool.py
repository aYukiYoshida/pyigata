# -*- coding: utf-8 -*- 

import pandas as _pd
import numpy as _np
from sklearn.preprocessing import LabelEncoder as _LabelEncoder
from .common import Union as _union


###-----------------------------------------------------------------------
def tabular_confusion_matrix(confusion_matrix: _np.ndarray, display_labels:_union[list,None]=None) -> _pd.DataFrame:
###-----------------------------------------------------------------------
    if display_labels is None:
        idx = _pd.MultiIndex.from_arrays([
                ['True']*confusion_matrix.shape[0],
                range(confusion_matrix.shape[0])])
        col = _pd.MultiIndex.from_arrays([
                ['Predicted']*confusion_matrix.shape[1],
                range(confusion_matrix.shape[1])])
    else:
        idx = _pd.MultiIndex.from_arrays([
                ['True']*len(display_labels),
                display_labels])
        col = _pd.MultiIndex.from_arrays([
                ['Predicted']*len(display_labels),
                display_labels])

    table = _pd.DataFrame(confusion_matrix,index=idx,columns=col)
    table['recall'] = _np.diag(confusion_matrix)/confusion_matrix.sum(axis=1)
    table['precision'] = _np.diag(confusion_matrix)/confusion_matrix.sum(axis=0)
    table['accuracy'] = [_np.diag(confusion_matrix).sum()/confusion_matrix.sum()]*confusion_matrix.shape[0]
    return table


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