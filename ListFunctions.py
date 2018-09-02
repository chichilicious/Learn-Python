cheese=['cheddar',34, 5.6]
print([cheese])
cheese[2]='mozerella'

def cheesee():
    if 'mozerella' in cheese:
        return True

print(cheesee())

no1=[1,2,3,4]
no2=[4,5,6]

for i in range(len(no1)):
    no1[i] += 2
    i=i+1

print(no1)

print(no1+no2)
print(no1*2)
print(no1[1:3])
no1[1:3]=[5,4]
print(no1)

a=['bpple','at','dog','cat']
a.sort()
print(a)

b=[1,56,56.02,32]
b.sort()
print(b)

a.append('ele')
print(a)
a.extend(b)
print(a)

def add(b):
    total=0
    for x in b:
        total+=x
    return total

print(add(b))
print(sum(b))

c=[1,2,3,[4,5,6],[7,8,9]]
c[3]=sum(c[3])
c[4]=sum(c[4])
print(sum(c))

def capitalize_all(a):
    res=[]
    for s in a:
        res.append(s.capitalize())
    return res

print(capitalize_all(a[:5]))

d=capitalize_all(a[:5])
print(d)

def upper(a):
    res=[]
    for s in a:
        if s.isupper():
            res.append(s)
    return res

print(upper(d))

"""Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list."""

def cumulative_sum(c):
    i=0
    res=[c[i]]
    for x in c:
        while i<len(c)-1:
            add=c[i]+c[i+1]
            res.append(add)
            i=i+1
    return res

e=[1,3,5,7]
f=[3,4,5,6,77]
print(cumulative_sum(e))
print(cumulative_sum(f))

print(e.pop(3))
print(e)
# del f[3]
# print(f)
cheese.remove('cheddar')
print(cheese)

def middle(f):
    return(f[1:len(f)])

print(middle(f))

cheese1=list(cheese[1])
print(cheese1)

new=('If only i knew this before')
new1=new.split()
new2=new.split('knew')
print(new1)
print(new2)
new3=('yes','no','yes')
deli=' '
dells=deli.join(new1)
print(dells)
deli=''
dells1=deli.join(new3)
print(dells1)

a_list=[1,2,3]
b_list=a_list
def something(a,b):
    if a is b:
        return 'oh,yeaaaaah'
    else:
        return 'hehe,no'

print(something(a_list,b_list))

