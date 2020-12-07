#coding = utf-8
#create 2020/12/2
#滚动输出
import sys
import time
def print_act(word):
    sys.stdout.write("r")
    sys.stdout.flush()
    for item in word:
        sys.stdout.write(item)
        sys.stdout.flush()
        time.sleep(0.3)

if __name__ == '__main__':
    print('test' + "=================" + 'test')
    while True:
        print_act('rolling      rolling')