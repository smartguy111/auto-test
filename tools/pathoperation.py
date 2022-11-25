# Editer : ding kai
# Function : 路径操作
# Date : 2022/11/15 18:23

import os

# 获得项目根路径
def getRootPath(project_name):
    # 获取当前文件路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find(project_name) + len(project_name)]
    return rootPath


# 从根目录下开始获取指定路径
def getAssignPath(project_name: str, relativePath: str) ->str:
    # 调用了上述获得项目根目录的方法
    rootPath = getRootPath(project_name)
    assignPath = os.path.abspath(rootPath +'/' + relativePath)
    return assignPath

