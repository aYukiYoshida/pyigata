# -*- coding: utf-8 -*-

import csv
import os
import sys
from collections import deque
from enum import Enum
from typing import List, Union

import pkg_resources

from .common import Common
from .extend import ExtendDict


class LicenseListCreator(Common):
    INFO_LABEL = ["name", "version", "license", "homepage"]

    def __init__(
        self, python_path: Union[str, List[str]], output_csv: str, log_level: int
    ) -> None:
        super().__init__(log_level)
        python_path = python_path
        self.python_path: List[str] = (
            python_path if isinstance(python_path, list) else [python_path]
        )
        self.output_csv = output_csv

    def __call__(self) -> None:
        self.fetch()
        self.create()

    @staticmethod
    def __get_pkg_license(pkg):
        try:
            lines = pkg.get_metadata_lines("METADATA")
        except BaseException:
            lines = pkg.get_metadata_lines("PKG-INFO")

        license_ = "UNKNOWN"
        labels = ["License: ", "Classifier: License :: OSI Approved :: "]
        for label in labels:
            for line in lines:
                if line.startswith(label):
                    license_ = line[len(label):]
                    break
        return license_

    @staticmethod
    def __get_pkg_home_page(pkg):
        try:
            lines = pkg.get_metadata_lines("METADATA")
        except BaseException:
            lines = pkg.get_metadata_lines("PKG-INFO")
        label = "Home-page: "
        for line in lines:
            if line.startswith(label):
                url = line[len(label):]
                break
        else:
            url = None
        return url

    def fetch(self) -> None:
        for path in self.python_path:
            if not os.path.exists(path):
                self.warning("Following file or directory is not found:")
                self.warning(f"  {path}")

        working_set = pkg_resources.WorkingSet(self.python_path)
        self.information = deque(
            ExtendDict(
                zip(
                    self.INFO_LABEL,
                    [
                        pkg.key,
                        pkg.version,
                        self.__get_pkg_license(pkg),
                        self.__get_pkg_home_page(pkg),
                    ],
                )
            )
            for pkg in sorted(working_set, key=lambda x: str(x).lower())
        )

    def create(self) -> None:
        with open(self.output_csv, "w") as f:
            writer = csv.DictWriter(f, self.INFO_LABEL)
            writer.writeheader()
            for info in self.information:
                writer.writerow(info)
        self.info(f"{self.output_csv} is created !!")
