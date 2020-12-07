import socketserver
host = '192.168.0.3'
port = 4444

#socketserver可以编写多线程的服务端
class MyTcpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                s.shutdown()
                break
            print("recv:  "+data.decode('utf-8'))
            send_data = input("> ")
            self.request.send(bytes(send_data,encoding='utf-8'))
        return
s = socketserver.TCPServer((host,port),MyTcpHandler)
s.serve_forever()
