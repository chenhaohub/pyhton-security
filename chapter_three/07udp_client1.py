import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    send_data = input('> ')
    s.sendto(bytes(send_data, encoding='utf-8'), ('192.168.0.3', 5001))
    if send_data == 'quit':
        break
    recv_data, addr = s.recvfrom(1024)
    print(recv_data)
    if recv_data == bytes('quit',encoding='utf-8'):
        break
s.close()