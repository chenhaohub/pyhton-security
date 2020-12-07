import socket
import sys

domain = sys.argv[1]
result = socket.gethostbyname(domain)
print(domain+": "+result)