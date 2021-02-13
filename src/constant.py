# -*- coding: utf-8 -*-

class Constant(object):
    class ConstError(TypeError):
        pass

    def __init__(self, **args):
        for name, value in args.items():
            self.__dict__[name] = value

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(f'Cannot rebind constant ({name})')
        self.__dict__[name] = value
