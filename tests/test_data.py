# -*- coding: utf-8 -*-

from .context import sample

import unittest
import io 
import sys


###-----------------------------------------------------------------------
class TestData(unittest.TestCase):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def test_common_type(self):
    ###-------------------------------------------------------------------
        loglv = 0
        reader = sample.Reader(loglv=loglv)
        self.assertIs(type(reader),sample.Reader)


    ###-------------------------------------------------------------------
    def test_readTestData(self):
    ###-------------------------------------------------------------------
        loglv = 3
        reader = sample.Reader(loglv=loglv)
        self.assertIs(type(reader.readTestData()),sample.data.pd.DataFrame)


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    unittest.main()
