#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pathlib
import sys
from argparse import ArgumentParser

import pyigata

SCRIPT_FILE_PATH = pathlib.Path(os.path.abspath(__file__))


def get_logger(args):
    log_level = 0 if args.debug else args.log_level
    return pyigata.Common(log_level)


def test_func(args):
    logger = get_logger(args)
    message = f"testing in mode of {args.mode}"
    logger.info(f"{args.name} is {message}")
    logger.debug(f"{args.name} is {message} with debug mode")


def create_license_list(args):
    logger = get_logger(args)
    if args.target:
        logger.info(f"TARGET: {args.target}")
        logger.info(f"OUTPUT: {args.output}")
        creator = pyigata.LicenseListCreator(
            python_path=args.target, output_csv=args.output, log_level=args.log_level
        )
        creator()
    else:
        logger.error("Please input --target")
        logger.abort("Try --help to get a list of flags !!")


def main():
    common_parser = ArgumentParser(description="parse common options.", add_help=False)
    common_parser.add_argument(
        "-d", "--debug", action="store_true", default=False, help="Run debug mode."
    )
    common_parser.add_argument(
        "-l",
        "--log-level",
        type=int,
        default=1,
        metavar="NUM",
        choices=range(4),
        help="Specify log level as an integer number.",
    )

    main_parser = ArgumentParser(description="Sample command.")
    subparsers = main_parser.add_subparsers(help="sub-command help")

    # for test
    subparser_test = subparsers.add_parser("test", parents=[common_parser])
    subparser_test.add_argument(
        "-n", "--name", type=str, default="Yuki Yoshida", help="Your name."
    )
    subparser_test.add_argument(
        "-m",
        "--mode",
        type=int,
        default=0,
        choices=range(10),
        metavar="NUM",
        help="Specify test mode as an integer number.",
    )
    subparser_test.set_defaults(handler=test_func)

    # for license
    subparser_license = subparsers.add_parser("license", parents=[common_parser])
    subparser_license.add_argument(
        "-o",
        "--output",
        type=str,
        default="license_list.csv",
        help="Output license list file name.",
    )
    subparser_license.add_argument(
        "-t",
        "--target",
        type=str,
        default=None,
        metavar="PATH",
        help="Path to target python packages.",
    )
    subparser_license.set_defaults(handler=create_license_list)

    args = main_parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
