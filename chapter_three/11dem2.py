import  socket
'''
ports = ['21','22','23','25','80','110','3306','8080']#living ports


for port in ports:
    #通过端口和协议找不到相应的服务会报错
    serv_name = socket.getservbyport(int(port),'tcp')
    print(port +': '+ serv_name)
'''
# servs = ['ftp','ssh','telnet']
# for serv in servs:
#     port = socket.getservbyname(serv,'tcp')
#     print(serv+':'+str(port))

def getservfromport(living_ports):
    for port in living_ports:
        serv_name = socket.getservbyport(int(port),'tcp')
        print(port+': '+serv_name)

if __name__ == '__main__':
    linving_ports = ['21','22','23','25','80','110','3306','8080']
    getservfromport(linving_ports)