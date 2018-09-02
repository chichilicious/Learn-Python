import socket
import time

first
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #establish
mysock.connect(('data.pr4e.org',80)) #connect
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
mysock.sendall(b"GET http://data.pr43.org/cover3.jpg HTTP/1.0\r\n\r\n")
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) <1:
        break
    # print(data.decode(),end='')

    time.sleep(0.25)
    picture = picture + data
    # print(picture,data)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
    #print(picture)

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())
# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
print("------------")


#---------------------------------------------------------------------------------------------------

import urllib.request
count = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    # print(line.decode().strip())
    words = line.decode().strip()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
print("-----------------")


#-------------------------------------------------------------------------------------------------------
import urllib.request,urllib.parse,urllib.error
import re

# url = input("Enter url: ")
url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"',html)
for link in links:
    print(link.decode())
print("-----------------")


#-------------------------------------------------------------------------------------------------------
# from bs4 import BeautifulSoup
# import ssl

# ctx = ssl.create_default_context
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg','wb')
# fhand.write(img)
# fhand.close()
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size,'chars copied')
fhand.close()

import urllib.request
count = dict()
length = 0
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().strip()
    length = length + len(list(words))
    if length < 100:
        print(words)
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
print(length)
print("-----------------")
