import socket
#服务端
service_socket = socket.socket()
service_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#套接字重用
#addr = '192.168.57.134'
# addr = '192.168.0.3'

#获取本机ip地址
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
result = s.getsockname()[0]

addr = result
port = 4444
#客户端要的socket要绑定ip和port
service_socket.bind((addr,port))
#listen设置可以处理的连接数
service_socket.listen(5)
#循环等待连接

while True:
    client_socket, addr = service_socket.accept()
    while True:
        data = client_socket.recv(1024) #接收数据
        if data.decode() == 'quit':
            client_socket.close()
            service_socket.close()#这个是否有关闭的必要?
            break
        else:
            print(data)
        send_data = input("> ")
        if send_data == 'quit':
            client_socket.send(bytes(send_data, encoding='utf-8'))
            client_socket.close()
            service_socket.close()
            exit(0)

        client_socket.send(bytes(send_data,encoding='utf-8'))#发送的数据类型是bytes类型
    client_socket.close()
    break
service_socket.close()

