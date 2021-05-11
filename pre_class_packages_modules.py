"""
import my_module  # we've loaded my_module

my_module.my_function()  # we've called a function defined in my_module

print(my_module.my_variable)  # we've accessed a variable defined in my_module

---------------------------------------
import my_module as mym # loads my_module, we give a nickname to it

mym.my_function()  # we can use it the same way

print(mym.my_variable) 
--------------------------------------
from my_module import my_function  # we've loaded only my_function from my_module

my_function()  # my_function can be used directly now at the current module

----------------------------------------
from my_module import my_function as mfnc # we've imported my_function named mfnc

mfnc()  # we use the my_function's alias directly

------------------------------------
import module_1
import module_2
import module_3

# The code stream of the current module starts here

------------------------------------
Q: What are python modules? Name some commonly used built-in modules in Python.
A: Python modules are files containing Python code. This code can either be functions classes or variables. 
A Python module is a .py file containing executable code. 
Some of the commonly used built-in modules are: os, sys, math, random, datetime. 

------------------------------------
Q: How can you generate random numbers in Python?
A: Random module is the standard module that is used to generate a random number. The method is defined as:

import random
print(random.random())
The statement "random.random()" method return the floating point number that is in the range of (0, 1).
The function generates random float numbers.  

"""
import math

print(dir(math))  # you can find out all names defined in this module


from math import pi, factorial, log10  # we'll use the functions directly

print(pi)  # it also contains several arithmetic constants
print(factorial(4))  # gives the value of 4!
print(log10(1000))  # prints the common logarithm of 1000

def factor(x):#factorial
    
    result = 1
    for i in range(x):
        result *= (i+1)
    return print(result)

factor(5)

import string as stg  # we've used alias for 'string' module

print(stg.punctuation)  # prints all available punctuation marks
print(stg.digits)  # prints all the digits


import datetime

print(datetime.date.today())  # prints today's date (yyyy-mm-dd)
print(datetime.datetime.now())  # prints the current time in microseconds

from random import choice

paths = ['AWS & DevOps Engineer', 'Java Dev', 'Web Dev', 'Data Science']
print(choice(paths)) 


""" this is my first module & script """

def my_func1(x):
    return print(x**2)

def my_func2(y):
    return print(*y)

if __name__ == '__main__':  # output-generating statements are here
    print('hello') 
    my_func1(3)
    my_func2("clarusway")
"""
earth/                          # Top-level package
      __init__.py               # Initialize the earth package
      asia/                     # Subpackage for file asia
              __init__.py
              japan.py
              mongolia.py       # A module under a subpackage
              pakistan.py
              taiwan.py
              ...
      europe/                   # Subpackage for file europe
              __init__.py
              germany.py        # A module under a subpackage
              england.py
              turkey.py
              kosovo.py
              ...
      america/                  # Subpackage for file america
              __init__.py
              canada.py
              ustates.py
              mexico.py
              peru.py           # A module under a subpackage

import earth.europe.kosovo  # importing with naming package, subpackage and module

earth.europe.kosovo.a_function()  # we want to access a function defined in kosovo module
-----------------------------------
from earth import europe.kosovo  # importing with naming subpackage and module

europe.kosovo.a_function()  # we want to access a function defined in kosovo module
---------------------------------
from earth.europe import kosovo  # importing without naming package and subpackage

kosovo.a_function()  # we want to access a function defined in kosovo module
-----------------------------
from earth.europe.kosovo import a_function  # importing without any naming

a_function()  # we use directly the function's name

****************************Don't forget:******************************************
For Python to recognize the folders you created as packages / subpackages, 
you need to create an empty file named __init__.py in both the package and subpackage folders.
They are usually empty, but may contain some initialization code of the package.
***********************************************************************************
Tips:
Note that when using from package import item, 
the item can be either a submodule (or subpackage) of the package, 
or some other name defined in the package, like a function, class or variable.
The import statement first tests whether the item is defined in the package; 
if not, it assumes it is a module and attempts to load it. 
If it fails to find it, an ImportError exception is raised.


Q: What is module and package in Python?
A: In Python, module is the way to structure the program. Each Python program file is a module, 
which imports other modules like objects and attributes. 
The folder of Python program is a package of modules. A package can have modules or subfolders.


from . import mongolia  # one dot means addressing to a current package/subpackage
 
from .. import europe  # two dots mean addressing to a parent package/subpackage
 
from ..europe import kosovo  # subpackage name comes immediately after two dots


----------------------------------
"""" this is my first module & script """"

def my_func1(x):
    return print(x**2)

def my_func2(y):
    return print(*y)

from ..asia import japan  # we've added importing syntax using two dots
japan.my_func1(6)         # and the name of parent subpackage (asia)

if __name__ == '__main__':
    print('hello') 
    my_func1(3)
    my_func2("clarusway")

-------------------------------------------------
Avoid:
Using the syntax from name import * is usually considered bad practice.
While working on Python codes, keep this in your mind : Readability counts!
-----------------------------------
Tips:
Absolute imports syntax are preferred, as they are usually more readable.
When dealing with very complex and sophisticated packages, it is preferable to use relative imports syntax, 
since using absolute imports will result in unnecessary redundancy.
"""







