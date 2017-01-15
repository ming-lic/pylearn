#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Util module for learning python2.7
'''

__all__ = ['compline', 'fib', 'fib2']

def compline(name=None): 
    '''
    print test name with * enbraced and line cut 
    '''
    if name is not None:
        print("****************************************** "+name+" complete **********************************************\n")
    else:
        print("*****************************************************************************************************\n")
        
        
def fib(n):
    '''
    write Fibonacci series up to n
    '''   
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b


def fib2(n): # return Fibonacci series up to n
    '''
    return Fibonacci series up to n
    '''  
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


if __name__=="__main__":
    fib(100)
    compline("fib(100)")
    print(fib2(100))
    compline("fib2(100)")
    
    from learn import mingutil
    print help(mingutil)