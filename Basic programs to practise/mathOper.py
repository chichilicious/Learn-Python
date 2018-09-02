r=5
volume=(3/4)*3.14*r**3
print("Volume of sphere is %f"%(volume))

import math
height=math.sin(r)
print("height is %f"%(height))
sqaure_root=math.sqrt(r)
print("Square root is %f"%(sqaure_root))    
x=math.exp(math.log(r+1))
print("Expoent is %f"%(x))

#def is a function object i.e a definition of the function object namely                
def song_lyrics():
    print("Hey i'm shrisha")
    print("I'm learning python")

def repeat():
    song_lyrics()
    song_lyrics()

repeat()


def repeat_words(a,b):
    print(a,b)
    print(b,a)

repeat_words('hello  '*5,6)
repeat_words(math.cos(0),6)
s="Learning py"
repeat_words(s,6)

def cat_noises(c,d):
    cat=c+d
    cad=d+c
    repeat_words(cat,cad)

cat_noises('Meow','Meowww')

#from module import everything(*)
from math import *
print(pi)
print(cos(pi))
print(log(pi))

#string should be in coloumn 70
def right_justify(s):
    with_spaces="                               " + s
    print(with_spaces)

right_justify("alice")
right_justify("Bob")

def fun_inside_fun(f,m):
    f(m)
    f(m)

def print_twice(z):
    print(z)
    print(z)

fun_inside_fun(print_twice,'3b')

def print_four(f,n):
    fun_inside_fun(f,n)
    fun_inside_fun(f,n)

print_four(print_twice,'hello')

#design
def horizontal_line():
    d="+ - - - - + - - - - +"
    #f="+"
    #line=f + d + f + d + f
    print(d)

def vertical_line():
    g= "|"
    h= g + "         " + g + "         " + g
    print(h)
    print(h)
    print(h)
    print(h)
    
def two_rows():
    vertical_line()
    horizontal_line()

horizontal_line()
two_rows()
two_rows()  
