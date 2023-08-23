# -*- coding: utf-8 -*-
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Record:
    _record: list[str]
    status: int = 0

    def __post_init__(self):
        self._index: int = 0

    def __iter__(self):
        # __next__メソッドが定義されているオブジェクトを返すように定義する
        return self

    def __next__(self):
        if self._index == len(self._record):
            raise StopIteration()
        data = self._record[self._index]
        self._index += 1
        return data

    def __getitem__(self, i):
        return self._record[i]

    @classmethod
    def generate(cls, message: str, status: int) -> Record:
        return cls([message], status)
