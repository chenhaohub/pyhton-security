import socket

client_socket = socket.socket()
ip = '192.168.0.3'
port = 4444

client_socket.connect((ip,port))
while True:
    data = input(">")
    if data == 'quit':
        client_socket.send(bytes(data, encoding='utf-8'))
        client_socket.close()
        break
    client_socket.send(bytes(data,encoding='utf-8'))

    recv_data = client_socket.recv(1024)#返回的也是bytes
    if recv_data.decode() == 'quit':
        client_socket.close()
        break
    else:
        print(recv_data)

