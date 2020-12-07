import socket
import sys
#端口扫描
#"192.168.57.134"
def port_scan(hostname):
    for port in range(0,66536):
        try:
            s = socket.socket()
            #s.settimeout(1)
            #s.connect(sys.argv[1], port)
            s.connect((hostname,port))
            print('Open:'+ str(port))
            s.close()
        except:
            #print('Close:  ' + str(port))
            s.close()
