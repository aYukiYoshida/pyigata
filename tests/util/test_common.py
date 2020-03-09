# -*- coding: utf-8 -*-
import unittest
from ..context import io 
from ..context import sys
from ..context import src


###-----------------------------------------------------------------------
class TestCommon(unittest.TestCase):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    def setUp(self):
    ###-------------------------------------------------------------------
        self.captor = io.StringIO()
        sys.stdout = self.captor


    ###-------------------------------------------------------------------
    def tearDown(self):
    ###-------------------------------------------------------------------
        sys.stdout = sys.__stdout__


    ###-------------------------------------------------------------------
    def test_common_type(self):
    ###-------------------------------------------------------------------
        loglv = 0
        common = src.util.Common(loglv=loglv)
        self.assertIs(type(common),src.util.Common)


    ###-------------------------------------------------------------------
    def test_logger_debug(self):
    ###-------------------------------------------------------------------
        loglv = 0
        common = src.util.Common(loglv=loglv)
        common.logger('test',0)
        self.assertEqual('[DEBUG] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_info(self):
    ###-------------------------------------------------------------------
        loglv = 0
        common = src.util.Common(loglv=loglv)
        common.logger('test',1)
        self.assertEqual('[INFO] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_warning(self):
    ###-------------------------------------------------------------------
        loglv = 0
        common = src.util.Common(loglv=loglv)
        common.logger('test',2)
        self.assertEqual('[WARNING] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_error(self):
    ###-------------------------------------------------------------------
        loglv = 0
        common = src.util.Common(loglv=loglv)
        common.logger('test',3)
        self.assertEqual('[ERROR] test\n',self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_pkg_name(self):
    ###-------------------------------------------------------------------
        loglv = 0
        common = src.util.Common(loglv=loglv)
        self.assertIsNone(src.util.pkg_name(common))


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    unittest.main()