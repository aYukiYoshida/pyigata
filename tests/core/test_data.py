# -*- coding: utf-8 -*-

import unittest
from ..context import io 
from ..context import sys
from ..context import data


###-----------------------------------------------------------------------
class TestData(unittest.TestCase):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def setUp(self):
    ###-------------------------------------------------------------------
        self.reader = data.Reader(log_level=0)
        self.captor = io.StringIO()
        sys.stdout = self.captor


    ###-------------------------------------------------------------------
    def test_common_type(self):
    ###-------------------------------------------------------------------
        self.assertIs(type(self.reader),data.Reader)


    ###-------------------------------------------------------------------
    def test_read_test_data(self):
    ###-------------------------------------------------------------------
        self.assertIs(type(self.reader.read_test_data()),data.pd.DataFrame)


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    unittest.main()
