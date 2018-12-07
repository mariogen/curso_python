#!/usr/bin/env python3

import time

# def isstr(obj):
#     return

# def strings(obj, many=(list,tuple), string=(type(''))):
#     return isinstance(obj, many) or hasattr(obj, '__iter__')


class Person(object):

    def __init__(self, name, birth):

        if isinstance(name, _many):
            name = list(name)

        elif isinstance(name, str) and ',' in name:
            name = ' '.join(name.split(',')[::-1])

        (self.fname,
        *self.mnames,
         self.lname) = name.split()

        self.birth = birth


