# -*- coding: utf-8 -*-
import io
import sys

from pytest import fixture
from pytest_bdd import scenario, given, when, then, parsers

from pyigata import Common

# Scenarios
@scenario('bdd.feature', 'デバッグログ出力')
def test_logger_debug():
    pass

@scenario('bdd.feature', 'インフォメーションログ出力')
def test_logger_info():
    pass

# Fixtures
@fixture(autouse=False)
def captor():
    captor = io.StringIO()
    sys.stdout = captor
    yield captor
    sys.stdout = sys.__stdout__
    del captor

@fixture(autouse=False)
def message():
    return 'test'

@given(parsers.parse('level={log_level}のログレベルがロガーに与えられる'),
      target_fixture='logger')
def logger(log_level):
    return Common(log_level=int(log_level))

@when(parsers.parse('level={log_level}のログの出力を実行する'))
def logging(logger, message, log_level):
    if log_level == 0:
        logger.debug(message)
    elif log_level == 1:
        logger.info(message)

@then(parsers.parse('level={log_level}のログが出力される'))
def no_error_message(logger: Common, log_level):
    assert logger.level == int(log_level)
