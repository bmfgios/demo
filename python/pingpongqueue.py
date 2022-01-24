import multiprocessing
import os


def sub_task(queue):
    print('子进程进程号:', os.getpid())
    n = 0
    while n < 5:
        queue.put('Pong')
        n += 1


if __name__ == '__main__':
    print('当前进程号:', os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=sub_task, args=(queue,))
    p.start()
    n = 0
    while n < 5:
        queue.put('Ping')
        n += 1
    p.join()
    print('子任务已经完成.')
    for _ in range(10):
        print(queue.get(), end='')