from multiprocessing import Process, current_process
import os
import time

def f(x):
    # print('module name:', __name__)
    # print('parent process:', os.getppid())
    # print('process id:', os.getpid())
    
    print(current_process().name)


def g(y):
    print(f'printing {y}')

if __name__ == '__main__':
    for _ in range(4):
        Process(target=f, args=(3,)).start()


    # print(f'cpu count {os.cpu_count()}')
    # with Pool(10) as p:
    #     print(type(p))
    #     # print(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    #     p.apply_async(g,"nitin")