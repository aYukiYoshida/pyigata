# -*- coding: utf-8 -*- 

import logging
import os
import sys

import sample


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    helper = sample.Help(sys.argv)
    loglv,test_flg = helper.parser()

    if test_flg:
        sys.exit(sample.pkg_name(helper))
    else:
        helper.abort('Please input command !!')
