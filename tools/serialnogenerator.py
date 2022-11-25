# Editer : ding kai
# Function : 生成序号
# Date : 2022/11/17 15:21
from tools.pathoperation import getAssignPath
from tools.logger import logger
log = logger()
def generate(startNum: int, count: int) :
    '''
    :param startNum: 初始值, 默认为1
    :param count: 生成个数
    :return:
    '''
    num = startNum
    counter = 0
    while True:
        if counter > count:
            break
        num += 1
        yield num
        counter += 1

def getSerialNoList(count: int) -> list:
    '''
    :param count: 序号生成个数
    :return: 序号列表

    获取当前序号，可一次获取多个序号，返回序号列表
    ps: 当前序号值在项目根目录下serial.ini文件中查看
    '''
    startNum = 1
    lst = []
    with open(getAssignPath('auto-test', 'serial.ini'), 'r+', encoding='utf-8') as f:
        numStr = f.readline()
        if numStr.isnumeric():
            startNum = int(numStr)
        elif numStr == "" or numStr is None:
            startNum = 1
        else:
            log.error("serial.ini配置错误，必须是数字")
            raise Exception("serial.ini配置错误，必须是数字")

        generator = generate(startNum, count)
        for counter in range(count):
            lst.append(next(generator))
        newStartNum = lst[-1]
        log.info("当前序号使用：{}".format(newStartNum))
        f.seek(0) # 文件指针移动到行首，覆盖为新的序号值
        f.write(str(newStartNum))
    return lst

if __name__ == '__main__':
    numList = getSerialNoList(5)
    print(numList)
