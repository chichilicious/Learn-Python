import re

#first
hand = open('mbox-short.txt')
i = 0
for each in hand:
    line = each.rstrip()
    # if re.search('From:',line): #use ^ to mention starting or first word, use '..' for inbetween
    # if re.search('^From:',line):
    # if re.search('^F..m:',line):
    if re.search('^F..m:.+za',line): #use :.+ to include another word
        i =  i+1
        print(line)
print(i)
        
#second
s = 'say hi to shrisha@ladywithadarkide.com from mailme@desginedbyashw.in @10pm and $$fckme'
lst = re.findall('\S+@+lady\S+',s)
mst = re.findall('\$[a-z.]+',s) # (+,o/p) --> $fckme; (*,o/p) --> ['$','$fckme'] - ESCAPE CHARACTER
print(mst)
print(lst)

#third
ahand = open('mbox-short.txt')
for each in ahand:
    #print("THIS IS EACH",each)
    line = each.rstrip()
    #print(line)
    # new = re.findall('\S+@\S+berkeley\S+',line) #whatever you type after @, it should follow that word
    # new = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    # new = re.findall('^X\S*: [0-9.]+',line)
    # new = re.findall('^X\S*: ([0-9.]+)',line) #add parenthesis when you want only part of it
    # new = re.findall('^Details:.*rev=([0-9.]+)',line)
    new = re.findall('^From .* ([0-9][0-9]):',line)
    
    if len(new) > 0:
        print(new)

v = 'New Revision: 39772999'
cst = re.findall('^New.+ ([0-9.]+)',v)
print(cst)