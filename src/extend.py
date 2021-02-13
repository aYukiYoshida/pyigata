# -*- coding: utf-8 -*-

class ExtendDict(dict):
    def __getattr__(self, name):
        return self.get(name)
