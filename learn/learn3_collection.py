#coding=utf-8 
#! /usr/bin/env python 
from collections import deque
import time
import sys

from mingutil import compline


#init list
a = [1,2,3,4,5,6,7,8,9,10]
print a
compline("init")

#add obj will append to tail
a.append(11)
print a
compline("append")

#extend usage, a b will extend all elements from list a
b=[]
b.extend(a)
print b
compline("extend")

#insert with index
a.insert(0, 0)
print a
compline("insert")


#remove will only remove from  first one 
b.append(10)
print b
b.remove(10)
print b
compline("remove")

#pop will return and remove the idnex one , defalut pop will remove the last one 
print "b:",b
b.pop()
print "b:",b
b.pop(b.__len__()-1) #means pop the latest one of the index.
print "b:",b

compline("pop")


# return the first index of the value of the input one 
indexof5 = b.index(5)
print "indexof5:",indexof5, "of list b:", b
compline("index") 


#sort
b.sort(cmp=None, key=None, reverse=False)
print "b after b.sort(cmp=None, key=None, reverse=False):", b
b.sort(reverse=True)
print "b after b.sort(reverse=True):", b
compline("sort") 


#last in first out, use it as a stack
stack = [1,2,3]
stack.append("a")
print "after append stack:",stack
stack.pop()
print "after pop stack:",stack
print stack
compline("sort") 

def test_deque_vs_list(n=200000000):
    #performance test compared with the original deque.
    queue = deque(["Eric", "John", "Michael"]);
    
    startTS  = time.time();
    print startTS
    
    for i in range(n):
        queue.append("test")
        queue.popleft()
    endTS = time.time();
    print endTS
    dur1 = endTS - startTS;
    print str(n)+" operation deque FILO cost ms:", dur1*1000
    
    
    listsimqueue = ["Eric", "John", "Michael"]
    startTS  = time.time();
    print startTS
    for i in range(n):
        listsimqueue.append("test")
        listsimqueue.pop(0)
    endTS = time.time();
    print endTS
    dur2 = endTS - startTS;
    print str(n)+" operation list simmulate FILO cost ms:", dur2*1000
    print "in avg the FILO operation deque is ", "%.2f" % (100*(dur2- dur1)/dur1)+'%' , "faster than list append and pop index"

test_deque_vs_list(1000000)
"""
test 20m times
1484374272.98
1484374305.05
2000000000 operation deque FILO cost ms: 32063.0002022
1484374305.05
1484374351.1
2000000000 operation list simmulate FILO cost ms: 46053.9999008
in avg the FILO operation deque is  43.64% faster than list append and pop index
"""
compline("test_deque_vs_list") 




#filter , map and reduce usage
def f(x): return x % 2 != 0
filteredList = filter(f, range(10, 20))
print "filter(f, range(10, 20)) , return the <list of all the input values> that will make the f function return True:",filteredList


def cube(x): return x*x*x
cubeList = map(cube, range(1, 11))# range(1,11) measn  numbers>= 1 and < 11
print "map(cube, range(1, 3)) will return all the  <output values for the input values> of the function cube", cubeList

def multi_paramslist_map(x, y): return x+y
seq = range(8)
multimaplist = map(multi_paramslist_map, seq, seq)
print "map(multi_paramslist_map, seq, seq) will return all the  <output values for the input values> of the function multi_paramslist_map with two series of input values", multimaplist
compline("filter , map and reduce usage") 




#### list comprehension， 列表推导式 , 3 kind of equal format
squares = []
for x in range(10):
    squares.append(x**2)
    
squares1 = [x**2 for x in range(10)] #comprehension format
squares2 = map(lambda x:x**2,range(10))
print "squares calc by list ", squares, squares1,squares2


#notice the return for multiple params must be using tuples or list 
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print "original for in loop:", combs

tuplexy = [ [x, y] for x in [1,2,3] for y in [3,1,4] if x != y]
print "[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]:",tuplexy


# matrix transpose operarion
def matrix_transpose(matrix):
    '''
    transpose the x*y matrix to y*x
    '''
    columnsize = matrix[0].__len__()
    convertMatrix = [ [row[i] for row in matrix] for i in range(columnsize)]
    return convertMatrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print "matrix before transpose:", matrix

convertMatrix = matrix_transpose(matrix)
print "row column switched matrix by comprehension :",convertMatrix 


print "list(zip(*matrix))", zip(*matrix) #internal function zip(*matrix)


compline("list comprehension") 



# del
aa = [0,1,2,3,4,5,6,7,8,9]
print "aa:", aa
del aa[0]
print "after del aa[0]:", aa
del aa[2:4] #[2:4]  means from >=2 to <4, that is 2,3 without 4
print "after del aa[2:4]:", aa
del aa

try:
    print aa
except:
    print "after del aa, met exception", sys.exc_info()[0],sys.exc_info()[1] # sys.exc_info()[0] is Exception type, [1] is the details desc

compline("del") 
    
# tuples
t = 12345, 54321, 'hello!'
print "tuple t:", t
u = t, (1, 2, 3, 4, 5)
print "tuple u:", u

try:
    t[0] = 1
except:
    exMsg = sys.exc_info()[0]
    print "t[0] = 1 met exception", sys.exc_info()[0],sys.exc_info()[1] 


singleTuple  = "singletuple",
print singleTuple,len(singleTuple)

#unrwap , from tuple to var
t1,t2,t3 = t
print t1,t2,t3

compline("singleton tuple and unrwap tuple to vars") 


# set operation 
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana','apple','banana']
print "basket:",basket
basketset = set(basket)
print "basketset = set(basket):",basketset

#if pass in string , the set would treat the alphabet as the element!
alphaSetA = set('abracadabra')
alphaSetB = set('alacazam')
print "alphaSetA,alphaSetB:",alphaSetA,alphaSetB
print "alphaSetA - alphaSetB:", alphaSetA - alphaSetB # in A not in B
print "alphaSetB - alphaSetA:", alphaSetB - alphaSetA # in B not in A
print "alphaSetA | alphaSetB:", alphaSetA | alphaSetB # in either A or B
print "alphaSetA & alphaSetB:", alphaSetA & alphaSetB # in A and B 
print "alphaSetA ^ alphaSetB:", alphaSetA ^ alphaSetB # in A or B but not both
print " {x for x in 'abracadabra' if x not in 'abc'}:", {x for x in 'abracadabra' if x not in 'abc'}
compline("set") 


# dict, important is that the key set must be immutable, which means numbers and string are ok, but not list and object, for that list can be append() or pop() to change
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print "tel:", tel
del tel['sape']
print "tel after del tel['sape']:", tel
print "tel.keys():",tel.keys()

try:
    tel2 = {'jack': 4098, 'jack': 4099} # actuallly it is same as tel['jack'] = 4098; tel['jack'] = 4099, and it would be 4099 with jack as key at last
    print tel2
except:
    print "tel2 = {'jack': 4098, 'jack': 4099}", sys.exc_info()[0],sys.exc_info()[1] 
    

#use list of tuple or list of 2 element list is the same when use dict() to directly form a dict
print "dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]):", dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print "dict([['sape', 4139], ['guido', 4127], ['jack', 4098]]):",  dict([['sape', 4139], ['guido', 4127], ['jack', 4098]])

#dict comprehension
print"{x: x**2 for x in (2, 4, 6)}, dict comprehension:", {x: x**2 for x in (2, 4, 6)}

print "dict(sape=4139, guido=4127, jack=4098) directly assign for simple string to string :", dict(sape=4139, guido=4127, jack=4098)
compline("dict and dict comprehension")


#enumerate()  and loop dict.items , get the index and value
print "enumerate a list ['tic', 'tac', 'toe']:"
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

print "enumerate a dict dict(sape=4139, guido=4127, jack=4098):"
for i, v in enumerate( dict(sape=4139, guido=4127, jack=4098)  ):
    print  i, v

print "loop key in dict"
for k in dict(sape=4139, guido=4127, jack=4098):
    print(k)
print "loop k, v  in dict.items:"      
for k, v in dict(sape=4139, guido=4127, jack=4098).items():
    print(k,v)
        
print "use zip to loop two list at the same time for q, a in zip(questions, answers):"
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

print " use reversed to do reservsed sort for i in reversed(xrange(1, 10, 2)):"
for i in reversed(xrange(1, 10, 2)):
    print(i)

print " use sorted(set) to create a new list without affecting the original one "
print "basket :", basket
for f in sorted(set(basket)):
    print f

compline("enumerate and loop")


# deep in logic
print " <and> <or> is short circuit operator , like && and || in java"
print " 1>3 and 1<3 and 2<4",  1>3 and 1<3 and 2<4
print " 'aa' in locals().keys() and aa.__len__() > 0 ",  'aa' in locals().keys() and aa.__len__() > 0 # if not short circuit , the aa is del in previous and it will cause exception

#not have the highest priority
print " True and not False or 1==2:", True and not False or 1==2
print " True and (not False) or 1==2:", True and (not False) or 1==2


# print (cc=1) == 1 #SyntaxError: invalid syntax, it will be checked during compiling time not runtime

print (1, 2, 3)              < (1, 2, 4)
print [1, 2, 3]              < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)           < (1, 2, 4)
print (1, 2)                 < (1, 2, -1)
print (1, 2, 3)             == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)








