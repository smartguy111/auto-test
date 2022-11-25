# Editer : ding kai
# Function : ...
# Date : 2022/11/14 19:09

import sys
import os

# 获得根路径
def getRootPath(project_name):
    # 获取当前文件路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find(project_name) + len(project_name)]
    return rootPath

if __name__ == '__main__':
    print(getRootPath('auto-test'))


    # pass



