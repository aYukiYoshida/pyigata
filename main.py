#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os
import pathlib
import sys
from argparse import ArgumentParser

import src

SCRIPT_FILE_PATH = pathlib.Path(os.path.abspath(__file__))

def main(argv):
    if argv.debug:
        argv.log_level = 0
    logger = src.common.Common(argv.log_level)

    if argv.command == 'license':
        if argv.target:
            logger.info(f'TARGET: {argv.target}')
            logger.info(f'OUTPUT: {argv.output}')
            creator = src.LicenseListCreator(
                python_path=argv.target,
                output_csv=argv.output,
                log_level=argv.log_level)
            creator()
        else:
            logger.error('Please input --target')
            logger.abort('Try --help to get a list of flags !!')
    elif argv.command == 'test':
        message = f'testing in mode of {argv.test_mode}'
        logger.info(f'{argv.name} is {message}')
        logger.debug(f'{argv.name} is {message} with debug mode')
    else:
        logger.error('Invalid command !!')
        logger.abort('Try --help to get a list of flags !!')


def define_flags():
    parser = ArgumentParser()
    parser.add_argument('command', type=str,
        choices=['test', 'license'], metavar='CMD', default=None, help='Command')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
        help='Run debug mode.')
    parser.add_argument('-l', '--log-level', type=int, default=1, metavar='NUM',
        choices=range(4), help='Specify log level as an integer number.')
    parser.add_argument('-n', '--name', type=str, default='Yuki Yoshida',
        help='Your name.')
    parser.add_argument('-o', '--output', type=str, default='license_list.csv',
        help='Output licence list file name.')
    parser.add_argument('-t', '--target', type=str, default=None,
        metavar='PATH', help='Path to target python packages.')
    parser.add_argument('--test-mode', type=str, default=0, choices=range(9),
        metavar='NUM', help='Specify test mode as an integer number.')
    return parser.parse_args()

if __name__ == '__main__':
    args = define_flags()
    sys.exit(main(args))