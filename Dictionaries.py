"""DICTIONARIES"""

trial=dict()
# trial['one']='uno'
print(trial)
trial = {'two':'dos','three':'thres','four':'quathros'}
trial['one']='uno'
print(trial)
print(trial['one'])

#you need the kay for the in operator, the value wont work
def messing(trial):
    vals = trial.values()
    if 'one' in trial and 'thres' in vals:
        print("yayy")
    else:
        print("nay")

messing(trial)
print(len(trial))

fin = open('words.txt')
fin = dict()
vals=fin.values()
if 'candies' in vals:
    print("yayy")
else:
    print("nayy")

#dictionary
def histogram(s):
    d = dict()
    for letter in s:
        if letter not in d:
            d[letter] = 1 
        else:
            d[letter] += 1
    return d

def histogram_new(s):
    for letter in s:
        return s.get(letter)

h= histogram('shrisha')
print(h)   
x= h.get('x')
print(x)

def histogram_1(s):
    for key in s:
        print(key,s[key])

histogram_1(h)

def histogram_2(s):
    h = list(s)
    h.sort()
    print(h)

histogram_2(h)

# def reverse_look(d,v):
#     for k in d:
#         if d[k] == v:
#             print(k)
#     raise ValueError(k)
# reverse_look(h,2)

#inverse of dict
def inverse(d):
    inverse = dict()
    for key in d:
        val = d[key]
        print(val)
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print(inverse(h))

known={1:1,2:2,3:3,5:5}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(5))
