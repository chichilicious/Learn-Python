#while
def test(n):
    while n>=0:
        print(n)
        n=n-1
        print("Hey again:%d"%(n))

test(5)

#sequence
def sequence(n):
    while n!=8:
        print(n),
        if n%2==0:
            n=n/2
        else:
            n=n*3+1

sequence(3)

#strings
def stringss(lmn):
    fruit = lmn
    length = len(fruit)
    print(length)
    first_letter = fruit[0]
    print(first_letter)
    last_letter = fruit[length-1]
    print(last_letter)
    print('Printing forwards')
    index=0
    while index<length:
            letter = fruit[index]
            print(letter)
            index=index+1
    print('Backwards')
    # index1=length
    while length>0:
        letter1 = fruit[length-1]
        print(letter1)
        length = length - 1
    #slice
    print(fruit[:3])
    print(fruit[4:])
    print(fruit[3:7])
    print(fruit[:])

    #changes
    new_fruit= 'M'+fruit[1:]
    print(new_fruit)
    new_fruit1= 'u'+ new_fruit[2:]
    print(new_fruit1)
    new_fruit2= 's'+ new_fruit1[3:]
    print(new_fruit2)
    new_fruit3= 'k'+ new_fruit2[4:]
    print(new_fruit3)

    #search
def find(word,letter):
    index = 0
    while index < len(word):
        if word[index]==letter:
            return index
        else:
            index = index + 1
    return -1

def number_of_letters(word,x):
    count=0
    for letter in word:
        if letter == x:
            count=count+1
    print(count)

stringss("watermelon")
find('hello',1)
number_of_letters('bananaNanana','n')

def diffmethods(word,x,n):
    new_uppercase = word.upper()
    print(new_uppercase)
    new_find = word.find(x,n)
    print(new_find)

diffmethods('shrishalovespy','s',5)
diffmethods('shrishashasha','sha',6)

def in_word(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)
    
    if word1 < word2:
        print(word1,word2)
    else:
        print(word2,word1)

in_word('apples','bananas')

def if_reverse(word1,word2):
    if len(word1) == len(word2):
        i=0
        j=len(word2)-1
        while j>0:
            if word1[i] != word2[j]:
                print(False)
                return False
                i=i+1
                j=j-1
            else:
                print(True)
                return True
    else:
        print("words are not equal")

if_reverse('qwerty','ytreqw')

import string


def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res



print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
print(rotate_word('sleep', 9))

def operators_strings(word1,word2,word3,word4):
    words=word1,word2,word3,word4
    words.sort()
    for word in words():
        print(word)
operators_strings('apple','cat','bat','dog')

convergence
def sequence(n):
    # print(n)
    while n!=0:
        # print(n),
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
    print(n)

for n in range(10**5):
    sequence(n)
    

    
