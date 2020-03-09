#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys

import src
from absl import app
from absl import flags


###-----------------------------------------------------------------------
### to parse arguments
###-----------------------------------------------------------------------
flag_values = flags.FLAGS
flags.DEFINE_boolean('debug', False, 'run with debug mode.')
flags.DEFINE_integer('loglv', 1, 'Logging level.', lower_bound=0, upper_bound=3)
flags.DEFINE_string('name', 'Yuki Yoshida', 'Your name.')
flags.DEFINE_enum('practice', None, ['a', 'b', 'c'], 'This is one of the command. Practice mode.')
flags.DEFINE_enum('test', None, ['a', 'b', 'c'], 'This is one of the command. Test mode.')
flags.DEFINE_enum('exercise', None, ['a', 'b', 'c'], 'This is one of the command. Exercise mode.')


###-----------------------------------------------------------------------
def main(argv):
###-----------------------------------------------------------------------
    if flag_values.debug:
        flag_values.loglv = 0
    common = src.util.Common(flag_values.loglv)

    command_flags_list = [ flag_values.practice, flag_values.test, flag_values.exercise ]
    if len([ command_flag for command_flag in command_flags_list if command_flag is not None]) == 1:
        if flag_values.practice:
            message = 'practicing in mode of {0}'.format(flag_values.practice)
        elif flag_values.test:
            message = 'testing in mode of {0}'.format(flag_values.test)
        elif flag_values.exercise:
            message = 'exercising in mode of {0}'.format(flag_values.exercise)
        common.logger('{0} is {1}'.format(flag_values.name,message),1)
        common.logger('{0} is {1} with debug mode'.format(flag_values.name,message),0)
    else:
        common.logger('Please input command !!',3)
        common.abort('Try --help to get a list of flags !!')


###-----------------------------------------------------------------------
if __name__ == '__main__':
###-----------------------------------------------------------------------
    sys.exit(app.run(main))