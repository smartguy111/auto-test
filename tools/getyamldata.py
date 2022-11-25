# Editer : ding kai
# Function : 读取yaml文件
# Date : 2022/11/12 21:51

import yaml
import logging
import logging.config as conf


def get_yaml_data_list(fileDir):
    """
    :param fileDir: yaml路径
    :return: list - 格式：[(dict, dict),(dict, dict)]
    """
    with open(fileDir, 'r', encoding='utf-8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        print(res)

    resultList = []
    for one in res:
        resultList.append((one['xml'], one['resp']))

    return resultList

def createXmlFile():
    pass

def get_yaml_data_dict(fileDir):
    """
    :param fileDir: yaml路径
    :return: dict  返回yaml配置文件字典
    """
    with open(fileDir, 'r', encoding='utf-8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)

    return res

def get_log_yaml_config():
    with open(file="../configs/logging.yml", mode='r', encoding="utf-8") as file:
        logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
        # 配置logging日志：主要从文件中读取handler的配置、formatter（格式化日志样式）、logger记录器的配置
        conf.dictConfig(config=logging_yaml)
    # 获取根记录器：配置信息从yaml文件中获取
    root = logging.getLogger()
    # 子记录器的名字与配置文件中loggers字段内的保持一致
    logger = logging.getLogger("auto-test")


if __name__ == '__main__':
    # get_yaml_data('/Users/dingkai/python/pythonProjects/auto-test/configs/case/nomalCredit-update.yml')
    get_log_yaml_config()
