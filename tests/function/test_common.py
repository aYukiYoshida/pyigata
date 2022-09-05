# -*- coding: utf-8 -*-
import io
import sys
import unittest

from pyigata import Common
from pyigata.color import StringColor


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
        self.helper.debug("test")
        self.assertEqual(
            f"{StringColor.GREEN}[DEBUG] test{StringColor.RESET}\n",
            self.captor.getvalue(),
        )

    def test_logger_info(self):
        self.helper.info("test")
        self.assertEqual(
            f"{StringColor.DEFAULT}[INFO] test{StringColor.RESET}\n",
            self.captor.getvalue(),
        )

    def test_logger_warning(self):
        self.helper.warning("test")
        self.assertEqual(
            f"{StringColor.YELLOW}[WARNING] test{StringColor.RESET}\n",
            self.captor.getvalue(),
        )

    def test_logger_error(self):
        self.helper.error("test")
        self.assertEqual(
            f"{StringColor.RED}[ERROR] test{StringColor.RESET}\n",
            self.captor.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()
