# coding=utf-8
# create 2020/12/5
import zipfile
import sys

z = zipfile.ZipFile(sys.argv[1])

#zip 暴力破解
with open('test.txt') as f:
    pass_list = f.readlines()
    for line in pass_list:
        try:
            z.extractall(pwd=bytes(line.strip()),encoding='utf-8')#pyhton3的pwd要传bytes类型
            print('sucecessful'+line)
            exit(0)
        except:
            pass
print('your dict is small ')