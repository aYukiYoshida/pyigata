# -*- coding: utf-8 -*-

import sys
import os
import pkg_resources
from typing import List, Union
from collections import deque
from enum import Enum 
import csv

from .common import Common
from .extend import ExtendDict


class CreatorType(Enum):
    DEFAULT = 'default'
    LIST = 'list'


class CreatorFactory:
    @classmethod
    def get_instance(cls, creator_type:str='default', log_level:Union[int, str]=1, **args):
        try:
            creator_type = CreatorType(creator_type)
            if creator_type in [ CreatorType.DEFAULT, CreatorType.LIST ]:
                return LicenseListCreator(log_level,**args)
        except ValueError:
            raise NotImplementedError(f'type of {creator_type.value} is not implemented !!')


class LicenseListCreator(Common):
    INFO_LABEL = [ 'name', 'version', 'license', 'homepage' ]

    def __init__(self,log_level: Union[int, str], **args) -> None:
        super().__init__(log_level)
        python_path = args.get('python_path')
        self.python_path:List[str] = python_path if isinstance(python_path,list) else [ python_path ]
        self.output_csv:str = args.get('output_csv', os.path.join('out', 'license_list.csv'))
        self.fetch()

    @staticmethod
    def __get_pkg_license(pkg):
        try:
            lines = pkg.get_metadata_lines('METADATA')
        except:
            lines = pkg.get_metadata_lines('PKG-INFO')

        license = 'UNKNOWN'
        labels = ['License: ', 'Classifier: License :: OSI Approved :: ']
        for label in labels:
            for line in lines:
                if line.startswith(label):
                    license = line[len(label):]
                    break 
        return license

    @staticmethod
    def __get_pkg_home_page(pkg):
        try:
            lines = pkg.get_metadata_lines('METADATA')
        except:
            lines = pkg.get_metadata_lines('PKG-INFO')
        label = 'Home-page: '
        for line in lines:
            if line.startswith(label):
                url = line[len(label):]
                break
        return url

    def fetch(self) -> None:
        for path in self.python_path:
            if not os.path.exists(path):
                self.warning('Following file or directory is not found:')
                self.warning(f'  {path}')

        working_set = pkg_resources.WorkingSet(self.python_path)
        self.information = deque(
            ExtendDict(zip(
                self.INFO_LABEL,
                [ pkg.key, pkg.version, self.__get_pkg_license(pkg), self.__get_pkg_home_page(pkg) ]))
                for pkg in sorted(working_set, key=lambda x: str(x).lower()))

    def create(self) -> None:
        with open(self.output_csv, 'w') as f:
            writer = csv.DictWriter(f, self.INFO_LABEL)
            writer.writeheader()
            for info in self.information:
                writer.writerow(info)
        self.info(f'{self.output_csv} is created !!')