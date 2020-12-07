import  socket

#默认情况下不写family和type的入参是创建一个tcp的socket
tcp_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
