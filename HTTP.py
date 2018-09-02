import socket
import time
import urllib.request

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if (len(data) < 1):
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data),count)
    picture = picture + data

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

files = urllib.request.urlopen()
for each in files:
    print(each.decode().strip())




