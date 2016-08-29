"""
Exercise questions from Think like a Computer Scientist
http://www.greenteapress.com/thinkpython/html/index.html

Exercises 3.1,3.2,3.3,3.4,3.5

"""
import random
import sys
import os
import math



a='letter a'
b='letter b'
print a+b
print 'zan'*3
#compute time
print(miles+2)/2
km=2
print(km*miles)
print(3.14*1/2)
width=17


"""exercise 3.3"""

def right_justify(s):
    print ' '*59+s

right_justify('allen')

"""exercise 3.4"""



def printtwice(spam):
    print spam
    print spam

def do_twice(f,arg):
    f(arg)
    f(arg)


def do_four(f,arg):
    do_twice(f,arg)
    do_twice(f,arg)

do_four(printtwice,'spam')

"""exercise 3.5"""

def plusline():
    print (('+ '+ '- '*4)*2)+'+'

def line():
    print ('|'+ ' '*9)*3

def set():
    line()
    line()
    line()
    line()

def two():
    plusline()
    set()


def printtwice(f):
    f()
    f()

def printgrid():
    printtwice(two)
    plusline()
printgrid()

