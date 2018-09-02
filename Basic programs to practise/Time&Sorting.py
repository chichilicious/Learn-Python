#sorting
def is_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

a=[1,2,9,2]
b=['a','b','a']
print(is_sorted(a))
print(is_sorted(b))

#anagram
def is_anagram(a,b):
    if len(a) != len(b):
        return False
    else:
        x=list(a)
        y=list(b)
        x.sort()
        y.sort()
        if x == y:
            return True
        else:
            return False

c='spar'
d='rasb'
print(is_anagram(c,d))

def has_duplicates(a):
    a.sort()
    print(a)
    for i in range(len(a)-1):
        res=[]
        count=0
        if a[i] != a[i+1]:
            res.append(a[i])
            count=count+1
            print(count)
            count == len(a)
            return True
        return False

def is_duplicates(a_list):
    a_list.sort()
    for each in a_list:
        count = a_list.count(each)
        if count > 1:
            print("there are duplicates bruh")
            return True
    print("no duplicates")
    return False
            

f=[1,2,5,2,3,4,5]
g=[1,3,2,6,5,8]
print(is_duplicates(f))
print(is_duplicates(g))

def remove_duplicates(a_list):
    b_list = set(a_list)
    print(b_list)

print(remove_duplicates(f))
print(remove_duplicates(g))

""""Time operations""""

import time


def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print( len(t))
print( t[:10])
print( elapsed_time, 'seconds')


"""Binary search"""
from bisect import bisect_left
def make_word_list3():
    word_list=[]
    fin=open('words.txt')
    for line in fin:
        word=line.strip()
        word_list.append(word)
    return word_list

def in_bisect(word_list,word):
    i = bisect_left(word_list,word)
    if i!= len(word_list) and word_list[i] == word:
        return True
    else:
        return False

word_list=make_word_list3()
for word in ['hello', 'candies']:
        print(word, 'in list', in_bisect(word_list, word))



        
