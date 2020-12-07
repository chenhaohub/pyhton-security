import socket

s = socket.socket()
r = s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
print(r)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#r默认是0设置为1后这个套接字就可以重复使用
print(s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR))