# -*- coding: utf-8 -*-

from typing import Union

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder as _LabelEncoder


def tabular_confusion_matrix(confusion_matrix: np.ndarray, display_labels: Union[list, None] = None) -> pd.DataFrame:
    if display_labels is None:
        idx = pd.MultiIndex.from_arrays([["True"] * confusion_matrix.shape[0], range(confusion_matrix.shape[0])])
        col = pd.MultiIndex.from_arrays(
            [
                ["Predicted"] * confusion_matrix.shape[1],
                range(confusion_matrix.shape[1]),
            ]
        )
    else:
        idx = pd.MultiIndex.from_arrays([["True"] * len(display_labels), display_labels])
        col = pd.MultiIndex.from_arrays([["Predicted"] * len(display_labels), display_labels])

    table = pd.DataFrame(confusion_matrix, index=idx, columns=col)
    table["recall"] = np.diag(confusion_matrix) / confusion_matrix.sum(axis=1)
    table["precision"] = np.diag(confusion_matrix) / confusion_matrix.sum(axis=0)
    table["accuracy"] = [np.diag(confusion_matrix).sum() / confusion_matrix.sum()] * confusion_matrix.shape[0]
    return table


def convert_categorical_to_onehot(array: Union[np.ndarray, pd.Series, pd.DataFrame], classes_number: int = None) -> np.ndarray:
    if type(array) is pd.Series or type(array) is pd.DataFrame:
        array = array.values
    if classes_number is None:
        classes_number = np.unique(array)

    return np.squeeze(np.eye(classes_number)[array.reshape(-1)])


def convert_categorical_to_label(
    array: Union[list, np.ndarray, pd.Series],
    label: Union[list, np.ndarray, pd.Series] = None,
) -> np.ndarray:
    le = _LabelEncoder()
    if label is not None:
        le = le.fit(label)
        return le.transform(array)
    else:
        return le.fit_transform(array)
