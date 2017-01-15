#coding=utf-8 
#! /usr/bin/env python 


"""
from modname import funcname 
from modname import fa, fb, fc 
or   from modname import * 
"""



import mingutil


"""
python能够改变变量作用域的代码段是def、class、lamda.
if/elif/else、try/except/finally、for/while 并不能涉及变量作用域的更改，也就是说他们的代码块中的变量，在外部也是可以访问的
变量搜索路径是：本地变量->全局变量
"""


def scopetest():  
    localvar=6;  
    print "in def scope localvar=",localvar
    
scopetest() 
#print(localvar) #if uncomment it will cause exception, fotr that it is in def scope, and it is local variables in def scope.
mingutil.compline("test def scope1")
 
"""
very important!!! if/elif/else、try/except/finally、for/while  is able to define global var! not like java!

"""
while True:  
    newvar=8  
    print "in exposed not in def while loop newvar=", newvar 
    break;  
  
print "not in def nor while loop newvar=", newvar 
mingutil.compline("test while scope ")

try:  
    newlocal=7  
    raise Exception  
except:  
    print "var defined in try and invoke in except, newlocal = ", newlocal #可以直接使用哦 

mingutil.compline("test try catch scope1")

"""
output would be 
5
6
5

local will search for local var first , so the in scopttest2, the var would call local var=6 as first priority, if not then search the global localvar list

"""
def scopetest2():  
    var=6;  
    print(var)#  
      
var=5   
print(var)  
scopetest2()  
print(var)   

mingutil.compline("test def local ")

"""
output would be 
5
6
6

use global keyword to set the var2 in def scopt as the global one
"""

def scopetest3():  
    global var2   
    var2=6;  
    print(var2)#  
      
var2=5   
print(var2)  
scopetest3()  
print(var2)  

mingutil.compline("test def global var ")




