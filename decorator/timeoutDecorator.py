# Editer : ding kai
# Function : 超时处理装饰器
# Date : 2022/11/15 20:44

import time
from func_timeout import func_set_timeout, FunctionTimedOut
from tools.logger import logger

log = logger()

def time_out(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except FunctionTimedOut:
            print('函数调用超时..')
            log.error(str(func) + '函数调用超时..', exc_info=True)

    return wrapper


@time_out
@func_set_timeout(1)
def foo(name):
    time.sleep(2)
    print(name + 'is hls')
    return 'b'


if __name__ == '__main__':
    c = foo(name='my name')
    print(c)
