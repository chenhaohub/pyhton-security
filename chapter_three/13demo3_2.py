import socket

data = 123456

result = socket.htonl(data)#将主机序转换为网络序
print(result)

# print(socket.htons(data)) #转换成16位的数据

print(socket.ntohl(result)) #将网络序转换为主机序
