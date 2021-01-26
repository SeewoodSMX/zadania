import time

from random import randint


def foo1(l_list):
    print("Method 1")
    start = time.time()
    for i in l_list:
        if i == -1:
            print('found')
            break
    end = time.time()
    print('elapsed:', end - start, 'sec')


def foo2(l_list):
    print("Method 2")
    start = time.time()
    for i in range(1000000):
        if l_list[i] == -1:
            print('found')
            break
    end = time.time()
    print('elapsed:', end - start, 'sec')


def foo3(l_list):
    print("Method 3")
    t = time.process_time()
    for i in l_list:
        if i == -1:
            print('found')
            break
    elapsed_time = time.process_time() - t
    print('elapsed:', elapsed_time, 'sec')


long_list = [randint(0, 3000) for element in range(1000000)]
foo1(long_list)
foo2(long_list)
foo3(long_list)
