#!/usr/bin/env python
# -*-coding:utf-8 -*-
import sys
from learn.mingutil import compline

'''
Python 的一个特别之处在于——如果没有使用 global 语法——其赋值操作总是在最里层的作用域。赋值不会复制数据——只是将命名绑定到对象。
删除也是如此： del x 只是从局部作用域的命名空间中删除命名 x 。事实上，所有引入新命名的操作都作用于局部作用域。
特别是 import 语句和函数定将模块名或函数绑定于局部作用域。（可以使用 global 语句将变量引入到全局作用域。）
'''


class MyClass:
    """A simple example class"""
    i = 12345
    data = []
    def f(self):
        return 'hello world'
#     def __init__(self): the __init__ only have one, even they have different parameters
#         self.data = []
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
myc = MyClass(1,2)
print myc.f()
print myc.__doc__
print myc.r, myc.i

compline("class creation")

# 数据属性 相当于 Smalltalk 中的“实例变量”或 C++ 中的“数据成员”。 never like java. 
# 和局部变量一样，数据属性不需要声明，第一次使用时它们就会生成。例如，如果 x 是前面创建的 MyClass 实例，下面这段代码会打印出 16 而在堆栈中留下多余的东西:

myc.counter = 1
while myc.counter < 10:
    myc.counter = myc.counter * 2
print myc.counter
del myc.counter

print "different between 函数对象 and  方法对象",MyClass.f, myc.f


referInstMethod = myc.f
print referInstMethod()

compline("class function and instance method")


#code guide
#1.数据属性会覆盖同名的方法属性。 为了避免意外的名称冲突，这在大型程序中是极难发现的 Bug，使用一些约定来减少冲突的机会是明智的。
# 可能的约定包括：大写方法名称的首字母，使用一个唯一的小字符串（也许只是一个下划线）作为数据属性名称的前缀，或者方法使用动词而数据属性使用名词。

#2.数据属性可以被方法引用，也可以由一个对象的普通用户（客户）使用。 换句话说，类不能用来实现纯净的数据类型。 事实上，Python 中不可能强制隐藏数据——一切基于约定。
# （如果需要，使用 C 编写的 Python 实现可以完全隐藏实现细节并控制对象的访问。这可以用来通过 C 语言扩展 Python。）

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
cc = C()
print cc.g(),cc.h(),cc.g, cc.h #hello world hello world <bound method C.g of <__main__.C instance at 0x02A45328>> <bound method C.g of <__main__.C instance at 0x02A45328>>
compline("reference to class member method")




class C2(C):
    pass
cc2 = C2()
print cc2.g(),cc.g(), cc2.g,cc.g# cc2 and cc's same method is not the same method instance
def newg():
    return 'goodbye world'
cc2.g = newg
print cc2.g(),cc.g()

class C3(C):
    def g(self):
        return 'hello world new'

cc3 = C3();
print cc3.g()

print cc.f,cc2.f,cc3.f #event the f() is out of the class, the method instance is still diff between the 3 inherited classes
print cc.f(1,2), cc2.f(1,2), cc3.f(1,2) # they all have the same method instance

compline("extend class")


class T1:
    def m1(self):
        return "m1 call"

class T2:
    def m1(self):
        return "redefined m1 call"
    def m2(self):
        return "m2 call"

class T3:
    def m3(self):
        return "m3 call"



#为了防止重复访问基类，通过动态的线性化算法，每个类都按从左到右的顺序特别指定了顺序，每个祖先类只调用一次，这是单调的（意味着一个类被继承时不会影响它祖先的次序）。
class MultiExtendT(T1,T2,T3):
    pass

t =  MultiExtendT();
print t.m1(), t.m2(),t.m3()
compline("multi extend class, left to right order ")



compline("private member in python")
    


   
