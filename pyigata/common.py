# -*- coding: utf-8 -*-

import sys

from pyigata.log import Log


class Common(Log):
    def __init__(self, log_level: int = 1) -> None:
        super().__init__(level=log_level)

    def abort(self, string: str, frame=None) -> None:
        self.error(string, frame)
        sys.exit(1)
