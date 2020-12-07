import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#bind当前的ip地址
# 服务端向客户端发送quit不会退出,会一直运行中,当客户端重新上线,可以重新接收数据
s.bind(('192.168.0.3',5001))
while True:
    # date = s.recv(1024)
    # print(date)
    data, addr = s.recvfrom(1024)
    if data == bytes('quit',encoding='utf-8'):
        break
    print(data)
    send_data = input("> ")
    s.sendto(bytes(send_data,encoding='utf-8'),addr)

s.close()
