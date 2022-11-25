# Editer : ding kai
# Function : fixture配置
# Date : 2022/11/13 18:24

import pytest
from tools.logger import logger

log = logger()

@pytest.fixture(scope='session', autouse=True)
def start_demo(request):
    print('-------自动化测试开始执行---------')

    def fin():
        # 数据清除写这里
        print('---------自动化测试结束---------')

    request.addfinalizer(fin)


# 不自动执行
@pytest.fixture(scope='function', autouse=False)
def normal_credit_init():
    log.info('normal_credit_init....')
    print('这里可以对测试方法进行扩展')