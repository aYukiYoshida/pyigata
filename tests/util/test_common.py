# -*- coding: utf-8 -*-
import unittest
from ..context import io 
from ..context import sys
from ..context import common


###-----------------------------------------------------------------------
class TestCommon(unittest.TestCase):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def setUp(self):
    ###-------------------------------------------------------------------
        self.helper = common.Common(loglv=0)
        self.captor = io.StringIO()
        sys.stdout = self.captor


    ###-------------------------------------------------------------------
    def tearDown(self):
    ###-------------------------------------------------------------------
        sys.stdout = sys.__stdout__


    ###-------------------------------------------------------------------
    def test_common_type(self):
    ###-------------------------------------------------------------------
        self.assertIs(type(self.helper),common.Common)


    ###-------------------------------------------------------------------
    def test_logger_debug(self):
    ###-------------------------------------------------------------------
        self.helper.logger('test',0)
        self.assertEqual('[DEBUG] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_info(self):
    ###-------------------------------------------------------------------
        self.helper.logger('test',1)
        self.assertEqual('[INFO] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_warning(self):
    ###-------------------------------------------------------------------
        self.helper.logger('test',2)
        self.assertEqual('[WARNING] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_error(self):
    ###-------------------------------------------------------------------
        self.helper.logger('test',3)
        self.assertEqual('[ERROR] test\n',self.captor.getvalue())


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    unittest.main()