import socket

#设置套接字的超时
s = socket.socket()
print(s.gettimeout())
s.settimeout(10)
print(s.gettimeout())