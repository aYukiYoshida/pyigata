# -*- coding: utf-8 -*-

import sys
import os
import pkg_resources
from typing import List, Union
from collections import deque
from enum import Enum 

import pandas as pd

from .common import Common
from .object import ObjectLikeDict


class CreatorType(Enum):
    DEFAULT = 'default'
    LIST = 'list'


class CreatorFactory:
    @classmethod
    def get_instance(cls, creator_type:str='default', loglv:Union[int, str]=1, **args):
        try:
            creator_type = CreatorType(creator_type)
            if creator_type in [ CreatorType.DEFAULT, CreatorType.LIST ]:
                return LicenseListCreator(loglv,**args)
        except ValueError:
            raise NotImplementedError(f'type of {creator_type.value} is not implemented !!')


class LicenseListCreator(Common):
    INFO_LABEL = [ 'name', 'version', 'license', 'hogepage' ]

    def __init__(self,loglv: Union[int, str], **args) -> None:
        super().__init__(loglv)
        python_path = args.get('python_path')
        self.python_path:List[str] = python_path if isinstance(python_path,list) else [ python_path ]
        self.output_csv:str = args.get('output_csv', 'license_list.csv')
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
        self.infomation = deque(
            ObjectLikeDict(zip(
                self.INFO_LABEL,
                [ pkg.key, pkg.version, self.__get_pkg_license(pkg), self.__get_pkg_home_page(pkg) ]))
                for pkg in sorted(working_set, key=lambda x: str(x).lower()))

    def create(self) -> None:
        info_table = pd.DataFrame(dict(zip(
            self.INFO_LABEL,
            [[ info[label] for info in self.infomation ] for label in self.INFO_LABEL])))
        info_table.to_csv(self.output_csv, index=False)
        self.info(f'{self.output_csv} is created !!')