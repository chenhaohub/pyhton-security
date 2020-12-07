import socket
import binascii #转换16进制
ip_addr = '192.168.0.3'

#字符串ip转换为16进制
result = socket.inet_aton(ip_addr)
print(result)

#16进制ip转换为字符串ip
result_1 = socket.inet_ntoa(result)
print(result_1)

result_2 = binascii.hexlify(result)
print(result_2)