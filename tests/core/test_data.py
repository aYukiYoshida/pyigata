# -*- coding: utf-8 -*-

import unittest
from ..context import io 
from ..context import sys
from ..context import src


###-----------------------------------------------------------------------
class TestData(unittest.TestCase):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def test_common_type(self):
    ###-------------------------------------------------------------------
        loglv = 0
        reader = src.core.Reader(loglv=loglv)
        self.assertIs(type(reader),src.core.Reader)


    ###-------------------------------------------------------------------
    def test_readTestData(self):
    ###-------------------------------------------------------------------
        loglv = 3
        reader = src.core.Reader(loglv=loglv)
        self.assertIs(type(reader.readTestData()),src.core.data._pd.DataFrame)


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    unittest.main()
