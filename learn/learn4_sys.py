import sys

import __builtin__
from learn.mingutil import compline

from keyword import kwlist




print sys.path

print dir()
compline("dir()")

print dir('mingutil')
compline("dir('mingutil')")


print(kwlist)
compline("kwlist")

print help(__builtin__)
compline("__builtin__")