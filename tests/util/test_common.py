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
        self.helper.debug('test')
        self.assertEqual(
            f'{common.StringColor.COLOR_DEFAULT}[DEBUG] test{common.StringColor.RESET}\n',
            self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_info(self):
    ###-------------------------------------------------------------------
        self.helper.info('test')
        self.assertEqual(
            f'{common.StringColor.COLOR_DEFAULT}[INFO] test{common.StringColor.RESET}\n',
            self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_warning(self):
    ###-------------------------------------------------------------------
        self.helper.warning('test')
        self.assertEqual(
            f'{common.StringColor.YELLOW}[WARNING] test{common.StringColor.RESET}\n',
            self.captor.getvalue())


    ###-------------------------------------------------------------------
    def test_logger_error(self):
    ###-------------------------------------------------------------------
        self.helper.error('test')
        self.assertEqual(
            f'{common.StringColor.RED}[ERROR] test{common.StringColor.RESET}\n',
            self.captor.getvalue())


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    unittest.main()