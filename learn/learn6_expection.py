#!/usr/bin/env python
# -*-coding:utf-8 -*-
import sys
#invalud syntas when compile
#while True print 'Hello world'


#exception in python means runtime exception in java
while True:
    try:
#         x = int(raw_input("Please enter a number: "))
        x = int('a')
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
        break
    
    
try:
    raise IndexError
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except: # goes here for that none of the above exception match the exception 
    print "Unexpected error:", sys.exc_info()[0]

for arg in ['/tmp/fakefile',]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else: # if no exception caught, goes here
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
        
        
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)    # the exception instance
    print inst.args     # arguments stored in .args
    print inst          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print 'x =', x
    print 'y =', y
    
    
#define ERROR

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value
    print 'My exception occurred, value:', e  #__str__ is like the toString() in java object
    
    
#format of define Error 
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        
#first the except clause then the finally as literally means 
try:
    raise KeyboardInterrupt
except KeyboardInterrupt as e:
    print "caught exception", e
finally:
    print 'Goodbye, world!'
    
    
