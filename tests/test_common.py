# -*- coding: utf-8 -*-
import unittest
from .context import io 
from .context import sys
from .context import Common, STRING_COLORS


class TestCommon(unittest.TestCase):
    def setUp(self):
        self.helper = Common(log_level=0)
        self.captor = io.StringIO()
        sys.stdout = self.captor


    def tearDown(self):
        sys.stdout = sys.__stdout__


    def test_common_type(self):
        self.assertIs(type(self.helper), Common)


    def test_logger_debug(self):
        self.helper.debug('test')
        self.assertEqual(
            f'{STRING_COLORS.GREEN}[DEBUG] test{STRING_COLORS.RESET}\n',
            self.captor.getvalue())


    def test_logger_info(self):
        self.helper.info('test')
        self.assertEqual(
            f'{STRING_COLORS.COLOR_DEFAULT}[INFO] test{STRING_COLORS.RESET}\n',
            self.captor.getvalue())


    def test_logger_warning(self):
        self.helper.warning('test')
        self.assertEqual(
            f'{STRING_COLORS.YELLOW}[WARNING] test{STRING_COLORS.RESET}\n',
            self.captor.getvalue())


    def test_logger_error(self):
        self.helper.error('test')
        self.assertEqual(
            f'{STRING_COLORS.RED}[ERROR] test{STRING_COLORS.RESET}\n',
            self.captor.getvalue())


if __name__ == '__main__':
    unittest.main()