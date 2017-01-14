#coding=utf-8 
#! /usr/bin/env python 

# pyexcel_xls �� OrderedDict �ṹ�������� 
from collections import OrderedDict 

 # write Fibonacci series up to n
def fib(n):   
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        #print a,  # ����ֻ��Ϊ�˴�ӡ�����У�PY �﷨
        result.append(a)
        a,b=b, a+b
    return result
       
fib_r = fib(100)
print "0-100 fib array:",fib_r

#Ĭ��ֵ�ں��� ���� �����򱻽���, �����Ǻ�JAVA��ͬ
#��Ҫ����: Ĭ��ֵֻ����ֵһ�Ρ���ʹ�õ�Ĭ��ֵ�ǿɱ����ʱ��������ͬ�������б��ֵ���ߴ�������ʵ�������磬����ĺ����ں������ù����л��ۻ���ǰ�棩�������Ĳ���:
def f(a, L=[]):
    L.append(a)
    return L

print f(1 )
print f(2 )
print f(3 )

#����������˵���������Ҫ����״̬���������µ�Ĭ��NONEȻ��ֵ�İ취��
def f2(a, L= None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1 )
print f2(2 )
print f2(3 )

#��������ͨ���ƶ�KEYWORD=VALUE�ķ�ʽ���ã��ܷ���
def parrot(voltage, state= 'a stiff', action=' voom', type= 'Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    print "*****************************************************************************"

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action= 'VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage= 1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump' )         # 3 positional arguments
parrot('a thousand', state= 'pushing up the daisies')  # 1 positional, 1 keyword


"""
  *name list must be before  **keywords dict like input
"""
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
       
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper= 'Michael Palin',
           client= "John Cleese",
           sketch= "Cheese Shop Sketch")


#test the is not and not in if 
def test_if_not():
    if "x" not in locals().keys():
        print "x is not defined in locals"
    x = 100
    if "x"  in locals().keys():
        print "x is defined now x=", x

test_if_not()

#lamda expression, here we will return the lamda exp as a var, so need to assign it to a var then use it.
def make_incrementor(n):
    if "x" not in locals().keys():
        x = 100
    return lambda x: x + n
lam = make_incrementor(10)
 
print " lamda test1:",lam(1)
print " lamda test1:",lam(2)

# promt is force param, retries and complaint is optional and has defalt values
def ask_ok(prompt, autoExit=True, retries=4, complaint='Yes or no, please!'):
    if autoExit:
        print "system exit"
        return True
    else:
        while True:
            ok = raw_input(prompt)
            if ok in ('y', ' ye', 'yes'):
                print "system exit"
                return True
            if ok in ('n', 'no' , 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise IOError('refusenik user')
            print complaint
        
   
       
ask_ok('Do you really want to quit?')
