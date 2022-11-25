# Editer : ding kai
# Function : ...
# Date : 2022/11/14 19:27


import time

def show_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return inner # 函数对象


def foo():
    print('-----test------')
    time.sleep(1)


if __name__ == '__main__':
    show_time(foo)
