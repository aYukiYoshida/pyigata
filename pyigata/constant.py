# -*- coding: utf-8 -*-


class Constant(object):
    class ConstError(TypeError):
        pass

    def __init__(self, **args):
        for name, value in args.items():
            self.__dict__[name] = value

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(f"Cannot rebind constant ({name})")
        self.__dict__[name] = value


class ConstantMeta(type):
    def __init__(cls):
        pass

    def __setattr__(cls, name, value):
        if name in cls.__dict__:
            raise TypeError(f"Cannot rebind constant ({name})")
        else:
            cls.__setattr__(name, value)
