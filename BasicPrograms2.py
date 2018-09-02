nums = [12,23,45,66,76,54]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
avg = sum(nums)/len(nums)
print(avg)

#printing avg of number
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count
    print('Average:', average)


#printing avg using lists
mylist = list()
while(True):
    a = 'done'
    inp = input("Enter a no.:")
    if inp == a :
        print(max(mylist))
        print(min(mylist))
    else:
        value = float(inp)
        mylist.append(value)
        avg = sum(mylist)/len(mylist)
        print('Avg:',avg)


s=('I am never forgetting this in my life')
make_list = list(s)
split_words = s.split()
print(make_list)
print(split_words[2:4])

a = ("My cgpa: 7.86")
delimiter = ':'
b = a.split(delimiter)
cgpa = b[1]
print(cgpa)

words = ['pple','pricot','lmonds','shwin','noosha','bhi']
for each in words:
    add = 'a' + each
    print(add)

def join(words):
    delimiter = ':'
    print(delimiter.join(words))

join(words)

def date(mailbox):
    count = 0
    for each_line in mailbox:
        line = each_line.rstrip()
        if not each_line.startswith('From '): continue
        words= each_line.split()
        print(words[1])
        count = count + 1
    print(count)
        

mailbox = open('mbox-short.txt')
date(mailbox)

def first_last_middle(t):
    del t[0]
    del t[len(t)-1]
    print(words)

first_last_middle(words)


#ROMEO
romeo = open('romeo.txt')

def read_romeo(t):
    final_list = list()
    for each_line in t:
        #print(each_line)
        x = str(each_line)
        #print(x)
        y = x.split()
        #print(y)
        for each_word in y:
            if each_word not in final_list:
                final_list.append(each_word)
        

    final_list.sort()
    print(final_list)

read_romeo(romeo)

mailbox = open('mbox-short.txt')
def email(mailbox):
    for each_line in mailbox:
        line = each_line.rstrip()
        # print(each_line)
        words = each_line.split()
        if len(each_line) == 0 and words[0] != 'From ': continue
        # print(words[0])

email(mailbox)

print("Hello\nworld")

mailbox = open('mbox-short.txt')
count = 0
for line in mailbox:
    count = count + 1
print('Line Count:', count)

romeo = open('romeo.txt')
inp = romeo.read()
print(len(inp))
print(inp)

mailbox = open('mbox-short.txt')
for line in mailbox:
    if not line.startswith('From '): continue
    if line.find('@media.berkeley.edu ')==-1: continue
    line = line.rstrip()
    print(line)

mailbox = open('mbox-short.txt')
for line in mailbox:
    if not line.startswith('From '): continue
    line1 = line.rstrip()
    line2 = str(line1)
    print(line2.upper())

mailbox = open('mbox-short.txt')
mylist1 = list()
for line1 in mailbox:
    if not line1.startswith('X-DSPAM-Confidence:'): continue
    line = line1.rstrip()
    new = str(line)
    delimiter=':'
    new1 = new.split(delimiter)
    mylist1.append(new1[1])
    
print(mylist1)

fruit = 'strawberry'
i = len(fruit) -1
print(i)
while i>=0:
    print(fruit[i])
    i = i-1


a='karnataka'
b='abcdefghijklmnopqrstuvwxyz'
def count(a,b):
    list_a=list(a)
    list_b=list(b)
    for each in list_b:
        if each in list_a:
            z=list_a.count(each)
            print(each,z)
        else:
            print(each,0)

count(a,b)

a=['a','q','j','b','i','o']
def bubblesort(a):
    for each in range(len(a)-1):
        for i in range(each):
            if a[i] >= a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

bubblesort(a)
print(a)

class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval


        