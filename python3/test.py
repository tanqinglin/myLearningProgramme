import os
from posixpath import split
from typing import Iterable
print(x.find('t') for x in os.listdir('.'))
s = ['sdugfgufvbe', 'sioadghgdeb']
print(list(x.find('deb') for x in s))

L = ['Hello', 'World', 'IBM', 'Apple'] # 将元素改为首字母大写，其他字母小写
L = [l[0].upper() + l[1:].lower() for l in L]
print(L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l, str)]
print(L2)

from email import generator


t = (x for x in range(1,11))
print(t)
print(isinstance(t, tuple))
print(next(t), next(t))

def triangles():
    L = [1]
    yield(L)
    while True:
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]
        yield(L)

from collections.abc import Iterable
print(isinstance(L, Iterable))

def s(x):
    return x**2


name = ['adam', 'LISA', 'barT']
def norm(s):
    return s[0].upper()+s[1:].lower()
print(list(map(norm, name)))

from functools import reduce

def str2float(s):
    
    pro = {'1': 1, '2': 2, '3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def f1(c):
        return pro[c]

    def f2(a=0, b=0):
        return a * 10 + b

    def f3(a=0, b=0):
        return a / 10 + b

    s1, s2 = s.split('.')
    val_1 = reduce(f2, map(f1, s1))
    val_2 = reduce(f3, list(map(f1, s2))[::-1]) / 10
    return val_1 + val_2

def is_palindrome(n):
    return str(n)==str(n)[::-1]

def createCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# 装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__ )
        return func(*args, **kw)
    return wrapper

@log
def now(x):
    print('2022-08-03')
    x += 1

now = log(now)
now(1)

#--------------------------------------------------
class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(getattr(s, 'age', 404))
#--------------------------------------------------

# -*- conding: utf-8 -*-

class Screen(object):
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '561-44556'))