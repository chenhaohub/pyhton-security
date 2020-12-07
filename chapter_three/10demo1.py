import socket
#获取主机名和ip地址
def get_local_machine_info():
    #获取主机名,只是用来获取文件共享的识别,ip地址更多的进行网络的通信
    hostname = socket.gethostname()
    #通过主机名获取的ip地址可能不准确,获取的可能是127.0.0.1是通过/etc/hosts对应得主机名的地址
    ip_addr = socket.gethostbyname(hostname)
    #通过这样获取的外界ip地址的方法
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    return hostname,ip
if __name__ == '__main__':
    hostname,ip_addr = get_local_machine_info()
    print('hostname: '+hostname)
    print('ip: '+ip_addr)