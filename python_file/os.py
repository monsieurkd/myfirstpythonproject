import os


print(os.system('dir *Nháp.py'))
pipe=os.popen("dir *Nháp.py")
print (pipe.read())

#regular expression
import re
x = 'my 2 favourite numbers are 19 21 and 2200'
y = re.search('[0-9]+', x)
print(y)
# ? = not greedy ( lấy cái ngắn hơn)

#socket python 13/10 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()