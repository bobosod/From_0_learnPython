import os
from multiprocessing import Process

def run_proc(name):
    print('子进程' +name+ '在运行，进程号为' + str(os.getpid()))

if __name__ == '__main__':
    print('父进程' + str(os.getpid()))
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print(str(i) + '号程序将要启动')
        p.start()
    p.join()
    print('进程结束')