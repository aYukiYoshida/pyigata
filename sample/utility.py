# -*- coding: utf-8 -*- 

import pandas as _pd
import numpy as _np
from typing import Union as _union

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