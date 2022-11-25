# Editer : ding kai
# Function : 删除测试报告生成的临时文件
# Date : 2022/11/6 17:04

import os

# "../report/tmp"
def cleanTestFile(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

    for one in os.listdir(dir):
        print(one)
        if one.endswith('json') or one.endswith('txt'):
            os.remove(f'{dir}/{one}')



