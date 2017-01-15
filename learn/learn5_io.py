#!/usr/bin/env python
# -*-coding:utf-8 -*-
import math
import pickle

from learn.mingutil import compline


#to make the code to be more compatible with 3 , use repr() and print() 
s = 'Hello, world.'

print 'str(s):',str(s)
print 'repr(s):',repr(s)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s
compline("dif between str and repr")


for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),repr(x*x*x).rjust(4)
    
    
for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
    
print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print 'We are the {1} who say "{0}!"'.format('knights', 'Ni')
print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible') #normally the format could use {num index} and {str key}
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

#{0:10}, 0 is index, 10 is the min width of the str
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
    
#pass in dict as k-v to match the format string
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

#old format way to use %
print 'The value of PI is approximately %5.3f.' % math.pi

compline("repr(x).rjust and string.format ")



'''
第一个参数是一个标识文件名的字符串。第二个参数是由有限的字母组成的字符串，描述了文件将会被如何使用。可选的 模式 有：
 'r' ，此选项使文件只读； 'w' ，此选项使文件只写（对于同名文件，该操作使原有文件被覆盖）； 'a' ，此选项以追加方式打开文件； 'r+' ，此选项以读写方式打开文件； 模式 参数是可选的。如果没有指定，默认为 'r' 模式。
'''
f = open('workfile', 'w')
f.write("line1\n")
f.write("line2")

print f.closed

f.close()# file must be close to use again

print f.closed

f2= open('workfile', 'r')
print f2.__sizeof__()
print f2.readlines() #list of lines
f2.close()

f3 = open('workfile', 'r')
fread = f3.read() #str
f3.close()
print fread

f = open('workfile', 'r')
for line in f:
    print line,f.tell()

f.close()

#the with **** as f  will close the f automatically 
with open('workfile', 'r') as f:
    read_data = f.read()
print f.closed

compline("open(file) and read write")



#pickle is a serialization and deserialization tool in python

class Foo:
    '''
    used for serialization test
    '''
    attr1 = 'a class attr1'
    attr2 = 'a class attr2'
    def __init__(self):
        print "init..."
        pass
    

fooObj =  Foo()

with open('foo', 'w') as f:
    pickle.dump(fooObj, f)
    

    
with open('foo', 'r') as f:
    x = pickle.load(f)
    print x.attr1
     
compline("pickle ser and de-ser")



