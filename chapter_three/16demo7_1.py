import argparse
DEFAULT_LOCALHOST = '127.0.0.1'
parse = argparse.ArgumentParser(description='Port Forwarding Tool ')
parse.add_argument('--local-host',action='store',dest='local_host',default=DEFAULT_LOCALHOST)
parse.add_argument('--local-port',action='store',dest='local_port',type=int,required=True)
parse.add_argument('--remote-host',action='store',dest='remote_host',required=True)
parse.add_argument('--remote-port',action='store',dest='remote_port',required=True)

given_args = parse.parse_args()#将具体设置的参数传递到这里来,现在这样才会生效
local_host,remote_host = given_args.local_host,given_args.remote_host
local_port,remote_port = given_args.local_port,given_args.remote_port

print('(%s:%s)===>(%s:%s)'%(local_host,local_port,remote_host,remote_port))
