#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys

import src
from absl import app
from absl import flags


###-----------------------------------------------------------------------
def main(argv):
###-----------------------------------------------------------------------
    if flag_values.debug:
        flag_values.loglv = 0
    logger = src.common.Common(flag_values.loglv)

    command_flags_list = [ flag_values.practice, flag_values.test, flag_values.exercise ]
    if len([ command_flag for command_flag in command_flags_list if command_flag is not None]) == 1:
        if flag_values.practice:
            message = f'practicing in mode of {flag_values.practice}'
        elif flag_values.test is not None:
            message = f'testing in mode of {flag_values.test}'
        elif flag_values.exercise:
            message = f'exercising in mode of {flag_values.exercise}'
        logger.info(f'{flag_values.name} is {message}')
        logger.debug(f'{flag_values.name} is {message} with debug mode')
    else:
        logger.error('Please input command !!')
        logger.abort('Try --help to get a list of flags !!')


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    flag_values = flags.FLAGS
    flags.DEFINE_boolean('debug', False, 'run with debug mode.')
    flags.DEFINE_enum('loglv', 'INFO', ['DEBUG', 'debug', 'INFO', 'info', 'WARNING', 'warning', 'ERROR', 'error'], 'Logging level.')
    flags.DEFINE_string('name', 'Yuki Yoshida', 'Your name.')
    flags.DEFINE_enum('practice', None, ['a', 'b', 'c'], 'This is one of the command. Practice mode.')
    flags.DEFINE_integer('test', None, 'This is one of the command. Test mode.', lower_bound=0, upper_bound=9)
    flags.DEFINE_enum('exercise', None, ['a', 'b', 'c'], 'This is one of the command. Exercise mode.')
    sys.exit(app.run(main))