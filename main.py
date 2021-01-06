#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys

import src
from absl import app
from absl import flags


def main(argv):
    if flag_values.debug:
        flag_values.log_level = 0
    logger = src.common.Common(flag_values.log_level)

    command_flags_list = [ flag_values.license, flag_values.test ]
    if len([ command_flag for command_flag in command_flags_list if command_flag is not None]) == 1:
        if flag_values.license:
            if flag_values.target:
                logger.info(f'TARGET: {flag_values.target}')
                logger.info(f'OUTPUT: {flag_values.output}')
                creator = src.license.CreatorFactory.get_instance(
                    creator_type=flag_values.license,
                    python_path=flag_values.target,
                    output_csv=flag_values.output,
                    log_level=flag_values.log_level)
                creator.create()
            else:
                logger.error('Please input --target')
                logger.abort('Try --help to get a list of flags !!')
        elif flag_values.test is not None:
            message = f'testing in mode of {flag_values.test}'
            logger.info(f'{flag_values.name} is {message}')
            logger.debug(f'{flag_values.name} is {message} with debug mode')
    else:
        logger.error('Please input command !!')
        logger.abort('Try --help to get a list of flags !!')


def define_flags():
    flag_values = flags.FLAGS
    flags.DEFINE_boolean(
        'debug', False, 'run with debug mode.')
    flags.DEFINE_enum(
        'log_level', 'INFO',
        ['DEBUG', 'debug', 'INFO', 'info', 'WARNING', 'warning', 'ERROR', 'error'],
        'Logging level.')
    flags.DEFINE_string(
        'name', 'Yuki Yoshida', 'Your name.')
    flags.DEFINE_integer(
        'test', None, 'This is one of the command. Test mode.', lower_bound=0, upper_bound=9)
    flags.DEFINE_enum(
        'license', None,
        [ t.value for t in src.license.CreatorType ],
        'This is one of the command. License check mode.')
    flags.DEFINE_string(
        'target', None, 'Path to target python packages')
    flags.DEFINE_string(
        'output', 'license_list.csv', 'Output file name')
    return flag_values


if __name__ == '__main__':
    flag_values = define_flags()
    sys.exit(app.run(main))